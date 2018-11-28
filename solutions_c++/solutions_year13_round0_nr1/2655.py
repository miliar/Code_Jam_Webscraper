#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <stdlib.h>
#include <sstream>
#include <assert.h>

#include <time.h>
#pragma comment(linker, "/STACK:20000000")

#define fr(i,a,b) for(int i=(int)(a);i<=(int)(b);i++)
#define fd(i,a,b) for(int i=(int)(a);i>=(int)(b);i--)
#define mp make_pair
#define pb push_back
#define ll long long

using namespace std;

int ri(){int x;scanf("%d",&x);return x;}
ll rll(){ll x;scanf("%lld",&x);return x;}

char s[10][10];
int dx[] = {1,1,0,-1,-1,-1,0,1},dy[] = {0,1,1,1,0,-1,-1,-1};

string w[] = { "","X won","O won","Draw","Game has not completed"};

bool check_range(int x,int y)
{
	return x > 0 && x < 5 && y > 0 && y < 5;
}

bool check(char c)
{
	fr(sx,1,4)
	fr(sy,1,4)
	{
		int x = sx, y = sy;
		if (s[x][y] == c)
		{
			fr(i,0,7)
			{
				int T = 0, a = 1;
				x = sx, y = sy;
				fr(j,1,7)
				{
					x += dx[i], y += dy[i];
					if (!check_range(x,y))
						break;
					if (s[x][y] == c)
						a++;
					if (s[x][y] == 'T')
						T++;
				}
				if (a + T == 4)
					return true;
			}
			
		}
	}
	return false;
}

void solve()
{
	int test = ri();
	fr(testing,1,test)
	{
		getchar();
		fr(i,1,4)
			gets(s[i]+1);
		int res = 3;
		int cnt = 0;
		fr(i,1,4)
			fr(j,1,4)
				if (s[i][j] == '.')
					cnt++;
		if (cnt)
			res = 4;
		if (check('X'))
			res = 1;
		else
		if (check('O'))
			res = 2;
		printf("Case #%d: %s\n",testing,w[res].c_str());
	}


}

int main()
{
	/*#ifndef ONLINE_JUDGE
		freopen("C:/Users/CleRIC/Desktop/Универ/acm.timus.ru/input.txt","rt",stdin);
		freopen("C:/Users/CleRIC/Desktop/Универ/acm.timus.ru/output.txt","wt",stdout);
	#else
		//freopen("input.in","rt",stdin);
		//freopen("output.out","wt",stdout);
	#endif*/

	solve();

	/*#ifndef ONLINE_JUDGE
		printf("\n\ntime-%.3lf",clock()*1e-3);
	#endif*/

	return 0;
}