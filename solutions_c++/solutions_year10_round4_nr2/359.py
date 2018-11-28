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

int n, need[6010], p;
int64 d[6010][12], cost[6100];

int64 get(int v, int have, int h){
	int64 &ans = d[v][have];
	if (ans != -1) return ans;

	if (h == p)
		if (have >= need[v]) return 0;
		else return INF64;

	ans = INF64;
	ans = min(ans, get(2*v + 1, have + 1, h + 1) + get(2*v + 2, have + 1, h + 1) + cost[v]);
	ans = min(ans, get(2*v + 1, have, h + 1) + get(2*v + 2, have, h + 1));

	return ans;
}

inline void readData(){
	scanf("%d", &p);
	n = (1 << p);
	forn(i, n){
		scanf("%d", &need[n + i - 1]);
		need[n + i - 1] = p - need[n + i - 1];
	}

	ford(stage, p)
		for(int i = (1 << stage) - 1; i < 2*(1 << stage) - 1; i++)
			scanf("%I64d", &cost[i]);

}

inline void writeData(){
	printf("%I64d\n", get(0, 0, 0));
}

inline void init(){
	memset(d, 255, sizeof d);
	memset(cost, 0, sizeof cost);
	memset(need, 0, sizeof need);
}

inline void solve(){
	init();
	readData();
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