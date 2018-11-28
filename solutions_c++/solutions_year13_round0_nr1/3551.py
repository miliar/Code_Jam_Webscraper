#include <iostream>
#include <cstdio>
#include <fstream>

#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <string>
#include <cstring>

#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cassert>
#include <memory.h>
using namespace std;

#define fr(i, n) for (int i = 0; i < (int)(n); i++)
#define fb(i, n) for (int i = n - 1; i >= 0; i--)
#define all(a) (a).begin(), (a).end()
#define _(a, b) memset(a, b, sizeof(a))
#define mp make_pair
#define pb push_back
#define sz(v) ((int)(v).size())

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

inline int ni() { int a; scanf("%d", &a); return a; }
inline double nf() { double a; scanf("%lf", &a); return a; }
template <class T> void out(T a, T b) { bool first = true; for (T i = a; i != b; i++) { if (!first) printf(" "); first = false; cout << *i; } puts(""); }
template <class T> void outl(T a, T b) { for (T i = a; i != b; i++) cout << *i << "\n"; } 

const int N = 4;

int T;
char s[N][N];

bool win(char c) {
	bool has_won = false;
	fr(i, N) {
		has_won = true;
		fr(j, N)
			if (s[i][j] != c && s[i][j] != 'T') {
				has_won = false;
				break;
			}
		if (has_won)
			return true;

		has_won = true;
		fr(j, N)
			if (s[j][i] != c && s[j][i] != 'T') {
				has_won = false;
				break;
			}
		if (has_won)
			return true;
	}
	has_won = true;
	fr(i, N)
		if (s[i][i] != c && s[i][i] != 'T') {
			has_won = false;
			break;
		}			
	if (has_won)
		return true;

	has_won = true;
	fr(i, N)
		if (s[i][N - i - 1] != c && s[i][N - i - 1] != 'T') {
			has_won = false;
			break;
		}			
	if (has_won)
		return true;
	return false;
}

const char *solve() {
	fr(i, N)
		cin >> s[i];
	
	bool is_full = true;
	fr(i, N)
		fr(j, N)
			if (s[i][j] == '.')
				is_full = false;
	if (win('X'))
		return "X won";
	if (win('O'))
		return "O won";
	return (is_full ? "Draw" : "Game has not completed");
}       	

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> T;
	fr(test, T) {
		printf("Case #%d: %s\n", test + 1, solve());
	}		  
}
        