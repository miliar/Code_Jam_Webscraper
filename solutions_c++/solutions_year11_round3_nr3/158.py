#include <iostream>
using namespace std;

int a[110];

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("1.out","w",stdout);
	int T,cas;
	scanf("%d",&T);
	for(cas=1;cas<=T;++cas)
	{
		int N,L,H;
		scanf("%d%d%d",&N,&L,&H);
		int i,j;
		for(i=1;i<=N;++i)
		{
			scanf("%d",&a[i]);
		}
		for(i=L;i<=H;++i)
		{
			for(j=1;j<=N;++j)
			{
				if(i%a[j]==0||a[j]%i==0)
					;
				else
					break;
			}
			if(j>N)
			{
				printf("Case #%d: %d\n",cas,i);
				break;
			}
		}
		if(i>H)
		{
			printf("Case #%d: NO\n",cas);
		}
	}

	return 0;
}