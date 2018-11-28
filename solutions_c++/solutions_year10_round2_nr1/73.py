#include <iostream>
#include <set>
#include <string>
using namespace std;

string s, t;
set<string> S;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, nt, n, m, i, j;
	scanf("%d", &T);
	for (nt = 1; nt <= T; nt++)
	{
		scanf("%d%d", &n, &m);
		S.clear();
		S.insert("/");
		for (i = 0; i < n; i++)
		{
			cin >> s;
			s += '/';
			t = "";
			for (j = 0; j < s.size(); j++)
			{
				t.push_back(s[j]);
				if (s[j] == '/')
					S.insert(t);
			}
		}
		int ans = 0;
		for (i = 0; i < m; i++)
		{
			cin >> s;
			s += '/';
			t = "";
			for (j = 0; j < s.size(); j++)
			{
				t.push_back(s[j]);
				if (s[j] == '/' && S.find(t) == S.end())
				{
					ans++;
					S.insert(t);
				}
			}
		}
		printf("Case #%d: %d\n", nt, ans);
	}
	return 0;
}
