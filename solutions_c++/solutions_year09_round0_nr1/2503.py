#define _SRT_NO_SECURE_DEPRECATE

#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <utility>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cassert>
#include <iomanip>

#define INF (INT_MAX / 2)
#define X first
#define Y second
#define ft first
#define sc second
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define pb push_back
#define mp(a, b) make_pair((a), (b))
#define forn(i, n) for(int i = 0; i < int(n); i++)
#define forl(i, n) for(int i = 1; i <= int(n); i++)
#define sqr(a) ((a) * (a))
#define PI 3.1415926535897932384626433832795
#define NMAX 5010

using namespace std;

typedef pair<int, int> pt;
typedef unsigned char byte;
typedef vector<vector<int> > matrix;

set<char> z[20];
string a[NMAX];

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

	int L, D, N;
	cin >> L >> D >> N;

	getline(cin, a[0]);
	forn(i, D)
		getline(cin, a[i]);

	forn(test, N)
	{
		string s;
		getline(cin, s);

		forn(i, 20)
			z[i].clear();

		for(int i = 0, k = 0; i < int(s.length()); k++)
		{
			if(s[i] == '(')
				while(s[++i] != ')')
					z[k].insert(s[i]);
			else
				z[k].insert(s[i]);
			i++;
		}

		int ans = 0;
		forn(i, D)
		{
			bool t = true;
			forn(j, a[i].size())
				if(z[j].find(a[i][j]) == z[j].end())
				{
					t = false;
					break;
				}
			if(t)
				ans++;
		}
		printf("Case #%d: %d\n", test + 1, ans);
	}

    return 0;
}