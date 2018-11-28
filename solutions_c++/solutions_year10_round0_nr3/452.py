#include<iostream>

using namespace std;

int t,r,k,n;
int g[2000];
int q[2000],p[2000],ss[2000];

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&t);
	int tt = 0;
	while (t > 0)
	{
		t--;
		tt++;
		scanf("%d%d%d",&r,&k,&n);
		for (int i = 0; i < n; i++) scanf("%d",&g[i]);
		long long ans = 0;
		int st = 0;
		for (int i = 0; i < n; i++) q[i] = -1;
		for (int i = 0; i < r; i++)
		{
			int s = 0;
			int  p = 0;
			int ts = st;
			if (q[ts]==-1){
			while ((s + g[st] <= k) && (p < n))
			{
				p++;
				s = s + g[st];
				ans = ans + g[st];
				st = (st + 1) % n;
			}
			q[ts] = st;
			ss[ts] = s;
			}else {ans = ans + ss[ts];st = q[ts];}
		}
		printf("Case #%d: %lld\n",tt,ans);
	}
}
