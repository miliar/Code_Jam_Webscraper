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

const int maxn = 10010;

int a[maxn];
int c[maxn];
int f[maxn][2];
int n, v, n1, n2;

void init()
{
    scanf("%d%d", &n, &v);
    n1 = (n - 1) / 2;
    n2 = (n + 1) / 2;
    for (int i = 1; i <= n1; ++i) {
	scanf("%d%d", &a[i], &c[i]);
    }
    for (int i = n1 + 1; i <= n; ++i) {
	scanf("%d", &a[i]);
    }
}

void get(int i, int c, int w)
{
    int x = i * 2;
    int y = i * 2 + 1;
    if (c == 0) {
	if (f[x][0] < inf && f[y][0] < inf) {
	    f[i][0] = min(f[i][0], f[x][0] + f[y][0] + w);
	}
	if (f[x][0] < inf && f[y][1] < inf) {
	    f[i][1] = min(f[i][1], f[x][0] + f[y][1] + w);
	}
	if (f[x][1] < inf && f[y][0] < inf) {
	    f[i][1] = min(f[i][1], f[x][1] + f[y][0] + w);
	}
	if (f[x][1] < inf && f[y][1] < inf) {
	    f[i][1] = min(f[i][1], f[x][1] + f[y][1] + w);
	}
    }
    else {
	if (f[x][1] < inf && f[y][1] < inf) {
	    f[i][1] = min(f[i][1], f[x][1] + f[y][1] + w);
	}
	if (f[x][0] < inf && f[y][1] < inf) {
	    f[i][0] = min(f[i][0], f[x][0] + f[y][1] + w);
	}
	if (f[x][1] < inf && f[y][0] < inf) { 
	    f[i][0] = min(f[i][0], f[x][1] + f[y][0] + w);
	}
	if (f[x][0] < inf && f[y][0] < inf) {
	    f[i][0] = min(f[i][0], f[x][0] + f[y][0] + w);
	}
    }
}



void run()
{

    memset(f, 0x7f, sizeof(f));
    for (int i = n1 + 1; i <= n; ++i) {
	if (a[i]) {
	    f[i][1] = 0;
	}
	else {
	    f[i][0] = 0;
	}
    }

    for (int i = n1; i > 0; --i) {
	get(i, a[i], 0);
	if (c[i]) {
	    get(i, (a[i] + 1) % 2, 1);
	}
    }

    if (f[1][v] < inf) {
	printf("%d\n", f[1][v]);
    }
    else {
	printf("IMPOSSIBLE\n");
    }
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

