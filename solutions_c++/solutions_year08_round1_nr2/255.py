#include <stdio.h>
#include <algorithm>

#define MAX 110

#define ison(a,b) ( (a&(1<<b))?1:0 )

using namespace std;

pair<int,int> g[MAX][MAX];

int main()
{
	int ncases;
	int cnt;
	int i,j,k;
	int n,m;
	int reti,ret;
	int valid;
	int f2;

	scanf("%d",&ncases);
	for(cnt=1;cnt<=ncases;++cnt)
	{
		ret=-1;
		scanf("%d %d",&n,&m);
		for(i=0;i<m;++i)
		{
			scanf("%d",&k);
			g[i][0].first=k;
			for(j=1;j<=k;++j)
			{
				scanf("%d %d",&g[i][j].first,&g[i][j].second);
				--g[i][j].first;
			}
		}
		for(i=0;i<1<<n;++i)
		{
			valid=1;
			for(j=0;j<m && valid;++j)
			{
				f2=0;
				for(k=1;k<=g[j][0].first && !f2;++k)
				{
					if(g[j][k].second==ison(i,g[j][k].first))
						f2=1;
				}
				if(!f2)
				{
					valid=0;
				}
			}
			if(valid && (ret<0 || __builtin_popcount(i)<ret) )
			{
				ret=__builtin_popcount(i);
				reti=i;
			}
		}
		printf("Case #%d:",cnt);
		if(ret<0)
			printf(" IMPOSSIBLE\n");
		else
		{
			for(i=0;i<n;++i)
			{
				printf(" %d",reti%2);
				reti/=2;
			}
			printf("\n");
		}
	}
	return 0;
}







