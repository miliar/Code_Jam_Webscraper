#include<iostream>

using namespace std;

typedef unsigned long UL;
typedef unsigned long long ULL;

const ULL mod=100003;
const UL M = 510;

ULL binom[M][M]={0};
ULL C[M][M]={0}; //access [i][j] only for j<=i

int main()
{
	binom[0][0]=1;
	binom[1][0]=binom[1][1]=1;
	for(UL i=2; i< M; ++i)
		binom[1][i]=0;
	for(UL i=2; i< M; ++i)
	{
		binom[i][0]=1;
		for(UL j=1; j< M; ++j)
			(binom[i][j]=binom[i-1][j-1]+binom[i-1][j])%=mod;
	}

	C[0][0]=C[1][0]=C[1][1]=0;
	for(UL i=2; i<M; ++i)
	{
		C[i][0]=0;
		C[i][1]=1;
		for(UL j=2; j<i; ++j)
		{
			C[i][j]=0;
			for(UL z=0; z<=j-2; ++z)
				(C[i][j] += C[j][z+1]*binom[i-j-1][j-2-z])%=mod;
		}
		C[i][i]=0;
	}
	
	ULL ans[M]={0};
	for(UL i=0; i<M; ++i)
		for(UL j=0; j<M; ++j)
			(ans[i]+=C[i][j])%=mod;
	
	UL ntests;
	cin>>ntests;
	for(UL tt=1; tt<=ntests; ++tt)
	{
		UL n;
		cin>>n;
		cout<<"Case #"<<tt<<": "<<ans[n]<<'\n';
	}
}
