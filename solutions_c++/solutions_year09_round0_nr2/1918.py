#include <vector>
#include <list>
#include <set>
#include <queue>
#include <deque>
#include <stack>
//#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
//#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>
#include <string>

using namespace std;

#define MP make_pair
#define FF first
#define SS second
#define SZ size()
#define PB push_back
#define all(x) (x).begin(), (x).end()
#define FORZ(i, n) for(typeof(n) i = 0 ; i !=n ; i++)
#define tr(c, it) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define dbg(x) cout << #x << " : " << x << "; " << flush;
#define dbge(x) cout << #x << " : " << x << ";" << endl;
#define GI ({int t; scanf("%d", &t); t;})
typedef long long LL;
typedef pair <int, int> II;
typedef vector <int> VI;

int map[100][100];
int next[100][100];
bool vis[100][100];
int dx [] = {0, -1, 0, 0, 1};
int dy [] = {0, 0, -1, 1, 0};
int row, col;

void cal_dfs(int u, int v)
{
    int mid = 0;
    int m = map[u][v];
    for(int t = 1; t <= 4; t++)
    {
	int x = u + dx[t];
	int y = v + dy[t];
	if(x >= 0 && x < row && y >= 0 && y < col)
	    if(map[x][y] < m) {
		mid = t;
		m = map[x][y];
	    }
    }
    next[u][v] = mid;
    return;
}

int mark_dfs(int u, int v, int mark)
{
    if(vis[u][v])
	return map[u][v];
    vis[u][v] = true;
    map[u][v] = mark;
    int t = next[u][v];
    return map[u][v] = mark_dfs(u + dx[t], v + dy[t], mark);
}

int main()
{
    int tMax = GI;
    FORZ(test, tMax)
    {
	row = GI; col = GI;
	FORZ(i, row)
	    FORZ(j, col)
	    	map[i][j] = GI;
	memset(next, 0, sizeof next);
	FORZ(i, row)
	    FORZ(j, col)
	    	cal_dfs(i, j);

	memset(vis, false, sizeof vis);

	int cnt = -1;
	FORZ(i, row)
	    FORZ(j, col)
	    	if(!vis[i][j])
		    cnt = mark_dfs(i, j, cnt + 1);

	printf("Case #%d:\n", test+1);
	FORZ(i, row) {
	    FORZ(j, col)
		printf("%c ", (char)('a' + map[i][j]));
	    printf("\n");
	}
    }
    return 0;
}
