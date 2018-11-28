#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <queue>
#include <map>

using namespace std;

struct Order
{
	int cnt,flag;
}ord[1000];
int u[2][1000];
int flag[1000];

int main()
{
	int i,j,n;
	int cas=1;
	//freopen("A-large.in","r",stdin);
	//freopen("out.out","w",stdout);
	int t;scanf("%d",&t);
	while(t--)
	{
		u[0][0]=u[1][0]=0;
		memset(flag,0,sizeof(flag));
		scanf("%d",&n);
		for(i=1;i<=n;++i)
		{
			char a[2];
			int b;
			scanf("%s%d",a,&b);
			int kl=a[0]=='O'?0:1;
			ord[i].cnt=b,ord[i].flag=kl;
			u[kl][++u[kl][0]]=i;
		}
		flag[0]=1;
		int ans=0,he[2]={1,1},wei[2]={1,1};
		for(i=1;i<=n;++i)
		{
			int cnt=ord[i].cnt,f=ord[i].flag,ff=(f+1)%2;
			int t=abs(cnt-wei[f])+1;
			ans+=t;
			he[f]++;
			wei[f]=cnt;
			if(u[ff][0]==0||he[ff]==u[ff][0]+1) continue;
			int mm=ord[u[ff][he[ff]]].cnt;
			if(abs(wei[ff]-mm)<=t)
				wei[ff]=mm;
			else
			{
				wei[ff]=(mm-wei[ff])/abs(mm-wei[ff])*t+wei[ff];
			}
		}
		printf("Case #%d: %d\n",cas++,ans);
	}
}