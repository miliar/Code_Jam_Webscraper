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

const int inf = 0x7f7f7f7f;
const double eps = 1e-9;

int c1[10][10], c2[10][10];
bool v[10];
int a[10];
int n, m;

void init()
{
    scanf("%d", &n);
    int a, b;
    memset(c1, 0, sizeof(c1));
    memset(c2, 0, sizeof(c2));
    for (int i = 1; i < n; ++i)  {
	scanf("%d%d", &a, &b);
	--a, --b;
	c1[a][b] = c1[b][a] = true;
    }
    scanf("%d", &m);
    for (int i = 1; i < m; ++i) {
	scanf("%d%d", &a, &b);
	--a, --b;
	c2[a][b] = c2[b][a] = true;
    }
}


bool dfs(int x)
{    
    if (x == m) {
	bool ok = true;
	for (int i = 0; i < m; ++i) {
	    for (int j = 0; j < m; ++j) {
		if (c2[i][j] && !c1[a[i]][a[j]]) {
		    ok = false;
		    break;
		}
	    }
	    if (!ok)
		break;
	}
	return ok;
    }
    for (int i = 0; i < n; ++i) {
	if (!v[i]) {
	    a[x] = i;
	    v[i] = true;
	    if (dfs(x + 1))
		return true;
	    v[i] = false;
	}
    }
    return false;
}

void run()
{
    memset(v, 0, sizeof(v));
    if (dfs(0)) {
	printf("YES\n");
    }
    else {
	printf("NO\n");
    }
}

int main(void)
{
    int c;
    scanf("%d", &c);
    for (int i=  1; i <= c; ++i) {
	printf("Case #%d: ", i);
	init();
	run();
    }
    return 0;
}


