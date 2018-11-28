#include <stdlib.h>
#include <iostream>
//#include <string>
//#include <list>
using namespace std;

int L, D, N;

char dict[5001][16];
//list<string> dict;

char compstr[5000];
int comp();

int main(){
	cin>>L>>D>>N;
	for(int i=0; i<D; i++)
		cin>>dict[i];
/*
	for(int i=0; i<D; i++)
		cout<<dict[i]<<'\n';
*/
	for(int i=0; i<N; i++){
		cin>>compstr;
		cout<<"Case #"<<i+1<<": "<<comp()<<'\n';
	}
	cout<<'\n';
//	system("pause");
	return 0;
}

int comp(){
	int rst=0;
	bool good=0;
	
	for(int i=0; i<D; i++){

		char *pos=compstr;

		for(int j=0; j<L; j++){
			if(dict[i][j]==*pos){
				good=1;
//				cout<<'<'<<*pos;
			}else if(*pos=='('){
				pos++;
				while(*pos!=')'){
					if(dict[i][j]==*pos) good=1;
					pos++;
				}
			}
			if(good){
				if(j==L-1) rst++;
				good=0;
				pos++;
			}else
				break;
		}
	}


	return rst;
}