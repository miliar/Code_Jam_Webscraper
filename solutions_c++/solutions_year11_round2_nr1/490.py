#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <sstream>
#include <cassert>
#include <functional>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <ctime>
#include <deque>

using namespace std;

void prepare() {
	freopen("input.txt", "r", stdin);
#ifndef _DEBUG
	freopen("output.txt", "w", stdout);
#endif
}

#define fo(a,b,c) for( a = (b); a < (c); ++ a )
#define fr(a,b) fo(a,0,(b))
#define fi(n) fr(i,(n))
#define fj(n) fr(j,(n))
#define fk(n) fr(k,(n))
#define mp make_pair
#define pb push_back
#define all(a) (a).begin( ), (a).end( )
#define _(a, b) memset( (a), (b), sizeof( a ) )
#define __(a) memset( (a), 0, sizeof( a ) )
#define sz(a) (int)(a).size( )

typedef long long lint;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair <int, int> PII;

const int INF = 2000000000;
const int MAXN = 105;

int n, m;
char a[MAXN][MAXN];
int winc[MAXN];
int cnt[MAXN];
double wp[MAXN];
double owp[MAXN];
double oowp[MAXN];
double wpp[MAXN][MAXN];

void solve() {
	int i, j, k;
	scanf("%d", &n);
	for (i = 0; i < n; ++ i) {
		scanf("%s", a[i]);
	}
	for (i = 0; i < n; ++ i) {
		cnt[i] = 0;
		winc[i] = 0;
		for (j = 0; j < n; ++ j) {
			if (a[i][j] == '1' || a[i][j] == '0') {
				++ cnt[i];
				if (a[i][j] == '1') {
					++ winc[i];
				}
			}
		}
		wp[i] = (double)winc[i] / cnt[i];
	}
	for (i = 0; i < n; ++ i) {
		double sum = 0;
		int cnn = 0;
		for (j = 0; j < n; ++ j) {
			if (j != i && a[i][j] != '.') {
				int cn = 0;
				int wn = 0;
				for (k = 0; k < n; ++ k) {
					if (k != j && k != i) {
						if (a[j][k] != '.') {
							++ cn;
							if (a[j][k] == '1') {
								++ wn;
							}
						}
					}
				}
				sum += (double)wn / cn;
				++ cnn;
			}
		}
		owp[i] = sum / cnn;
	}
	for (i = 0; i < n; ++ i) {
		double sum = 0;
		int cnn = 0;
		for (j = 0; j < n; ++ j) {
			if (i != j && a[i][j] != '.') {
				sum += owp[j]; 
				++ cnn;
			}
		}
		oowp[i] = sum / cnn;
	}
	for (i = 0; i < n; ++ i) {
		printf("%.12lf\n", wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25);
	}
}

int main() {
	prepare();
	int tn;
	cin >> tn;
	int t = 0;
	while (t++ < tn) {
		printf("Case #%d:\n", t);
		solve();
	}
	return 0;
}