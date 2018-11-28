#include <stdio.h>
#include <iostream>
using namespace std;
typedef long long  INT64;
const int SIZE = 1050;

INT64 R,K,N;
INT64 dat[SIZE];
INT64 dp[SIZE];
INT64 pep[SIZE]; 
void init();
void prework();
INT64 work();
int main(){
	int cas;
	cin>>cas;
	for (int i=0;i<cas;i++){
		init();
		prework();
		INT64 ans=work();
		cout<<"Case #"<<(i+1)<<": "<<ans<<endl;
	}
	return 0;
}
void init(){
	cin>>R>>K>>N;
	for (int i=0;i<N;i++){
		cin>>dat[i];
	}
}
void prework(){
	for (int i=0;i<N;i++){
		INT64 sum=dat[i];
		int j=(i+1)%N;
		int tmp=sum+dat[j];
		
		while (tmp<=K && j!=i){
			sum=tmp;
			j=(j+1)%N;
			tmp=sum+dat[j];
		}
		dp[i]=sum;
		pep[i]=j;
	}
	/*
	for (int i=0;i<N;i++){
		printf("%d: dp: %lld ,pep: %lld\n",i,dp[i],pep[i]);
	}
	*/
}
INT64 work(){
	INT64 sum=0;
	int st=0;
	for (int i=0;i<R;i++){
		sum+=dp[st];
		st=pep[st];
	}
	return sum;
}