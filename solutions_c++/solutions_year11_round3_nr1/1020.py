#include <iostream>
#include <stdio.h>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <map>
#include <math.h>
#include <queue>
#include <stack>
#include <list>
#include <deque>
#include <set>
#include <numeric>
#include <functional>
#include <ctype.h>
#include <utility>
#include <cassert>
#include <time.h>
using namespace std;

#define  max(a,b)  ((a)>(b)?(a):(b))
#define  min(a,b)  ((a)<(b)?(a):(b))
#define out(x) (cout << #x << " = " << x <<endl)
const int inf = 0x3f3f3f3f;
const double eps = 1e-10;
#define N 100005


char G[54][54];
bool used[54][54];
int R,C;
bool ok(int x,int y)
{
	return (x >= 0 && x < R && y >=0 && y < C && G[x][y] == '#');
}
int main()
{
	int T;
	freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	cin >> T;
	int cases = 1;
	while (T--)
	{
		
		int i,j,k,cnt = 0;
		cin >> R >> C;
		for(i = 0; i < R; i++)
		{
			scanf("%s",G[i]);
			for(j = 0; j < C; j++)
				if(G[i][j] == '#')
				{
					cnt++;
				}
		}
		printf("Case #%d:\n",cases++);
		if(cnt%4)
		{
			puts("Impossible");
			continue;
		}
		memset(used,0,sizeof(used));
		int tt = 0;
		bool flag = true;
		for(i = 0; i < R; i++)
		{
			for(j = 0; j < C;j++)
			{
				if(G[i][j] == '#' && !used[i][j])
				{
                    G[i][j] = '/';
					if(ok(i,j+1) && !used[i][j+1])
					{
						G[i][j+1] = '\\';
						used[i][j+1] = 1;
					}
					if(ok(i+1,j+1) && !used[i+1][j+1])
					{
						G[i+1][j+1] = '/';
						used[i+1][j+1] = 1;
					}
					if(ok(i+1,j) && !used[i+1][j] )
					{
						G[i+1][j] = '\\';
						used[i+1][j] = 1;
					}
					tt++;
				}
			}
		}
		if(tt == cnt/4)
		{
			for(i = 0; i < R; i++)
			{
				for(j = 0; j < C; j++)
					printf("%c",G[i][j]);
				puts("");
			}
		}
		else
			puts("Impossible");
	}
	return 0;
}