#include <iostream>
#include <stdio.h>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>
#include <utility>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int) (n); ++i)
#define fore(i, a, b) for(int i = (int) (a); i < (int) (b); ++i)

#define ll long long
#define ld long double
#define PLL pair <ld, ld>
#define PII pair <int, int>

const ld EPS = 1e-9;
const int MAXN = 100000;

int a[MAXN], b[MAXN];

int main()
{
    freopen("input.txt","rt", stdin);
    freopen("output.txt", "wt", stdout);    

	int tk;
	cin >> tk;
	forn(ii, tk){
		int ans = 0;
		int n;
		cin >> n;
		forn(i, n){
			scanf("%d %d", &a[i], &b[i]);
		}

		forn(i, n){
			fore(j, i + 1, n){
				ll t1 = a[i] - a[j];
				ll t2 = b[i] - b[j];
				if (t1 * t2 < 0) ++ans;
			}
		}
		printf("Case #%d: %d\n", ii + 1, ans);
	}
          
    return 0;
}

