#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <algorithm>
typedef long long LL;
using namespace std;
#define F_IN  "A-large.in"
#define F_OUT "A-large.out"
//#define F_IN  "a.in"
//#define F_OUT "a.out"
#define PI 3.1415926535897932384626433832795
#define MAXN  11000
#define INF 1000001000
int l[MAXN];
int d[MAXN];
int ans[MAXN];
int n;

int k, rope, pos;

int main()
{
    int tc, tt, best, besti;
	int bestrope, bestpos;
    freopen(F_IN, "r", stdin);
    freopen(F_OUT, "w", stdout);
    scanf("%i", &tc);
    for(tt=1; tt<=tc; ++tt)
    {
		scanf("%i", &n);
		for(int i=0; i<n; ++i) scanf("%i %i", &d[i], &l[i]);
		scanf("%i", &d[n]);
		ans[n] = 0;
		for(int i=n-1; i>=0; --i) {
			ans[i] = INF;
			for(int j=i+1; j<=n; ++j) {
				if (d[j] - d[i] > l[i]) break;
				int mx;
				if (d[j] - d[i] > l[j]) mx = l[j]; else mx = d[j] - d[i];
				if (mx >= ans[j]) {
					if (d[j] - d[i] < ans[i]) ans[i] = d[j] - d[i];
				}
			}
		}
		cerr << tt << endl;
		if (ans[0] <= d[0]) 
			printf("Case #%i: YES\n", tt);
		else 
			printf("Case #%i: NO\n", tt);
    }

    return 0;
}


