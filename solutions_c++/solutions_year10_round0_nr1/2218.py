#include<iostream>

using namespace std;

long P[32];

int main()
{
	int i,T,N;
	long K;
	bool flag;
	cin>>T;
	P[1]=1;
	for(i=2;i<32;i++){
		P[i]=2*P[i-1]+1;
	}
	for(i=0;i<T;i++){
		scanf("%d %ld",&N,&K);
		if(K>0){
			K%=P[N]+1;
		}
		flag=false;
		if(K==P[N])
			flag=true;
		if(!flag)
			printf("Case #%d: OFF\n",i+1);
		else
			printf("Case #%d: ON\n",i+1);
	}
	return 0;
}