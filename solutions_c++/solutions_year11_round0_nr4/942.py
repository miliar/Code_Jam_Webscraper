#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int tc = 0; tc < t; tc++)
	{
		int n;
		cin >> n;
		vector <int> p(n);
		for(int i = 0; i < n; i++)
		{
			cin >> p[i];
			p[i]--;
		}
		vector <bool> was(n, false);
		int ans = 0;
		for(int i = 0; i < n; i++)
			if(!was[i])
			{
				int now = i;
				int cnt = 0;
				while(p[now] != i)
				{
					cnt++;
					now = p[now];
					was[now] = true;
				}
				if(cnt > 0)
					ans += cnt + 1;
			}
			printf("Case #%d: %.9lf\n", tc + 1, (double)ans);
	}
	return 0;
}