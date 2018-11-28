#include <iostream>
#include <set>
#include <string>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

string name = "a";

int n;
char a[1000][1000];
char b[1000][1000];

void clear(int n)
{
	for (int i = 0; i < n*2 + 2; i++) for (int j = 0; j < n*2 + 2; j++) b[i][j] = ' ';
}

bool check(int n)
{
//	cerr << "check: " << n << endl;
//	for (int i = 0; i < n*2-1; i++)
//		cerr << b[i] << "|" << endl;
	for (int i = 0; i < n; i++)
	{
		int s = n - 1 - i;
		for (int j = 0; j <= i; j++, s += 2)
			{
//				cerr << i << ' ' << s << ' ' << b[n*2-2-i][s] << ' ' << b[n*2-2-i][2*n - 2 - s] << endl;
				if (b[i][s] != ' ' && b[i][s] != b[n*2-2-i][s] && b[n*2-2-i][s] != ' ') 
				{
					return false;
				}
				if (b[i][s] != ' ' && b[i][s] != b[i][n*2-2-s] && b[i][n*2-2-s] != ' ') return false;
				
				if (b[n*2-2-i][s] != ' ' && b[n*2-2-i][s] != b[n*2-2-i][n*2-2-s] && b[n*2-2-i][n*2-2-s] != ' ') return false;
			}
	}
//	cerr << "true" << endl;
	return true;
}

void copy(int r, int c)
{
	//cerr << "copy: " << r << ' ' << c << endl;
	for (int i = 0; i < n*2 - 1; i++)
		for (int j = 0; j < n*2 - 1; j++)
			b[r+i][c+j] = a[i][j];
}

void solve()
{
	cin >> n;
	memset(a, 0, sizeof a);

	cin.getline(a[0], 1000);
	for (int i = 0; i < 2*n-1; i++)
	{
		cin.getline(a[i], 1000);
	}
	
	for (int i = 0; i < 2*n-1; i++) for (int j = 0; j < 2*n -1; j++)
		if (a[i][j] != '0' && !(a[i][j] >= '0' && a[i][j] <= '9')) a[i][j] = ' ';
	
	int res = 1 << 30;
	for (int s = n; s <= n*3 + 1 && res > 1e9; s++)
	{
		for (int r = 0; r <= s - n; r++)
		{
			clear(s);
			copy(r, s-1-r - (n - 1));
			if (check(s)) 
			{
				res = s*s - n * n;
				break;
			}
			clear(s);
			copy(r, s-1 + r - (n - 1));
			if (check(s)) 
			{
				res = s*s - n * n;
				break;
			}
			
			clear(s);
			copy(s*2-1-r-(2*n-1), s-1-r - (n - 1));
			if (check(s)) 
			{
				res = s*s - n * n;
				break;
			}
			clear(s);
			copy(s*2-1-r-(2*n-1), s-1 + r - (n - 1));
			if (check(s)) 
			{
				res = s*s - n * n;
				break;
			}
		}
	}
	cout << res << endl;
	cerr << res << endl;
}

int main()
{
	freopen((name + ".in").c_str(), "r", stdin);
	freopen((name + ".out").c_str(), "w", stdout);
	
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++)
	{
		cout << "Case #" << test << ": ";
		cerr << "Case #" << test << ": ";
		solve();
	}
	return 0;
}