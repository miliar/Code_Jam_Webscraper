#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
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

using namespace std;

#define sz(a) int((a).size()) 
#define pb push_back 
#define present(c,x) ((c).find(x) != (c).end()) 
#define sqr(x) ((x) * (x))
#define pow2(x) (1 << (x))

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;

const int inf = 1000000000;
const double eps = 1e-9;

int n, m;
vi bx, by;
vi nx, ny;

void init()
{
    bx.clear();
    by.clear();
    nx.clear();
    ny.clear();
    scanf("%d", &n);
    char s[100];
    for (int i = 0; i < n; ++i) {
	int a, b;
	scanf("%d%d%s", &a, &b, s);
	if (s[0]== 'B') {
	    bx.pb(a);
	    by.pb(b);
	}
	else {
	    scanf("%s", s);
	    nx.pb(a);
	    ny.pb(b);
	}
    }
}

void run()
{
    if (bx.empty()) {
	scanf("%d", &m);
	for (int i = 0; i < m; ++i) {
	    int x, y;
	    scanf("%d%d", &x, &y);
	    bool mark = false;
	    for (int j = 0; j < sz(nx); ++j) {
		if (nx[j] == x && ny[j] == y) {
		    mark = true;
		    break;
		}
	    }
	    if (mark) {
		printf("NOT BIRD\n");
	    }
	    else {
		printf("UNKNOWN\n");
	    }
	}
    }
    else {
	int xmin = inf, xmax = -inf, ymin = inf, ymax = -inf;
	for (int i = 0; i < sz(bx); ++i) {
	    xmin = min(xmin, bx[i]);
	    xmax = max(xmax, bx[i]);
	    ymin = min(ymin, by[i]);
	    ymax = max(ymax, by[i]);
	}
	int left = -inf, right = inf, up = inf, down = -inf;
	for (int i = 0; i < sz(nx); ++i) {
	    if (nx[i] >= xmax && ny[i] >= ymin && ny[i] <= ymax) {
		right = min(right, nx[i]);
	    }
	    else if (nx[i] <= xmin && ny[i] >= ymin && ny[i] <= ymax) {
		left = max(left, nx[i]);
	    }
	    if (ny[i] >= ymax && nx[i] >= xmin && nx[i] <= xmax) {
		up = min(up, ny[i]);
	    }
	    else if (ny[i] <= ymin && nx[i] >= xmin && nx[i] <= xmax) {
		down = max(down, ny[i]);
	    }
	}

	scanf("%d", &m);
	for (int i = 0; i < m; ++i) {
	    int x, y;
	    scanf("%d%d", &x, &y);
	    if (x >= xmin && x <= xmax && y >= ymin && y <= ymax) {
		printf("BIRD\n");
	    }
	    else if (x >= right || x <= left || y >= up || y <= down) {
		printf("NOT BIRD\n");
	    }
	    else {
		bool mark = false;
		for (int i = 0; i < sz(nx); ++i) {
		    if (nx[i] > xmax && ny[i] > ymax) {
			if (x >= nx[i] && y >= ny[i]) {
			    mark = true;
			    break;
			}
		    }
		    if (nx[i] < xmin && ny[i] < ymin) {
			if (x <= nx[i] && y <= ny[i]) {
			    mark = true;
			    break;
			}
		    }
		    if (nx[i] > xmax && ny[i] < ymin) {
			if (x >= nx[i] && y <= ny[i]) {
			    mark = true;
			    break;
			}
		    }
		    if (nx[i] < xmin && ny[i] > ymax) {
			if (x <= nx[i] && y >= ny[i]) {
			    mark = true;
			    break;
			}
		    }
		}
		if (mark) {
		    printf("NOT BIRD\n");
		}
		else {
		    printf("UNKNOWN\n");
		}
	    }
	}
    }
}

int main(void)
{
    int c;
    scanf("%d", &c);
    for (int i = 1; i <= c; ++i) {
	printf("Case #%d:\n", i);
	init();
	run();
    }
    return 0;
}


