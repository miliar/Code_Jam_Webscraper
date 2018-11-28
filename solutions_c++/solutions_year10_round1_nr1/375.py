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

const int NMAX = 55;

bool ar, ab;
int n, k;
char a[NMAX][NMAX], b[NMAX][NMAX];

inline void readData(){
	scanf("%d%d\n", &n, &k);
	forn(i, n)
		gets(a[i]);
}

inline void writeData(){
	if (!ar && !ab) printf("Neither\n");
	else if (ar && ab) printf("Both\n");
	else if (ar) printf("Red\n");
	else if (ab) printf("Blue\n");
}

inline void init(){
	memset(a, 0, sizeof a);
	memset(b, 0, sizeof b);
	ar = ab = false;
}

inline bool good(int x, int y, int dx, int dy, char c){
	int ans = 0;
	while (ans < k && b[x][y] == c && x < n && y < n){
		x += dx; y += dy; ans++;
	}

	return ans == k;
}

inline void solve(){
	init();
	readData();

	forn(i, n)
		forn(j, n)
			b[j][n - i - 1] = a[i][j];

	forn(j, n){
		string s;
		ford(i, n)
			if (b[i][j] != '.'){
				s += b[i][j];
				b[i][j] = '.';
			}

		int pos = 0;
		ford(i, n){
			if (pos == (int) s.size()) break;
			b[i][j] = s[pos++];
		}
	}

	swap(n, n);
	swap(n, n);

	forn(i, n)
		forn(j, n)
			if (b[i][j] != '.' && (good(i, j, 0, 1, b[i][j]) || good(i, j, 1, 1, b[i][j]) || good(i, j, 1, 0, b[i][j])))
				if (b[i][j] == 'R') ar = true;
				else ab = true;

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