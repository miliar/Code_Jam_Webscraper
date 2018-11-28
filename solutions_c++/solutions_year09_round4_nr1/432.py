#include<map>
#include<cmath>
#include<cstdio>
#include<vector>
#include<string>
#include<cstdlib>
#include<algorithm>

#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)

using namespace std;

int main()
{
	int T, cas, ans;
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	rep(cas,T)
	{
		int n, x[40], y;
		scanf("%d", &n);
		for(int i = 0; i < n; i ++)
		{
			x[i] = 0;
			for(int j = 0; j < n; j ++)
			{
				scanf("%1d", &y);
				if(y == 1)
				{
					x[i] >?= j;
				}
			}
		}
		int tmp, ans = 0, k;
		for(int i = 0; i < n; i ++)
		{
			for(int j = i; j < n; j ++)
			{
				if(x[j] <= i)
				{
					ans += (j-i);
					k = j;
					break;
				}
			}
			for(int j = k-1; j >= i; j --)
			{
				tmp = x[j];
				x[j] = x[j+1];
				x[j+1] = tmp;
			}
		}
		printf("Case #%d: %d\n", cas+1, ans);
	}
	return 0;
}
