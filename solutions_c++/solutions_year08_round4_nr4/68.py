#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <string>
#include <cstring>
#include <cassert>

using namespace std;

#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define present(c,x) ((c).find(x) != (c).end()) 
#define sqr(x) ((x) * (x))
#define dist(x1, y1, x2, y2) (sqrt(sqr((x1) - (x2)) + sqr((y1) - (y2))))
#define pow2(x) (1 << (x))

const int dir[8][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;

const int inf = 0x7f7f7f7f;
const double eps = 1e-9;


const int maxn = 50010;
char s[maxn];
int f[pow2(16)][16];
int w[16][16];
int n, m, c;

void init()
{
    scanf("%d", &m);
    scanf("%s", s);
    n = strlen(s);
    for (int i = 0; i < m; ++i) {
	for (int j = i + 1; j < m; ++j) {
	    w[i][j] = 0;
	    for (int k = 0; k < n; k += m) {
		if (s[k + i] != s[k + j]) {
		    ++w[i][j];
		}
	    }
	    w[j][i] = w[i][j];
	}
    }
}

void run()
{
    int res = inf;
    for (int start = 0; start < m; ++start) {
	memset(f, 0x7f, sizeof(f));
	f[pow2(start)][start] = n / m;
	for (int mask = 0; mask < pow2(m); ++mask) {
	    for (int i = 0; i < m; ++i) {
		if ((mask & pow2(i)) && f[mask][i] < inf) {
		    for (int j = 0; j < m; ++j) {
			if (!(mask & pow2(j))) {
			    f[mask | pow2(j)][j] = min(f[mask | pow2(j)][j], f[mask][i] + w[i][j]);
			}
		    }
		}
	    }
	}
	for (int i = 0; i < m; ++i) {
	    if (i != start) {
		int minus = 0;
		for (int x = 0; x < n - m; x += m) {
		    if (s[x + i] == s[x + m + start])
			++minus;
		}
		res = min(res, f[pow2(m) - 1][i] - minus);
	    }
	}
    }
    printf("%d\n", res);
}

int main(void)
{
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
	printf("Case #%d: ", i);
	init();
	run();
    }
    return 0;
}

