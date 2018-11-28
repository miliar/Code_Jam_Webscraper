#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <memory.h>

using namespace std;

#define fr(i,a,b) for(int i = (a); i <= (b); ++i)
#define frR(i,a,b) for(int i = (a); i >= (b); --i)
#define fi(a) for(int i = (0); i < (a); ++i)
#define fj(a) for(int j = (0); j < (a); ++j)
#define fk(a) for(int k = (0); k < (a); ++k)
#define CLR(a, b) memset((a), (b), sizeof((a)))
#define clr(a) CLR((a), 0)
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(),(v).end()

typedef long long ll;
typedef vector <int> vi;
typedef pair <int, int> pii;

const int maxn = 5000;
const int inf = 1000000000 + 7;
const double eps = 1e-5;

int n, m, a[500][500];
bool mark[500][500];
pii ans[500][500];
int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};
char res[500][500];
int cur;

pii dfs(int x, int y)
{
	if (mark[x][y])
		return (ans[x][y]);
	mark[x][y] = true;
	int ma = inf;
	fi(4)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
		if (ma > a[nx][ny])
			ma = a[nx][ny];
	}
	if (ma >= a[x][y])
	{
		ans[x][y] = mp(x, y);
		return (ans[x][y]);
	}
	fi(4)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
		if (ma == a[nx][ny])
		{
			ans[x][y] = dfs(nx, ny);
			return (ans[x][y]);
		}
	}
}

void solve()
{
	cin >> n >> m;
	fi(n)
		fj(m)
			cin >> a[i][j];

	clr(mark);
	fi(n)
		fj(m)
			ans[i][j] = dfs(i, j);
	
	fi(n)
		fj(m)
			res[i][j] = '0';
	cur = 0;
	fi(n)
	{
		fj(m)
		{
			if (res[ans[i][j].first][ans[i][j].second] == '0')
				res[ans[i][j].first][ans[i][j].second] = (char)('a' + cur++);
			res[i][j] = res[ans[i][j].first][ans[i][j].second];
			
			cout << res[i][j] << ' ';
		}
		cout << endl;
	}
}

void initf()
{
	//freopen("in.txt", "r",  stdin);
	//freopen("out.txt", "w",  stdout);
}

int main()
{
	initf();
	int t;
	cin >> t;
	fi(t)
	{
		printf("Case #%d:\n", i + 1);
		solve();
	}
	return (0);
}