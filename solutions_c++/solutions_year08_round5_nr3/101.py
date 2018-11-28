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

int m, n;
char a[100][100];
int num[100][100];
int n1, n2;
bool co[80 * 41][80 * 41];
bool cover[80 * 41];
int match[80 * 41];

void init()
{
    scanf("%d%d", &m, &n);

    for (int i = 0; i < m; ++i) {
	scanf("%s", a[i]);
    }

    n1 = n2 = 0;
    memset(num, 0, sizeof(num));

    for (int i = 0; i < m; ++i) {
	for (int j = 0; j < n; ++j) {
	    if (a[i][j] == '.') {
		if (j % 2 == 0) {
		    num[i][j] = n1++;
		}
		else {
		    num[i][j] = n2++;
		}
	    }
	}
    }

    memset(co, 0, sizeof(co));

    for (int i = 0; i < m; ++i) {
	for (int j = 0; j < n; ++j) {
	    if (a[i][j] == '.') {
		if (i > 0 && j > 0 && a[i - 1][j - 1] == '.') {
		    if (j % 2 == 0) {
			co[num[i][j]][num[i - 1][j - 1]] = true;
		    }
		    else {
			co[num[i - 1][j - 1]][num[i][j]] = true;
		    }
		}
		if (i > 0 && j + 1 < n && a[i - 1][j + 1] == '.') {
		    if (j % 2 == 0) {
			co[num[i][j]][num[i - 1][j + 1]] = true;
		    }
		    else {
			co[num[i - 1][j + 1]][num[i][j]] = true;
		    }
		}
		if (j > 0 && a[i][j - 1] == '.') {
		    if (j % 2 == 0) {
			co[num[i][j]][num[i][j - 1]] = true;
		    }
		    else {
			co[num[i][j - 1]][num[i][j]] = true;
		    }
		}
		if (j + 1 < n && a[i][j + 1] == '.') {
		    if (j % 2 == 0) {
			co[num[i][j]][num[i][j + 1]] = true;
		    }
		    else {
			co[num[i][j + 1]][num[i][j]] = true;
		    }
		}
	    }
	}
    }
}

bool go(int x)
{
    int k;
    for (int i = 0; i < n2; ++i) {
	if (co[x][i] && !cover[i]) {
	    cover[i] = true;
	    k = match[i];
	    match[i] = x;
	    if (k < 0 || go(k))
		return true;
	    match[i] = k;
	}
    }
    return false;
}

void run()
{
    memset(match, -1, sizeof(match));
    int tot = 0;
    for (int i = 0; i < n1; ++i) {
	memset(cover, 0, sizeof(cover));
	if (go(i)) {
	    ++tot;
	}
    }
    printf("%d\n", n1 + n2 - tot);
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

