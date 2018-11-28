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
const int MAXN = 20000;

int a[MAXN];
int next[MAXN];
ll sum[MAXN];

int main()
{
    freopen("input.txt","rt", stdin);
    freopen("output.txt", "wt", stdout);    
    
	int tk;
	cin >> tk;


	forn(ii, tk){
		ll ans = 0;
		int r, k, n;

		cin >> r >> k >> n;

		forn(i, n){
			cin >> a[i];
		}

		forn(i, n){
			sum[i] = a[i];
			next[i] = i + 1;
			
			int idx = i;

			for(int j = (i + 1) % n; j != i; j = (j + 1) % n){
				if (sum[i] + a[j] <= k){
					sum[i] += a[j];
					idx = j;
				}
				else
					break;
			}
			next[i] = (idx + 1) % n;
		}

		int t = 0;
		forn(i, r){
			ans += sum[t];
			t = next[t];
		}

		printf("Case #%d: %lld\n", ii + 1, ans);

	}
          
    return 0;
}

