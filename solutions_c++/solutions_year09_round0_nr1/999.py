#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <string>
#include <set>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)n; ++i)

int l, d, n;
string str[10000];
bool used[10000];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> l >> d >> n;
	forn(i, d)
		cin >> str[i];
	
	forn(i, n)
	{
		memset(used, 1, sizeof used);
		string s;
		cin >> s;
		int cur = 0;
		while (true)
		{
			if (s.length() == 0)
				break;
			
			set<char> st;
			if (s[0] != '(')
			{
				st.insert(s[0]);
				s = s.substr(1);
			}
			else
			{
				s = s.substr(1);
				while (s[0] != ')')
				{
					st.insert(s[0]);
					s = s.substr(1);
				}
				s = s.substr(1);
			}

			forn(j, d)
			{
				if (!used[j])
					continue;
				if (st.count(str[j][cur]) == 0)
					used[j] = false;
			}

			++cur;
		}

		int ans = 0;
		forn(j, d)
			if (used[j])
				++ans;
		printf("Case #%d: %d\n", i + 1, ans);
	}

	return 0;
}

