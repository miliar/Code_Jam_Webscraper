#include<iostream>
#include<sstream>

using namespace std;

int j, happy[10][100000], atual;

int transforma(int n, int b){
	int soma=0;
	while(n){
		soma=soma+((n%b)*(n%b));
		n/=b;
	}

	//cout<<"Atual= "<<atual<<endl;
	//cout<<"Soma= "<<soma<<endl;
	if(soma<atual){
		//cout<<happy[j][soma]<<endl;
		if(happy[j][soma]==1) return 1;
		else return 0;
	}
	if(happy[j][soma]==atual) return 0;
	else happy[j][soma]=atual;
	
	if(soma==1) return 1;
	else{
		//cout<<soma<<endl;
		if(transforma(soma,b)) return 1;
	}
	return 0;
}

int main(){
	string str;
	stringstream ss;
	int n,bases[10],total, number[10],flag,caso=1;
	cin>>n; cin.ignore();
	for(int i=0; i<n; i++){
		getline(cin,str);
		for(j=0; j<10; j++) for(int k=0; k<100000; k++) happy[j][k]=0;
		ss.clear();
		ss.str(str);
		total=0;
		while((ss>>bases[total])>0){
			total++;
		}
		//if(transforma(16,3,16)) cout<<"happy!\n";
		for(j=0; j<10; j++){
			happy[j][0]=1; happy[j][1]=1;
		}
		for(atual=2;;atual++){
			//cout<<atual<<endl;
			flag=1;
			//cin>>n;
			for(j=0; j<total; j++)
				if(transforma(atual,bases[j])==0){
					flag=0;
					happy[j][atual]=0;
					//cout<<atual<<" nao eh happy na base "<<bases[j]<<endl;
				       	//break;
				}
				else{
				       	happy[j][atual]=1;
					//cout<<atual<<" eh happy na base "<<bases[j]<<endl;
				}
			if(flag){
				cout<<"Case #"<<caso<<": "<<atual<<endl;
				caso++;
				break;
			}
			
		}


	}
	
}
