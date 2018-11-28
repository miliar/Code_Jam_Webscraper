#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
//int sum[100]={0};
int solve[100];
int main(){
	int t,cn=0,i;
	//preprocessing
	//sum[0]=0;
	solve[0]=0;
	for(i=1;i<=35;i++){
		//sum[i]=i+sum[i-1];
		solve[i]=1+2*solve[i-1];
		//period will be solve[1]+1;
	}
	//sums are stored
	scanf("%d",&t);
	while(cn<t){
		int N,K,period;
		char state[10];
		scanf("%d %d",&N,&K);
		//2+E(n-1) is the key
		//cout<<solve[N]<<endl;
		period=1+solve[N];

		if((K+1)%period==0){
			strcpy(state,"ON");
		}
		else{
			strcpy(state,"OFF");
		}
		cn++;
		printf("Case #%d: %s\n",cn,state);

	}
	return 0;
}
