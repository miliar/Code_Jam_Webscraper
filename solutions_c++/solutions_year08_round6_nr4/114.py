#include <iostream>
#include <string>
using namespace std;

#define INPUTFILENAME "D-small-attempt0.in"
#define OUTPUTFILENAME "output.txt"
template<class T> inline void smaller(T &a,T b){if(b<a) a=b;}
template<class T> inline void larger(T &a,T b){if(b>a) a=b;}

const int maxn = 100;
int n, m;
int map[maxn][maxn];
int maps[maxn][maxn];
int num[maxn];
bool mark[maxn];

void init()
{
	cin >> n;
	memset(map, 0, sizeof(map));
	memset(maps, 0, sizeof(maps));
	memset(num, 0, sizeof(num));
	memset(mark, 0, sizeof(mark));
	int x, y;
	for (int i = 0; i < n - 1; i++)
	{
		cin >> x >> y;
		x--;
		y--;
		map[x][y] = 1;
		map[y][x] = 1;
	}
	cin >> m;
	for (int i = 0; i < m - 1; i++)
	{
		cin >> x >> y;
		x--;
		y--;
		maps[x][y] = maps[y][x] = 1;
	}
}

bool OK(int i, int j)
{
	for (int k = 0; k < i; k++)
		if (map[num[k]][j] != maps[k][i])
			return false;
	return true;
}

bool search(int i)
{
	if (i == m)
		return true;
	for (int j = 0; j < n; j++)
		if (!mark[j] && OK(i, j))
		{
			mark[j] = true;
			num[i] = j;
			if (search(i + 1))
				return true;
			mark[j] = false;
		}
	return false;
}

void solve(int testnumber)
{
	cout << "Case #" << testnumber << ": ";
	if (search(0))
		cout << "YES" << endl;
	else
		cout << "NO" << endl;
}	

int main()
{
	int testnumber;
	freopen(INPUTFILENAME, "r", stdin);
	freopen(OUTPUTFILENAME, "w", stdout);
	cin >> testnumber;
	for (int i = 0; i < testnumber; i++)
	{
		init();
		solve(i + 1);
	}
	return 0;
}