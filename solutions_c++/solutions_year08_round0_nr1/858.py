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


int f[1010][110];
int m, n;

string se[101];
string q[1100];

void init()
{
    cin >> m;
    char ch = cin.get();
    while (ch != '\n')
	ch = cin.get();
    for (int i = 0; i < m; ++i) {
	getline(cin, se[i]);
    }
    cin >> n;
    ch = cin.get();
    while (ch != '\n')
	ch = cin.get();
    for (int i = 0; i < n; ++i) {
	getline(cin, q[i]);
    }
}

void run()
{
    if (n == 0) {
	printf("0\n");
	return;
    }
    memset(f, 0x7f, sizeof(f));
    for (int i = 0; i < m; ++i) {
	if (se[i] != q[0]) {
	    f[0][i] = 0;
	}
    }
    for (int i = 1; i < n; ++i) {
	for (int j = 0; j < m; ++j) {
	    if (f[i - 1][j] < inf) {
		for (int k = 0; k < m; ++k) {
		    int w = f[i - 1][j];
		    if (j != k)
			++w;
		    if (se[k] != q[i] && w < f[i][k]) {
			f[i][k] = w;
		    }
		}
	    }
	}
    }
    int res = inf;
    for (int i = 0; i < m; ++i) {
	if (f[n - 1][i] < inf) {
	    res = min(res, f[n - 1][i]);
	}
    }
    printf("%d\n", res);
}

int main(void)
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
	printf("Case #%d: ", i);
	init();
	run();
    }
    return 0;
}
