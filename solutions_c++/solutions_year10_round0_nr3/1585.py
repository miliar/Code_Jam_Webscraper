#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <numeric>
#include <utility>

#include <deque>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <queue>
#include <list>

#include <sstream>
#include <iostream>
#include <iomanip>

using namespace std;

typedef long long int64;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) a.size() - 1
#define all(a) a.begin(), a.end()
#define I (int)
#define I64 (int64)
#define LD (long double)
#define VI vector<int>

#define write_1d_array(message, a, n) { cout << endl << message << endl; forn(i, n) cout << a[i] << " "; cout << "\n\n";}
#define write_2d_array(message, a, n, m) { cout << endl << message << endl; forn(i, n){forn(j, m) cout << a[i][j] << " "; cout << endl; } cout << "\n\n";}

const long double EPS = 1E-9;
const int INF = (int)1E9;
const int64 INF64 = (int64)1E18;
const long double PI = 3.1415926535897932384626433832795;

const int NMAX = 1100;

int r, k, n, g[NMAX], num[NMAX];
int next[NMAX], w[NMAX];
int64 ans, s[NMAX];
bool used[NMAX];

inline void readData(){
	scanf("%d%d%d", &r, &k, &n);
	forn(i, n) scanf("%d", &g[i]);
}

inline void writeData(){
	printf("%I64d\n", ans);	
}

inline void init(){
	memset(used, 0, sizeof used);
	ans = 0;
}

inline void solve(){
	init();
	readData();

	forn(i, n)
		for(int v = i, sum = 0; ; v = (v + 1) % n)
			if ((v == i && sum != 0) || sum + g[v] > k){
				w[i] = sum;
				next[i] = v;
				break;
			}
			else
				sum += g[v];

	int64 sum = 0;
	int v = 0, nn = 0;
	while (r > 0){
		if (used[v]){
			int64 t = sum - s[v];
			int p = nn - num[v];
			ans += t*(r/p);
			r %= p;
			memset(used, 0, sizeof used);
		}
		else {
			ans += w[v];
			r--;
			num[v] = nn;
			s[v] = sum;
			nn++;
			sum += w[v];
			used[v] = true;
			v = next[v];
		}
	}

	writeData();
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tests;
	scanf("%d", &tests);
	forn(test, tests){
		printf("Case #%d: ", test + 1);
		solve();
	}
	
	return 0;
}