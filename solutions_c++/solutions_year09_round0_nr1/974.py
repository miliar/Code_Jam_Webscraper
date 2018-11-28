#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <string>

#define pb push_back
#define mp make_pair
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()

using namespace std;

typedef pair<int, int> ii;
typedef long long int64;
typedef vector<int> vi;

vector<string> v;
bool pattern[50][40];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int l, d, n;
	cin >> l >> d >> n;
	for (int i = 0; i < d; i++)
	{
		string s;
		cin >> s;
		v.pb(s);
	}
	for (int it = 0; it < n; it++)
	{
		int res = 0;
		string s;
		cin >> s;
		int tok = 0;
		int cur = 0;
		memset(pattern, 0, sizeof(pattern));
		while (tok < l)
		{
			if (s[cur] != '(')
			{
				pattern[tok][s[cur] - 'a'] = true;
				tok++;
				cur++;
				continue;
			}
			cur++;
			while (s[cur] != ')')
			{
				pattern[tok][s[cur] - 'a'] = true;
				cur++;
			}
			tok++;
			cur++;
		}
		for (int i = 0; i < sz(v); i++)
		{
			bool ok = true;
			for (int j = 0; j < l; j++)
			{
				if (!pattern[j][v[i][j] - 'a'])
				{
					ok = false;
					break;
				}
			}
			if (ok) res++;
		}
		printf("Case #%d: %d\n", it + 1, res);
	}
	return 0;
}
