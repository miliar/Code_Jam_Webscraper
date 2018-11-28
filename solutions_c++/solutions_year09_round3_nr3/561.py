#define _CRT_SECURE_NO_DEPRECATE

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

using namespace std;

typedef pair<int, int> pt;
typedef unsigned char byte;
typedef vector<vector<int> > matrix;

int fact(int n)
{
	return (n == 1? 1: n * fact(n - 1));
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

	int t;
	cin >> t;

	forn(test, t)
	{
		int n, m;
		cin >> n >> m;
		vector<int> a(m);
		forn(i, m)
			cin >> a[i], a[i]--;
		sort(all(a));

		int ans = INT_MAX / 2;
		vector<int> perm(m);
		forn(i, perm.size())
			perm[i] = i;
		forn(i, fact(m))
		{
			int res = 0;
			vector<int> used(n, false);
			forn(i, a.size())
			{
				int idx = perm[i];
				int j = idx - 1;

				while(j > -1 && !used[j])
					j--;
				if(j == -1)
					res += a[idx];
				else
					res += a[idx] - a[j] - 1;

				j = idx + 1;

				while(j < m && !used[j])
					j++;
				if(j == m)
					res += n - a[idx] - 1;
				else
					res += a[j] - a[idx] - 1;

				used[idx] = true;
			}

			ans = min(ans, res);
			next_permutation(all(perm));
		}
		printf("Case #%d: %d\n", test + 1, ans);
	}

    return 0;
}