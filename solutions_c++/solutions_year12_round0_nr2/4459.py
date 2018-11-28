#include <string.h>
#include <stdio.h>
#include <math.h>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
using namespace std;
#define mr 3200000
#define INF 1000000100

int T,cs = 1;
int n,m,p;
int a[110];
int vis[110];

int main()
{
	freopen("C:\\Users\\weilong.li.QUNARSERVERS\\Desktop\\B-large.in", "r", stdin);
	freopen("C:\\Users\\weilong.li.QUNARSERVERS\\Desktop\\out.txt", "w", stdout);
	setbuf(stdout, NULL);
	int i,j;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d%d",&n,&m,&p);
		for(i=0;i<n;i++) scanf("%d",&a[i]);
		sort(a,a+n);
		int maxd = 30, mind = 2*max(0,p-1) + p;
		int ans = 0;
		memset(vis,0,sizeof(vis));
		for(i=0;i<n;i++)
		{
			if(a[i]>=mind && a[i]<=maxd)
			{
				vis[i] = 1;
				ans++;
			}
		}
		while(m--)
		{
			for(i=0;i<n;i++) if(!vis[i])
			{
				if(a[i]<mind && a[i]>=2*max(0,p-2)+p)
				{
					vis[i] = 1;
					ans++;
					break;
				}
			}
		}
		printf("Case #%d: %d\n",cs++,ans);
	}
	return 0;
}
