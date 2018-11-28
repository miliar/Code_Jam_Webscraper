#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <queue>
#include <time.h>

using namespace std;

#define RP(a,h) for(int (a)=0; (a)<(h); (a)++)
#define FR(a,l,h) for((a)=(l); (a)<=(h); (a)++)
#define INF 2000000000
#define sz size()
#define pb push_back
#define sv(v) sort((v).begin(), (v).end())
#define ABS(x) (((x)>0)?(x):(-(x)))

int t, h, w;
int a[102][102];
char b[102][102];
int dx[4] = {0, -1, 1, 0};
int dy[4] = {-1, 0, 0, 1};
char now = 'a';

bool ok(int y, int x)
{
	return (y >= 0 && x >= 0 && y < h && x < w);
}

char flood(int y, int x)
{
	int idx = -1;
	int cur = 1000000;
	RP(i, 4)
	{
		int xx = x+dx[i];
		int yy = y+dy[i];
		if (ok(yy, xx) && a[yy][xx] < a[y][x] && (idx == -1 || a[yy][xx] < cur)) { idx = i; cur = a[yy][xx]; }
	}
	
	if (idx == -1)
	{
		b[y][x] = now;
		now++;
	}
	else if (b[y+dy[idx]][x+dx[idx]] != '*')
	{
		b[y][x] = b[y+dy[idx]][x+dx[idx]];		
	}
	else
	{
		b[y][x] = flood(y+dy[idx], x+dx[idx]);
	}
	return b[y][x];
}

int main()
{
	cin >> t;
	
	RP(test, t)
	{
		cin >> h >> w;
		
		RP(i,h)
		{
			RP(j,w)
			{
				cin >> a[i][j];
				b[i][j] = '*';
			}
		}
		
		
		
		now = 'a';
		RP(i,h)
		{
			RP(j,w)
			{
				if (b[i][j] == '*')
				{
					flood(i, j);
				}
			}
		}
		
		cout << "Case #" << test+1 << ":" << endl;
		RP(i, h)
		{
			RP(j, w)
			{
				cout<< b[i][j] << " ";
			}
			cout << endl;
		}
	}
	

	
}
