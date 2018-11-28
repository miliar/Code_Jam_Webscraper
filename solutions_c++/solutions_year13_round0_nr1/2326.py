#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cassert>
#include <ctime>


using namespace std;

#ifdef WIN32
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

typedef pair<int, int> pii;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<ll> vll;
typedef vector<vll> vvll;

ll rdtsc() {
    ll tmp;
    asm("rdtsc" : "=A"(tmp));
    return tmp;
}

#define TASKNAME "text"
#define pb push_back
#define mp make_pair
#define EPS (1e-9)
#define INF ((int)1e9)
#define sqr(x) ((x) * (x))         
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define sz(x) ((int)(x).size())

char resTypes[4][100] = {"X won", "O won", "Draw", "Game has not completed"};

char s[4][5];

void solve(int &testCase) {
	int res = 2;
	for (int i = 0; i < 4; i++) {
		scanf("%s", s[i]);
		if (find(s[i], s[i] + 4, '.') - s[i] != 4)
			res = 3;
	}
	for (int iter = 0; iter < 2; iter++) {
		char chs[3] = {!iter ? 'X' : 'O', 'T'};
		int ok = 0;
		for (int i = 0; i < 4; i++) {
			++ok;
			for (int j = 0; j < 4; j++)
				if (s[i][j] != chs[0] && s[i][j] != chs[1]) {
					--ok;
					break;
				}
			++ok;
			for (int j = 0; j < 4; j++)
				if (s[j][i] != chs[0] && s[j][i] != chs[1]) {
					--ok;
					break;
				}
		}
		++ok;
		for (int j = 0; j < 4; j++)
			if (s[j][j] != chs[0] && s[j][j] != chs[1]) {
				--ok;
				break;
			}
		++ok;
		for (int j = 0; j < 4; j++)
			if (s[j][3 - j] != chs[0] && s[j][3 - j] != chs[1]) {
				--ok;
				break;
			}	
		if (ok)
			res = iter;
	}
		
	printf("Case #%d: %s\n", ++testCase, resTypes[res]);
}

int main() {
	srand(rdtsc());
#ifdef DEBUG
	freopen(TASKNAME".in", "r", stdin);
	freopen(TASKNAME".out", "w", stdout);
#endif
	
	int testCase = 0;
	int n;
	while (scanf("%d", &n) >= 1) {
		for (int i = 0; i < n; i++)
			solve(testCase);
		//break;
	}
	return 0;
}
