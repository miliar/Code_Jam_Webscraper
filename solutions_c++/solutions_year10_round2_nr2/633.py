#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int n, ttime, m, t;
long long x[100];
long long v[100];
long long b;
int ans;
int sw;
bool run[100];


int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		printf("Case #%d: ", tt);
		cin >> n >> m >> b >> ttime;
		for (int i = 0; i < n; i++)
			cin >> x[i];
		for (int i = 0; i < n; i++)
			cin >> v[i];
		for (int i = n - 1; i >= 0; i--)
		{
			long long xe = x[i] + ttime * v[i];
			if (xe >= b)
				run[i] = true;
			else
				run[i] = false;				
		}
		ans = 0;
		int curm = 0;
		for (int i = n - 1; i >= 0; i--)
		{
			if (run[i])
			{
				for (int j = i + 1; j < n; j++)
					if (!run[j])
						ans++;					
				curm++;
			}
			if (curm == m)
				break;
		}
		if (curm < m)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ans);
	}
	return 0;
}
