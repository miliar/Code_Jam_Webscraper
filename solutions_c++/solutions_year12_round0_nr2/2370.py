#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

int tp[1000];

int main(){
	int T;
	cin>>T;
	for(int tt=0;tt<T;tt++){
		int S,N,P;
		cin>>N>>S>>P;
		int nct=0,res=0;
		for(int i=0;i<N;i++){
			int val;
			cin>>val;
			if(val%3==0){
				if(val/3>=P)
					res++;
				else if(val/3+1>=P && val!=0)
					nct++;
			}else if(val%3==1){
				if(val/3+1>=P)
					res++;
			}else if(val%3==2){
				if(val/3+1>=P)
					res++;
				else if(val/3+2>=P)
					nct++;
			}
		}
		if(nct>=S)
			res+=S;
		else
			res+=nct;
		cout<<"Case #"<<tt+1<<": "<<res<<endl;
	}
	return 0;
}
