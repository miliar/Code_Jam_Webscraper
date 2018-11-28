//#pragma comment(linker,"/STACK:256000000")

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <ctime>
#include <cassert>
#include <string>

using namespace std;

#define ldb long double
#define lng long long
#define nextline {int c; while ((int c = getchar()) != 10 && c != EOF);}

#define PI 3.1415926535897932384626433832795
#define EPS 1e-12

#define sqr(x) ((x) * (x))
#define ABS(a) ((a)<0?-(a):(a))
#define EQ(a,b) (ABS((a)-(b))<EPS)

#define all(a) a.begin(), a.end()
#define two(i) (1 << (i))
#define has(mask, i) ((((mask) & two(i)) == 0) ? false : true)

const int inf = 1000 * 1000 * 1000;
const lng inf64 = 1000LL * 1000LL * 1000LL * 1000LL * 1000LL * 1000LL;


#define MAXN 200
int a[MAXN][MAXN];
bool mark[MAXN*MAXN];
int b[MAXN][MAXN];
char coller[MAXN][MAXN];
int n, m, col;
vector <int> next[MAXN*MAXN];
int base;


class point
{
public:
	int x, y;
};
vector <int> q;

void Load()
{
	scanf("%d%d", &n, &m);
	int i, j;
	point w;
	for (i = 1; i <= n; i++)		
		for (j = 1; j <= m; j++)
		{
			scanf("%d", &a[i][j]);
			w.x = i;
			w.y = j;
		}
	base = (max(n, m) + 2);
	for (i = 1; i <= n; i++)
	for (j = 1; j <= m; j++)
		next[(i - 1) * base + j].clear();
}   

void dfs(int i)
{
	mark[i] = 1;
	int x, y, u;
	y = i % base;
	x = i / base + 1;
	b[x][y] = col;

	for (u = 0; u < (int) next[i].size(); u++)
		if (mark[next[i][u]] == 0)
			dfs(next[i][u]);
}

void Solve()
{
	int i, j;
	col = 0;
	int cur_ans;
	int w, t;



	for (i = 1; i <= n; i++)
	for (j = 1; j <= m; j++)
	{
		cur_ans = a[i][j];
		if (cur_ans > a[i - 1][j])	
		{
			cur_ans = a[i - 1][j];
			w = (i - 2) * base + j;
		}
		if (cur_ans > a[i][j - 1])	
		{
			cur_ans = a[i][j - 1];
			w = (i - 1) * base + j - 1;
		}
		if (cur_ans > a[i][j + 1])	
		{
			cur_ans = a[i][j + 1];
			w = (i - 1) * base + j + 1;
		}
		if (cur_ans > a[i + 1][j])	
		{
			cur_ans = a[i + 1][j];
			w = (i) * base + j;
		}
		t = (i - 1) * base + j;
		if (cur_ans != a[i][j])
		{
			next[t].push_back(w);
			next[w].push_back(t);
		}
		else
			q.push_back(t);
	}

	for (i = 0; i < (int) q.size(); i++)
	{
		col++;
		dfs(q[i]);
	}

	char c = 'a';
	for (w = 1; w <= n; w++)
		for (t = 1; t <= m; t++)
	    	if (coller[w][t] == 0)
	    	{
	    		for (i = 1; i <= n; i++)
		    		for (j = 1; j <= m; j++)
		    			if (b[i][j] == b[w][t])
		    				coller[i][j] = c;
		       	c++;
		    }
}
                
int main()
{
	freopen("b.in", "rt", stdin);
	freopen("b.out", "wt", stdout);
	int t, r;
	cin >> t;
	for (r = 1; r <= t; r++)
	{
		memset(mark, 0, sizeof (mark));
		memset(a, 0x7F, sizeof(a));
		memset(b, 0, sizeof(b));
		memset(coller, 0, sizeof(coller));
		q.clear();

		Load();
		Solve();

		cout << "Case #" << r <<":\n";
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= m; j++)
				cout << coller[i][j] <<" ";
			cout << "\n";
		}
	}
	return 0;
}
