#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

int T;
int n;
int d[10005];
int l[10005];
int D;
int pre[10005];

int main()
{
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		scanf("%d",&n);
		for(int i=1;i<=n;i++)
		{
			scanf("%d%d",&d[i],&l[i]);
		}
		scanf("%d",&D);
		printf("Case #%d: ",test);
		int now=1;
		memset(pre,-1,sizeof(pre));
		pre[1]=0;
		bool flag=false;
		for(int i=1;i<=n;i++)
		{
			now=max(now,i+1);
			int t=min(l[i],d[i]-d[pre[i]]);
			while(pre[i]!=-1&&now<=n&&d[now]-d[i]<=t)
				pre[now++]=i;
			if(pre[i]!=-1&&D-d[i]<=t)
			{
				puts("YES");
				flag=true;
				break;
			}
		}
		if(!flag)
			puts("NO");
	}
	return 0;
}

