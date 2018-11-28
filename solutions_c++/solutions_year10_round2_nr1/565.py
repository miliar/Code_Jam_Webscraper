#include<iostream>
#include<stdio.h>
#include<string.h>
#include<string>
#include<map>

using namespace std;
map<string,bool> Dict;
int main(){
	int t,T=1;
	cin>>t;
	while(T<=t){
		Dict.clear();
		//cn=0;
		int N,M,i,j,k,nmkd=0;
		string p;
		cin>>N>>M;

		for(i=0;i<N;i++){
			cin>>p;
			Dict[p]=true;
		}
		for(i=0;i<M;i++){
			cin>>p;
			j=p.size()-1;
			while(j>=0){
				if(Dict.count(p)!=0)break;
				Dict[p]=true;
				k=j;
				while(p[j]!='/'){
					j--;
				}
				nmkd++;
				p.erase(j,k);
				j--;
			}

		}
		printf("Case #%d: %d\n",T,nmkd);
		T++;
	}
	return 0;
}
