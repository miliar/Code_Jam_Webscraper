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


const int maxn = 110;

int tt;
struct node {
    int a, b;
    int type;
};

vector<node> lst;

inline bool operator<(const node &a, const node &b)
{
    return (a.a < b.a);
}

int n, na, nb;

int gettime()
{
    char buf[100];
    scanf("%s", buf);
    for (int i = 0; buf[i]; ++i) {
	if (buf[i] == ':')
	    buf[i] = ' ';
    }
    int a, b;
    sscanf(buf, "%d%d", &a, &b);
    return a * 60 + b;
}

void init()
{
    lst.clear();
    char buf[100];
    scanf("%d%d%d", &tt, &na, &nb);
    node tmp;
    for (int i = 0; i < na; ++i) {
	tmp.a = gettime();
	tmp.b = gettime();
	tmp.type = 0;
	lst.pb(tmp);
    }
    for (int i = 0; i < nb; ++i) {
	tmp.a = gettime();
	tmp.b = gettime();
	tmp.type = 1;
	lst.pb(tmp);
    }
    sort(lst.begin(), lst.end());
    n = na + nb;
}

bool ok(int ma, int mb)
{
    priority_queue<int, vector<int>, greater<int> > qa;
    priority_queue<int, vector<int>, greater<int> > qb;
    for (int i = 0; i < ma; ++i) {
	qa.push(0);
    }
    for (int i = 0; i < mb; ++i) {
	qb.push(0);
    }

    for (int i = 0; i < sz(lst); ++i) {
	if (lst[i].type == 0) {
	    if (qa.empty() || qa.top() > lst[i].a)
		return false;
	    qa.pop();
	    qb.push(lst[i].b + tt);
	}
	else {
	    if (qb.empty() || qb.top() > lst[i].a)
		return false;
	    qb.pop();
	    qa.push(lst[i].b + tt);
	}
    }
    return true;
}

void run()
{
    for (int i = 0; i <= na; ++i) {
	for (int j = 0; j <= nb; ++j) {
	    if (ok(i, j)) {
		printf("%d %d\n", i, j);
		return;
	    }
	}
    }
}

int main(void)
{
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
	init();
	printf("Case #%d: ", i);
	run();
    }
    return 0;
}

