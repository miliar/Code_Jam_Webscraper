#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

__int64 n,K,tar,ti;
__int64 pos[110],v[110];
int can[110],cnt;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	int cs,cn=1,i,j;
	scanf("%d",&cs);
	while(cs--)
	{
		scanf("%I64d%I64d%I64d%I64d",&n,&K,&tar,&ti);
		for(i=0;i<n;i++) scanf("%I64d",&pos[i]);
		for(i=0;i<n;i++) scanf("%I64d",&v[i]);
		cnt = 0;
		memset(can,0,sizeof(can));
		for(i=0;i<n;i++)
		{
			if(v[i]*ti >= tar-pos[i])
			{
				can[i] = 1;
				cnt++;
			}
		}
		if(cnt < K)
		{
			printf("Case #%d: IMPOSSIBLE\n",cn++);
		}
		else
		{
			int ans = 0,cc = 0;
			for(i=n-1;i>=0;i--) if(can[i])
			{
				for(j=i+1;j<n;j++) if(!can[j])
				{
					ans++;
				}
				cc++;
				if(cc == K) break;
			}
			printf("Case #%d: %d\n",cn++,ans);
		}
	}
	return 0;
}

