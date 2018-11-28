#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>

#include <iostream>
#include <algorithm>
#include <memory>
#include <string>
#include <vector>
#include <map>
#include <iostream>

#define TASK "a"
#define PB(x) push_back(x)
#define MP(x, y) make_pair(x, y)
#define CLR(x) memset(x, 0, sizeof(x))
#define forn(i, n) for (int i = 0; i < n; i++)

using namespace std;

typedef long long int64;
typedef long double ldouble;
typedef pair<int, int> pii;
typedef vector<int> vi;

const int INF = 0x3f3f3f3f;
const int64 INF64 = (int64)INF * (int64)INF;

const int MAXN = 200;

int k;                
int a[MAXN][MAXN];
bool was[MAXN][MAXN];

int num(int k, int i) {
	return (i <= k) ? i : (2*k - i);
}

bool is_was(int k) {
	for (int i = 1; i <= 2 * k - 1; i++)	
		for (int j = 1; j <= num(k, i); j++)
			if (!was[i][j]) return false;
	return true;
}

pair<int, int> hor(int k, int i, int j) {
	return MP(i, num(k, i) + 1 - j);
}

pair<int, int> ver(int k, int i, int j) {
	return MP(2 * k - i, j);
}

pair<int, int> change(int s, int di, int dj, int k, int i, int j) {
	int ri = i - di;
	int rj = j - dj - ((i - di <= k) ? 0 : i - di - k) + ((i <= s) ? 0 : i - s);
	return MP(ri, rj);
}

bool contain(int s, int di, int dj, int k, int i, int j) {
	pair<int, int> r = change(s, di, dj, k, i, j);
	return (r.first >= 1) && (r.first <= 2 * k - 1) && (r.second >= 1 && r.second <= num(k, r.first));
}

int check(int s, int di, int dj) {
	memset(was, 0, sizeof(was));

	for (int i = 1; i <= 2 * s - 1; i++) {
		for (int j = 1; j <= num(s, i); j++) {
///			printf("%d %d\n", i, j);
			if (contain(s, di, dj, k, i, j)) {
				
				pair<int, int> r = change(s, di, dj, k, i, j);
				was[r.first][r.second] = true;
//				printf("In our : %d %d [%d]\n", r.first, r.second, a[r.first][r.second]);

				pair<int, int> h = hor(s, i, j);
				pair<int, int> v = ver(s, i, j);

//				printf("hot : %d %d (%d)\n", h.first, h.second, contain(s, di, dj, k, h.first, h.second));
//				printf("ver : %d %d (%d)\n", v.first, v.second, contain(s, di, dj, k, v.first, v.second));

				pair<int, int> rh = change(s, di, dj, k, h.first, h.second);
				pair<int, int> rv = change(s, di, dj, k, v.first, v.second);

				if (contain(s, di, dj, k, h.first, h.second) && 
					a[r.first][r.second] != a[rh.first][rh.second])
						return INF;

				if (contain(s, di, dj, k, v.first, v.second) && 
					a[r.first][r.second] != a[rv.first][rv.second])
						return INF;
			}
		}
	}
	if (!is_was(k)) return INF;
	return s * s - k * k;
}

int main() {
    freopen(TASK ".in", "rt", stdin);
	freopen(TASK ".out", "wt", stdout);

    int T;
    scanf("%d", &T);
    forn(t, T) {
    	scanf("%d", &k);
    	for (int i = 1; i <= 2*k - 1; i++) {
    		for (int j = 1; j <= num(k, i); j++)
    			scanf("%d", &a[i][j]);
    	}

    	int answer = INF;
		for (int s = k;; s++) {
			if (answer < INF) break;
			for (int di = 0; di <= 2 * s - 1; di++) {
				for (int dj = 0; dj <= num(s, di + 1); dj++) {
					answer = min(answer, check(s, di, dj));
				}
			}
		}

    	printf("Case #%d: %d\n", t + 1, answer);
    }

    return 0;
}
