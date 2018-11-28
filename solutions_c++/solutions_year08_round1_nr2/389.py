#include <iostream>
#include <string>
using namespace std;

#define INPUTFILENAME "B-small-attempt0.in.txt"
#define OUTPUTFILENAME "output.txt"

const int MAXN = 15;
const int MAXM = 110;
int n, m;
int t[MAXM];
int c[MAXM][MAXN];
int a[MAXN];

void init()
{
	cin >> n >> m;
	for (int i = 0; i < m; i++)
	{
		cin >> t[i];
		for (int j = 0; j < t[i]; j++)
		{
			int x, y;
			cin >> x >> y;
			if (y == 0)
				c[i][j] = x;
			else
				c[i][j] = -x;
		}
	}
}

bool check()
{
	for (int i = 0; i < m; i++)
	{
		bool mark = false;
		for (int j = 0; j < t[i]; j++)
			if (c[i][j] > 0 && a[c[i][j]] ==0 ||
				c[i][j] < 0 && a[-c[i][j]] == 1)
			{
				mark = true;
				break;
			}
		if (!mark)
			return false;
	}
	return true;
}

bool search(int i)
{
	if (i > n) 
		if (check())
			return true;
		else
			return false;
	else
	{
		a[i] = 0;
		if (search(i + 1))
			return true;
		else
		{
			a[i] = 1;
			return search(i + 1);
		}
	}
}

void solve(int testnumber)
{
	cout << "Case #" << testnumber << ":";
	if (search(1))
	{
		for (int i = 1; i <= n; i++)
			cout << ' ' << a[i];
		cout << endl;
	}
	else
		cout << " IMPOSSIBLE" << endl;
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