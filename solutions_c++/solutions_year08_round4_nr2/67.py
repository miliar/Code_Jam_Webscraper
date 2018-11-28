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


int n, m, s;

void init()
{
    scanf("%d%d%d", &m, &n, &s);
}

inline int cross(int x1, int y1, int x2, int y2)
{
    return x1 * y2 - x2 * y1;
}

inline int area(int x1, int y1, int x2, int y2)
{
    return abs(cross(x1, y1, x2, y2));
}

void run()
{
    for (int x1 = 0; x1 <= m; ++x1) {
	for (int y1 = 0; y1 <= n; ++y1) {
	    for (int x2 = 0; x2 <= m; ++x2) {
		for (int y2 = 0; y2 <= n; ++y2) {
		    if (area(x1, y1, x2, y2) == s) {
			printf("0 0 %d %d %d %d\n", x1, y1, x2, y2);
			return;
		    }
		}
	    }
	}
    }
    printf("IMPOSSIBLE\n");
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

