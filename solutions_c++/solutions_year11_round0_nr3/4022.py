#include <iostream>
#include <vector>
using namespace std;


struct pile{
	long sean_val;
	long patric_val;
};

vector<long> *test_c;
int antal_tests= 0;

void read();
long solve(long stykker_tilbage, pile sean,pile patric,vector<long> slik,int placering);

long dyn[1000];





int main(){
	read();
	for (int i=0;i<antal_tests;i++){
	/*	for (int k=0;k<1000;k++){
			dyn[k]=-2;
		}*/
		pile a;
		pile b;
		a.patric_val =0;
		a.sean_val =0;
		b = a;

		long res = solve(test_c[i].size(),a,b,test_c[i],0);
		printf("Case #%i: ", i+1);
		if (res ==-1){
			printf("NO");
		}else{
			printf("%ld",res);
		}
		printf("\n");
		
	}

	return 0;
}





long solve(long stykker_tilbage, pile sean,pile patric,vector<long> slik,int placering){
	/*
	if (dyn[placering]!=-2){
		return dyn[placering];
	}
	*/
	//printf("solve(%i,%i\n",stykker_tilbage,placering);
	
	
	if(stykker_tilbage==0){
		// test at patrik ikke græder
		if (sean.patric_val ==patric.patric_val&&sean.sean_val !=0 &&patric.sean_val!=0){
			if (sean.sean_val>patric.sean_val){
				return sean.sean_val;
			}
			else{
				return patric.sean_val;
			}
			// græder ikke.
		}else{
			//han græder .. suk
			return -1;
		}
	

	}


	// 2 muligheder.
	// prøv at ligge til i seans stak, eller patriks stak

	
	// prøv sean

	pile backup = sean;
	sean.sean_val+=slik[placering];
	sean.patric_val = sean.patric_val^slik[placering];
	long temp1 = solve(stykker_tilbage-1,sean,patric,slik,placering+1);
	sean = backup;
	// prøv patrik

	patric.sean_val+=slik[placering];
	patric.patric_val = patric.patric_val^slik[placering];
	long temp2 = solve(stykker_tilbage-1,sean,patric,slik,placering+1);
	patric = backup;
	
   // se  hvad for en er bedst:


	if (temp1>temp2){/*
		 dyn[placering] = temp1;*/
		return temp1;
	}else{/*
		 dyn[placering]= temp2;*/
		return temp2;
	}








}

void read(){
	cin>>antal_tests;
	test_c = new vector<long>[antal_tests];
	for(int i=0;i<antal_tests;i++){
		int antal_slik =0;
		cin >> antal_slik;
		for (int y=0;y<antal_slik;y++){
			long temp=0;
			cin >> temp;
			test_c[i].push_back(temp);
		}
		
	}




}