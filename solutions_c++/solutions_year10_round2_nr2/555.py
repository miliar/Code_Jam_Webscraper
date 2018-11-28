#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int chicks[1000];
int speed[1000];
int main(){
	int t,tt=1;
	cin>>t;
	while(tt<=t){
		int N,K,B,T,i,j,k,nswp=0,nur=0,rched=0,x,v;
		cin>>N>>K>>B>>T;

		for(i=0;i<N;i++){
			cin>>chicks[i];	
		}

		for(i=0;i<N;i++){
			cin>>speed[i];
		}

		//Greedy
		for(i=N-1;i>=0;i--){
			x=chicks[i];
			v=speed[i];
			if(x+v*T>=B){
				rched++;
				nswp+=nur;
			}
			else{
				nur++;
			}
			if(rched>=K)break;
		}
		if(rched<K){
			printf("Case #%d: IMPOSSIBLE\n",tt);
		}
		else{
			printf("Case #%d: %d\n",tt,nswp);
		}
		tt++;
	}
	return 0;
}
