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
const long long mod = 10007;

int dx[2] = {1, 2};
int dy[2] = {2, 1};

int m, n;
int K;

bool a[100][100];
long long f[100][100];


void init()
{

    memset(a, 0, sizeof(a));
    scanf("%d%d%d", &m, &n, &K);
    while (K--) {
	int x, y;
	scanf("%d%d", &x, &y);
	--x, --y;
	a[x][y] = true;
    }
}

void run()
{
    memset(f, 0, sizeof(f));
    f[0][0] = 1;
    for (int i = 0; i < m; ++i) {
	for (int j = 0; j < n; ++j) {
	    if (a[i][j])
		continue;
	    for (int k = 0; k < 2; ++k) {
		int x = i - dx[k];
		int y = j - dy[k];
		if (x >= 0 && y >= 0) {
		    f[i][j] = (f[i][j] + f[x][y]) % mod;
		}
	    }
	}
    }
    printf("%lld\n", f[m - 1][n - 1]);
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


