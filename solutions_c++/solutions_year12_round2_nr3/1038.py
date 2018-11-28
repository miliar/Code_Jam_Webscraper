#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#define _clr(a,b) (memset((a),(b),sizeof((a))));
#define print(cas) printf("Case #%d:\n",(cas)++); 
#define inf 1<<25;
using namespace std;
int a[25];
int vis[25],flag,n;
void dfs(int index,int sum1,int sum2)
{
	int i;
	if(sum1==sum2&&sum1&&sum2)
	{
			int temp=0;
			for(i=0;i<n;i++)
			{
				if(vis[i]==1){if(temp)printf(" ");printf("%d",a[i]);temp++;}
			}
			printf("\n");
			temp=0;
			for(i=0;i<n;i++)
			{
				
				if(vis[i]==2){if(temp)printf(" ");printf("%d",a[i]);temp++;}
			}
			printf("\n");
			flag=1;return ;
	}
	if(flag||index==n)return ;
	//printf("%d %d\n",sum1,sum2);
	dfs(index+1,sum1,sum2);
	vis[index]=1;
	dfs(index+1,sum1+a[index],sum2);
	vis[index]=2;
	dfs(index+1,sum1,sum2+a[index]);
	vis[index]=0;
}
int main()
{
	int cas=1,txt,i;
	freopen("1.in","r",stdin);
	freopen("2.txt","w",stdout);
	scanf("%d",&txt);
	while(txt--)
	{
		flag=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		_clr(vis,0);
		print(cas);
		dfs(0,0,0);
		if(!flag)
			puts("Impossible\n");
	}
	return 0;
}

