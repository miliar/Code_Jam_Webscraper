#include <iostream>
#include <string>
#include <iomanip>
#include <stdio.h>
#include <vector>
#include <map>
#include <sstream>
#include <algorithm>
using namespace std;

#define rep(i, n) for (int i = 0; i < n; ++i)
#define rep2(i, x, n) for (int i = x; i < n; ++i)
#define repd(i, n) for (int i = n - 1; i >= 0; --i)
#define repd2(i, x, n) for (int i = n - 1; i >= x; --i)
#define _(a, b) memset(a, b, sizeof(a))
int ri() { int a; scanf( "%d", &a ); return a; }
double rf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; 
string rs() { scanf( "%s", sbuf ); return sbuf; }
long long rll() { long long a; scanf( "%lld", &a ); return a; }
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;
typedef map<string,string> mss;

int main()
{
	freopen("C:\\Users\\Administrator\\Desktop\\A-large.in","rt",stdin);
	freopen("C:\\Users\\Administrator\\Desktop\\C-large-practice.out","wt",stdout);
	int dx[]= {1, 1, 0, -1};
	int dy[] = {0, 1, 1, 1};

	int T = ri();
	rep(t, T)
	{
		vector<string> v;
		rep(i, 4) v.push_back(rs());

		bool notfinish = false;
		bool xwin = false;
		bool owin = false;
		rep(player, 2)
		{
			char ch = ((player == 0) ? 'X' : 'O');
			rep(i, 4) rep(j, 4) rep(k, 4) rep(l, 4)
			{
				int x = i + dx[k]*l;
				int y = j + dy[k]*l;
				if (x < 0 || x >= 4 || y < 0 || y >= 4)
					break;
				if (v[x][y] != ch && v[x][y] != 'T')
				{
					if (v[x][y] == '.')
						notfinish = true;
					break;
				}
				if (l == 3)
				{
					if (player == 0)
						xwin = true;
					else
						owin = true;
					goto go;
				}
			}
		}
go:;
		printf("Case #%d: ", t+1);
		if (xwin)
			printf("X won\n");
		else if (owin)
			printf("O won\n");
		else if (notfinish)
			printf("Game has not completed\n");
		else
			printf("Draw\n");
	}
	
	return 0;
}