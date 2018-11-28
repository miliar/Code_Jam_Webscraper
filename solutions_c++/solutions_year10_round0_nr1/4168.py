#include <algorithm>
#include <functional>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define inf 1000000000
#define pi (2*acos(0.0))
#define REP(i, n) for (int i = 0; (i) < (n); ++(i))
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()
#define foreach(it, c) for(typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define vi vector<int>
#define vvi vector< vi >
#define pii pair<int, int>
#define ll long long
#define C(a) memset((a), 0, sizeof((a)))
#define fill(a, v) memset((a), v, sizeof((a)))
#define sz(c) ((int)(c).size())
#define uniq(c) (c).resize(unique(all(c))-(c).begin())

int n, k, ans, t, deg2[35];


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	REP(i,35) deg2[i] = 1 << i;
	//cout << deg2[3];
	REP(cas,t) {
		scanf("%d", &n);
		scanf("%d", &k);
		if ((k+1) % deg2[n] == 0) printf("Case #%d: ON\n",cas+1);
		else printf("Case #%d: OFF\n",cas+1);
	}
	return 0;
}