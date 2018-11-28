#define _USE_MATH_DEFINES 
#define _CRT_SECURE_NO_DEPRECATE 
 
#include <algorithm> 
#include <bitset> 
#include <cassert> 
#include <climits> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <deque> 
#include <functional> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <string> 
#include <vector> 
 
using namespace std; 
 
#pragma comment(linker, "/STACK:64000000") 
 
template<class T> inline T sqr (T x) {return x * x;} 
 
typedef long long int64; 
typedef unsigned long long uint64; 
typedef pair<int, int> pii; 
typedef pair<int, pii> pip; 
typedef pair<pii, int> ppi; 
typedef pair<int64, int64> pii64; 
typedef pair<double, double> pdd; 
typedef pair<string, int> psi; 
typedef pair<int, string> pis; 
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
#define FAIL ++*(int*)0 
#define eps  1e-9 
#define inf  0x7f7f7f7f 
#define MP make_pair 
#define sz(C) (int)((C).size()) 
#define all(C) (C).begin(), (C).end() 
#define TASK "test" 
#define RR 151 

int dx[] = {0, 1, 1};
int dy[] = {1, 1, 0};

int n, m;
string a[1 << 6];

inline bool ok (int x, int y) {
	return x >= 0 && y >= 0 && x < n && y < m;
}

void solve () {
	cin >> n >> m;
	for (int i = 0; i < n; ++i)
		cin >> a[i];
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (a[i][j] != '#') continue;
			bool good = true;
			for (int k = 0; k < 3; ++k) {
				int tx = i + dx[k];
				int ty = j + dy[k];
				if (!ok(tx, ty) || a[tx][ty] == '.') {
					good = false;
					break;
				}
			}
			if (!good) {
				puts("Impossible");
				return;
			}
			a[i][j] = '/'; a[i][j + 1] = '\\';
			a[i + 1][j] = '\\'; a[i + 1][j + 1] = '/';
		}
	}
	for (int i = 0; i < n; ++i)
		cout << a[i] << endl;
}

int main() { 
    //freopen("input.txt", "r", stdin);  freopen("output.txt", "w", stdout);
	//freopen("A-small-attempt0.in", "r", stdin);  freopen("A-small-attempt0.out", "w", stdout);
	freopen("A-large.in", "r", stdin);  freopen("A-large.out", "w", stdout);

	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
		printf("Case #%d:\n", test);
		solve();
	}

    return 0; 
}