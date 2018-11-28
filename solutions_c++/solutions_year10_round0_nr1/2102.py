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
const int MAXN = 1000;

string s;

ll mask[50];
int tk, n;

ll next(ll ma){
	if (ma == mask[n] - 1) return 0;

	ll res = ma;
	forn(i, n){
		if (ma & mask[i]){
			res -= mask[i];
			continue;
		}

		res += mask[i];
		return res;
	}
	return res;
}

int main()
{
    freopen("input.txt","rt", stdin);
    freopen("output.txt", "wt", stdout);    
    
	mask[0] = 1;
	forn(i, 35){
		mask[i + 1] = mask[i] * 2;
	}

	
	ll k;
	cin >> tk;

	forn(ii, tk){
		cin >> n >> k;
		
		ll T = mask[n];

		k %= T;

		if (k + 1 == T){
			printf("Case #%d: ON\n", ii + 1);
		}
		else
			printf("Case #%d: OFF\n", ii + 1);
		
		continue;
		/*
		ll ma = 0;
		for(int i = n; i > 0; --i){
			ll q = mask[i] - 1;
			
			if (k >= q){
				k -= q;
				ma = mask[i] - 1;
			}
			forn(j, k){
				ma = next(ma);
			}
		}

		printf("Case #%d: %s\n", s.c_str());
		*/
	}
    return 0;
}

