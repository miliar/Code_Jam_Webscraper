#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:64000000")

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

#define write_1d_array(message, a, n) { cout << endl << message << endl; forn(i, n) cout << a[i] << " "; cout << "\n\n";}
#define write_2d_array(message, a, n, m) { cout << endl << message << endl; forn(i, n){forn(j, m) cout << a[i][j] << " "; cout << endl; } cout << "\n\n";}

const long double EPS = 1E-9;
const int INF = (int)1E9;
const int64 INF64 = (int64)1E18;
const long double PI = 3.1415926535897932384626433832795;

const int NMAX = 110;

int n, M, D, I, a[NMAX], ans;
int d[NMAX][300], used[NMAX][300];
int dt[300][300];

inline int up(int x, int y){
	int ans = x / y;
	if (x % y != 0) ans++;
	return ans;
}

inline int getNum(int x, int y){
	if (y == 256) return 0;
	if (M == 0 && x != y) return 300100;
	if (x > y) swap(x, y);

	if (x >= y - M) return 0;
	if (dt[x][y] != -1) return dt[x][y];

	return dt[x][y] = I + getNum(x + M, y);
}

int DP(int v, int x){
	if (v == n) return 0;
	
	int &ans = d[v][x];
	if (used[v][x] != -1) return ans;
	used[v][x] = 0;
	ans = DP(v + 1, x) + D;
	forn(i, 256){
		int t = DP(v + 1, i) + getNum(i, x) + abs(a[v] - i);
		ans = min(ans, t);
	}

	return ans;
}

inline void readData(){
	cin >> D >> I >> M >> n;
	forn(i, n)
		cin >> a[i];
}

inline void writeData(){
	printf("%d\n", ans);
}

inline void init(){
	memset(used, 255, sizeof used);
	memset(dt, 255, sizeof dt);
}

inline void solve(){
	init();
	readData();

	ans = DP(0, 256);

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