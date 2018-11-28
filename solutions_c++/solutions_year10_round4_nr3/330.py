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

const int SIZE = 110;

int ans = 0, maxX, maxY;
bool f[SIZE][SIZE], f1[SIZE][SIZE];

inline void fill(int x1, int y1, int x2, int y2){
	maxX = max(maxX, max(x1, x2) + 1);
	maxY = max(maxY, max(y1, y2) + 1);
	for(int x = min(x1, x2); x <= max(x1, x2); x++)
		for(int y = min(y1, y2); y <= max(y1, y2); y++)
			f[x][y] = true;
}

inline void readData(){
	int k;
	scanf("%d", &k);
	forn(i, k){
		int x1, y1, x2, y2;
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
		fill(x1, y1, x2, y2);
	}
}

inline bool get(int x, int y){
	if (x < 0 || y < 0) return false;
	return f[x][y];
}

inline void writeData(){
	printf("%d\n", ans);
}

inline void init(){
	ans = 0;
	maxX = maxY = -1;
	memset(f1, 0, sizeof f1);
	memset(f, 0, sizeof f);
}

inline void solve(){
	init();
	readData();

	while (true){
		int cnt = 0;
		forn(i, maxX)
			forn(j, maxY){
				f1[i][j] = f[i][j];
				if (f[i][j]) cnt++;
			}

		if (cnt == 0) break;
		forn(x, maxX)
			forn(y, maxY){
				if (f[x][y] && !get(x - 1, y) && !get(x, y - 1)) f1[x][y] = false;
				if (!f[x][y] && get(x - 1, y) && get(x, y - 1)) f1[x][y] = true;
			}				

		ans++;
		cnt = 0;
		forn(i, maxX)
			forn(j, maxY){
				f[i][j] = f1[i][j];
				if (f[i][j]) cnt++;
			}

		if (cnt == 0) break;
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