#include <cstdio>
#include <cstring>
#include <set>
using namespace std;

int		A, B;

void solve()
{
	int cc = 0;
	
	int 	d[20];
	for (int n = A; n <= B; n ++)
	{
		int x = n;
		int k = 0;
		int w = 1;
		while (x)
		{
			d[k] = x % 10;
			x /= 10;
			w *= 10;
			k ++;
		}
		w /= 10;
		
		for (int p = 0; p < k; p ++)
			d[k + p] = d[p];
			
		int m = n;
		set<int> Set;
		for (int p = 0; p < k; p ++)
		{
			m = (m - d[p]) / 10 + w * d[p];
			if (d[p] && m > n && m <= B)
			{
				Set.insert(m);
			}
		}
		cc += Set.size();
	}
	
	printf("%d\n", cc);
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	
	int caseNo, t;
	scanf("%d", &caseNo);
	
	for (t = 1; t <= caseNo; t ++)
	{
		fprintf(stderr, "%d/%d", t, caseNo);
		scanf("%d%d", &A, &B);
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}