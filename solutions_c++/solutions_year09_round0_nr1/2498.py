#include<iostream>
#include<string>
#include<fstream>
using namespace std;


int main(void)
{
	int i=0;
	int j=0;
	int L,D,N;
	int** checker;
	char** array;
	const char*aa;

	string str;
	fstream text2;
	text2.open("ABCD");

	getline(text2,str);
	sscanf(str.c_str(),"%d%d%d",&L,&D,&N);
	
	array = new char*[L];
	for(i=0;i<L;i++){
		array[i] = new char[D];		
	}	
	
	checker = new int*[L];
	for(i=0;i<L;i++){
		checker[i] = new int[D];		
	}	
	

	for(i=0;i<D;i++){
		for(j=0;j<L;j++)
			checker[j][i]=0;
	}	
	
	for(i=0;i<D;i++){
		getline(text2,str);
		aa = str.c_str();
		for(j=0;j<L;j++)
			array[j][i]=aa[j];
	}	

	int k;
	int a;

	for(a=0;a<N;a++){
		
		
		for(i=0;i<D;i++){
			for(j=0;j<L;j++)
			checker[j][i]=0;
		}	
	

		int pntr=0;
		int inpar=0;	
		
		getline(text2,str);
		aa = str.c_str();

		

		for(j=0;j<str.size();j++)
		{
	
			if(aa[j]=='('){
				inpar=1;
				continue;
				}
			else if(aa[j]==')'){
				inpar=0;
				pntr++;
				}
			else {
				
				for(k=0;k<D;k++)
					if(array[pntr][k]==aa[j]){			
							
						checker[pntr][k]=1;					
					}
				if(!inpar)
					pntr++;
	
							
				
				}
		}	
		int fnd=1;
		int cnn=0;
		for(j=0;j<D;j++){
			fnd = 1;
			for(i=0;i<L;i++)
				if(!(checker[i][j]))
					fnd=0;
			if(fnd)
				cnn++;
			
		}
		cout<<"Case #"<<a+1<<": "<<cnn<<endl;
	}	
		
		
	
	
}

