#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T,N;
	long K;
	scanf("%d",&T);
	for (int i=1;i<=T;++i)
	{
		scanf("%d%ld",&N,&K);
		if ((K&((1LL<<N)-1))==((1LL<<N)-1))
			printf("Case #%d: ON\n",i);
		else
			printf("Case #%d: OFF\n",i);
	}
	return 0;
}