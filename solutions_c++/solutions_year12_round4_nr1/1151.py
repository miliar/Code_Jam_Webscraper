#include <stdio.h>
#include <algorithm>

using namespace std;

const int maxn = 10000+6;

struct node
{
	int d, l;
	bool operator < (const node &a) const
	{
		return d<a.d;
	}
} a[maxn];
int pre[maxn];
int n, D;

int main()
{
	freopen("Alarge.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int T, cas, i, sd, sl, sofar, len, go;
	bool flag;
	scanf("%d", &T);
	for (cas=1; cas<=T; cas++)
	{
		scanf("%d", &n);
		for (i=0; i<n; i++)
		{
		  scanf("%d%d", &a[i].d, &a[i].l);
		  pre[i] = -1;
		}		
		scanf("%d", &D);
		pre[0] = 0;
		sofar = 1;  
		bool flag = false;
		for (i=0; i<n; i++)
		{
			if (pre[i]<0) continue;
			len = min(abs(a[i].d - pre[i]), a[i].l);
			go = a[i].d + len;
			while (sofar<n && go>=a[sofar].d)
			{
				if (a[sofar].d>a[i].d)
					pre[sofar] = a[i].d;
				sofar++;
			}
			if (go>=D)
			{
				flag = true;	
				break;
			}
		}	
		if (flag) printf("Case #%d: YES\n", cas);
		else printf("Case #%d: NO\n", cas);	
	}
	return 0;
}
/*
4
3
3 4
4 10
7 10
9

*/