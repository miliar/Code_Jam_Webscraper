#pragma comment(linker, "/STACK:64000000")
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
const int MAXN = 1100;

int a[MAXN][MAXN];
ll l, p, c;

int go(ll l, ll p){
	if (l * c >= p) return 0;
	int ans = 0;

	ll L = l, P = p;
	while (L < P){
		L *= c;
		P = (P - 1) / c + 1;
	}
	
	ans = 1 + go(l, L);
	return ans;
}

vector <ll> q, w; 

int main()
{
    freopen("input.txt","rt", stdin);
    freopen("output.txt", "wt", stdout);    
	
	int tk;
	cin >> tk;
	forn(ii, tk){
		int ans = 0;
		cin >> l >> p >> c;

		ans = go(l, p);

		printf("Case #%d: %d\n", ii + 1, ans);
	}
    return 0;
}

