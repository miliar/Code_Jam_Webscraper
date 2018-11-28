#include<iostream>
using namespace std;

int C(int t)
{
	int ret=0;
	while( t%2 == 0 )
	{
		ret++;
		t>>=1;
	}
	return ret;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int cas,kkk=1;
	int N,K;
	scanf("%d",&cas);
	while( cas-- )
	{
		scanf("%d%d",&N,&K);
		printf("Case #%d: ",kkk++);
		if( C(K+1) >= N) puts("ON");
		else puts("OFF");
	}
}