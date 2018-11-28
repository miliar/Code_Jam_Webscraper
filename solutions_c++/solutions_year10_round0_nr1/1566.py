#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;

int N,K,T;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		printf("Case #%d: ",test);
		scanf("%d",&N);
		scanf("%d",&K);
		if(K%(1<<N)==(1<<N)-1)
			puts("ON");
		else
			puts("OFF");
	}
	return 0;
}


