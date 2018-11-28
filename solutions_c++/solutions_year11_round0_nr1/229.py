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
#define pb push_back

const ld EPS = 1e-9;
const int MAXN = 10000;
const int INF = (int)(1e9 + 1e-9);

int t[2];
char tmp[MAXN];

void up(int &a, int b){
	a = min(a, b);
}


int main()
{
    freopen("input.txt","rt", stdin);
    freopen("a.out", "wt", stdout);    
	
	int tk;
	cin >> tk;

	forn(ii, tk){
		int n;
		cin >> n;

		forn(j, 2){
			t[j] = 1;
		}
		int ans = 0;
		int dt = 0, pr = -1, p;

		forn(i, n){
			scanf("%s", &tmp);

			int x = 1;
			if (tmp[0] == 'O') x = 0;

			cin >> p;

			int d = abs(t[x] - p);

			if (pr != x){
				d = max(0, d - dt) + 1;
				dt = d;
			}
			else
			{
				++d;
				dt += d;
			}

			pr = x;
			t[x] = p;
			
			ans += d;
		}

		printf("Case #%d: %d\n", ii + 1, ans);

	}

	return 0;
}

