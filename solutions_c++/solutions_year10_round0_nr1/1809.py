#include <cstdio>
#define LL long long
using namespace std;

int main()
{
	int cases,iD=1;
	LL one=1,N,K;

	for(scanf("%d",&cases);cases--;)
	{
		scanf("%lld %lld",&N,&K);
		printf("Case #%d: ",iD++);
		LL cycle=(1<<N);
		if((K%cycle)==cycle-1)
			puts("ON");
		else
			puts("OFF");
	}

	return 0;
}

