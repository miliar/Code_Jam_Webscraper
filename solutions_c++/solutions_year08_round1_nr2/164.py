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

int n, m;

int one[3000];
int a[3000];
int num[3000];
bool zero[3000][3000];

void init()
{
    scanf("%d%d", &n, &m);
    int t, x, y;
    memset(one, -1, sizeof(one));
    memset(zero, 0, sizeof(zero));
    memset(num, 0, sizeof(num));
    for (int i = 0; i < m; ++i) {
	scanf("%d", &t);
	while (t--) {
	    scanf("%d%d", &x, &y);
	    --x;
	    if (y) {
		one[i] = x;
	    }
	    else {
		zero[i][x] = true;
		++num[i];
	    }
	}
    }
    for (int i = 0; i < m; ++i) {
	int tot = 0;
	for (int j = 0; j < n; ++j) {
	    tot += zero[i][j];
	}
	assert(tot == num[i]);
    }
}

bool run()
{
    memset(a, 0, sizeof(a));
    while (1) {
	bool ok = true;
	for (int i = 0; i < m; ++i) {
	    //assert(num[i] >= 0);
	    if (num[i] == 0) {
		ok = false;
		if (one[i] >= 0) {
		    a[one[i]] = 1;
		    num[i] = 1;
		    for (int j = 0; j < m; ++j) {
			if (zero[j][one[i]])
			    --num[j];
			else if (one[j] == one[i]) {
			    ++num[j];
			}
		    }
		}
		else {
		    return false;
		}
	    }
	}
	if (ok)
	    break;
    }
    for (int i = 0; i < n; ++i) {
	printf(" %d", a[i]);
    }
    putchar('\n');
    return true;
}

int main(void)
{
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
	printf("Case #%d:", i);
	init();
	if (!run()) {
	    printf(" IMPOSSIBLE\n");
	}
    }
    return 0;
}
