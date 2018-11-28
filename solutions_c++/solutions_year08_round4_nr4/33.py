#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cassert>
#include <cmath>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for (int i = 1; i <= int(n); i++)

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

typedef pair<int, int> pii;
typedef vector<int> VI;
typedef long long ll;

#define NMAX 10

int k, n; 
string s, t;

int p[NMAX];

void apply(int l)
{
	string t = "";
	forn(i, k)
	{
		t += s[p[i] + l];
	}	
	forn(i, k)
	{
		s[l + i] = t[i];
	}
}
void solve(int test)
{
	scanf("%d\n", &k);
	getline(cin, s);
	n = (int)s.size();

	forn(i, k) p[i] = i;

	int ans = 100000000;
	t = s;
	do
	{
		s = t;
		for (int i = 0; i < n; i += k)
		{
			apply(i);
		}
		int cnt = 1;
		for1(i, n - 1)
		{         	
			if (s[i] != s[i - 1]) ++cnt;
		}		
		ans = min(ans, cnt);
	} while (next_permutation(p, p + k));
	printf("Case #%d: %d\n", test, ans);
}
int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc; scanf("%d\n", &tc);
	forn(it, tc)
	{
		solve(it + 1);
	}

	return 0;
}
