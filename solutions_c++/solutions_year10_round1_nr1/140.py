#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <ctime>
#include <map>
#include <queue>
#include <stack>
#include <string>

using namespace std;

#define Filename "a"
#define sqr(a) (a)*(a)
#define abs(a) ((a) < 0 ? -(a) : (a))
#define nextline for (int CcC = getchar();CcC != '\n' && CcC != EOF;CcC = getchar());

typedef long long lng;
typedef long double ldb;

const int INF = (1 << 30)-1;
const double EPS = 1e-9;

const int dx[] = {1, 1, 1, -1, -1, -1, 0, 0};
const int dy[] = {1, -1, 0, 1, -1, 0, 1, -1};

int n, T, k;

string s[55];

void Load()
{
	cin >> T;
}

bool da (int x, int y, vector <string> &cur)
{
	for (int i = 0;i < 8;i++)
	{
		int nx = x, ny = y, ost = k;
		while (nx < n && nx >= 0 && ny < n && ny >= 0)
		{
			if (cur[x][y] == cur[nx][ny]) ost--;
			else break;
			nx += dx[i];
			ny += dy[i];
		}
		if (ost <= 0) return true;
	}
	return false;
}

int go ()
{
	vector <string> cur(n);
	for (int i = 0;i < n;i++)
	{
		cur[i] = "";
		for (int j = n-1;j >= 0;j--)
			cur[i] += s[j][i];
	}
	for (int i = n-1;i >= 0;i--)
	{
		for (int j = 0;j < n;j++)
			if (cur[i][j] != '.')
			{
				int ni = i+1;
				while (ni < n && cur[ni][j] == '.')
				{
					cur[ni][j] = cur[ni-1][j];
					cur[ni-1][j] = '.';
					ni++;
				}
			}
	}
	bool w1 = false, w2 = false;
	for (int i = 0;i < n;i++)
	{
		//cerr << cur[i] << endl;
		for (int j = 0;j < n;j++)
		{
			if (cur[i][j] != '.')
			{
				if (da (i, j, cur))
				{
					if (cur[i][j] == 'B') w2 = true;
					else w1 = true;
				}
			}
		}
	}
	if (w1 & w2) return 2;
	if (w1) return 0;
	if (w2) return 1;
	return -1;
}

int main()
{
	freopen(Filename".in", "r", stdin);
	freopen(Filename".out", "w", stdout);
	Load();
	for (int step = 0;step < T;step++)
	{
		cin >> n >> k;
		for (int i = 0;i < n;i++)
			cin >> s[i];
		int ans = go ();
		printf("Case #%d: ", step+1);
		if (ans == 2) printf("Both\n");
		else if (ans == 1) printf("Blue\n");
		else if (ans == 0) printf("Red\n");
		else printf("Neither\n");
	}
	return 0;
}
