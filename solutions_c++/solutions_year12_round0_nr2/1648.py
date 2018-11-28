#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int	n, s, p;
int	list	[110];

int	opt		[110][110];

void renew(int& x, int x0)
{
	if (x0 > x) x = x0;
}

void solve()
{
	scanf("%d%d%d", &n, &s, &p);
	for (int i = 0; i < n; i ++)
		scanf("%d", &list[i]);
		
	memset(opt, 0xff, sizeof(opt));
	opt[0][0] = 0;
	
	for (int i = 0; i < n; i ++)
	{
		for (int k = 0; k <= s; k ++)
		{
			if (opt[i][k] < 0) continue;
			
			int x = list[i];
			
			// not-sup
			int av = x / 3;
			int bv = av + int(x % 3 > 0);
			
			renew(opt[i+1][k], opt[i][k] + int(bv >= p));
			
			// sup
			for (int a = max(av - 2, 0); a <= max(av + 2, 10); a ++)
				for (int b = max(av - 2, a); b <= max(av + 2, 10); b ++)
				{
					int c = list[i] - a - b;
					if (c < b) break;
					if (c - a == 2)
					{
						renew(opt[i+1][k+1], opt[i][k] + int(c >= p));
					}
				}
		}
	}
	
	printf("%d\n", opt[n][s]);
}

int main()
{
	freopen("B-large.in", "r", stdin);
//	freopen("in.txt", "r", stdin);
//	freopen("B-small-2.out", "w", stdout);
	freopen("B-large.out", "w", stdout);
	
	int caseNo, t;
	scanf("%d", &caseNo);
	
	for (t = 1; t <= caseNo; t ++)
	{
		printf("Case #%d: ", t);
		
		solve();
	}
	return 0;
}