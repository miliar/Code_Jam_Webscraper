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
const int MAXN = 60;
const int INF = (int)(1e9 + 1e-9);

int t[2];
char tmp[MAXN * 20];
string s;
int a[MAXN][MAXN];
bool b[MAXN][MAXN];
int q[MAXN * 20];
int h = 0;
int last[MAXN];

void up(int &a, int b){
	a = min(a, b);
}

int M(char c){
	return c - 'A' + 1;
}

int main()
{
    freopen("input.txt","rt", stdin);
    freopen("c.out", "wt", stdout);    
	
	int tk;
	cin >> tk;

	forn(ii, tk){

		int sum = 0, mx = (int)(1e9 + 1e-9);

		int n, rs = 0;
		cin >> n;
		forn(i, n){
			int x;
			cin >> x;
			rs ^= x;
			mx = min(mx, x);
			sum += x;
		}

		sum -= mx;

		if (sum == 0 || rs != 0){
			printf("Case #%d: NO\n", ii + 1);
		}
		else
			printf("Case #%d: %d\n", ii + 1, sum);

	}

	return 0;
}

