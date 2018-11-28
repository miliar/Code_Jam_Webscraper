#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

string solve()
{
	char A[300][300];
	bool O[300][300];
	memset(A, 0, sizeof(A));
	memset(O, 0, sizeof(O));
	int c, d, n;
	cin >> c;
	string s;
	for (int i = 0; i < c; i++)
	{
		cin >> s;
		A[s[0]][s[1]] = s[2];
		A[s[1]][s[0]] = s[2];
	}
	cin >> d;
	for (int i = 0; i < d; i++)
	{
		cin >> s;
		O[s[0]][s[1]] = true;
		O[s[1]][s[0]] = true;
	}
	cin >> n;
	cin >> s;
	vector<char> r;
	map<char, int> m;
//	memset(used, 0, sizeof(used));
	for (int i = 0; i < n; i++)
	{
		m[s[i]]++;
		r.push_back(s[i]);
		if (r.size() == 1)
			continue;
		char q = A[r[r.size() - 1]][r[r.size() - 2]];
		if (q != 0)
		{
			m[r[r.size() - 1]]--;
			m[r[r.size() - 2]]--;
			r.pop_back();
			r.pop_back();
			r.push_back(q);
			continue;
		}
		//пробуем очистить строку
		for (map<char, int>::iterator it = m.begin(); it != m.end(); ++it)
		{
			if (it->second)
			{
				bool b = O[r[r.size() - 1]][it->first];
				if (b)
				{
					r.clear();
					m.clear();
					break;
				}
			}
		}
	}
	string ans = "";
	for (int i = 0; i < r.size(); i++)
		ans += r[i];
	return ans;
}


int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		string ans = solve();
		printf("Case #%d: ", i + 1);
		if (ans.size() == 0)
		{
			printf("[]\n");
			continue;
		}
		printf("[");
		for (int i = 0; i < ans.size() - 1; i++)
		{
			printf("%c, ", ans[i]);
		}
		printf("%c]\n", ans[ans.size() - 1]);
	}
}