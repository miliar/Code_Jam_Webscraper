#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;
#define MM(a , x) memset(a , x , sizeof(a))
#define sqr(x) ((x) * (x))
#define abs(x) ((x > 0) ? (x) : -(x))
#define REP(i , n) for ((i) = 0; (i) < (n); ++(i))
#define FOR(i , a , b) for ((i) = (a); (i) <= (b); ++(i))
#define FORD(i , a , b) for ((i) = (a); (i) >= (b); --(i))
typedef long long LL;

const double precision = 1e-6;

struct Tdata
{
	double x , y , w;
};
struct Tvector
{
	double x , y;
};

int n , m , d , testcase , T , ans;
Tdata data[508][508];

void init()
{
	scanf("%d %d %d\n" , &n , &m , &d);
	int i , j , k;
	char ch;
	MM(data , 0);
	FOR (i , 1 , n)
	{
		FOR (j , 1 , m)
		{
			ch = getchar();
			data[i][j].x = -0.5 + (double)i;
			data[i][j].y = -0.5 + (double)j;
			data[i][j].w = (double)d + (ch - '0');
		}
		ch = getchar();
	}
}

void work()
{
	int i , j , k , size , tp , x , y;
	Tvector now , c;
	ans = 0;
	FOR (size , 3 , min(n , m))
	{
		FOR (i , 1 , n) FOR (j , 1 , m)
		{
			now.x = now.y = c.x = c.y = 0.0;
			if (i + size - 1 > n || j + size - 1 > m) continue;
			tp = 0;
			FOR (x , i + 1 , i + size - 2) FOR (y , j , j + size - 1)
			{
				tp++;
				c.x += data[x][y].x; c.y += data[x][y].y;
			}
			FOR (y , j + 1 , j + size - 2)
			{
				tp++;
				c.x += data[i][y].x; c.y += data[i][y].y;
				tp++;
				c.x += data[i + size - 1][y].x; c.y += data[i + size - 1][y].y;
			}
			c.x /= (double)tp; c.y /= (double)tp;
			FOR (x , i + 1 , i + size - 2) FOR (y , j , j + size - 1)
			{
				Tvector d;
				d.x = data[x][y].x - c.x;
				d.y = data[x][y].y - c.y;
				now.x += d.x * data[x][y].w;
				now.y += d.y * data[x][y].w;
			}
			FOR (y , j + 1 , j + size - 2)
			{
				Tvector d;
				d.x = data[i][y].x - c.x;
				d.y = data[i][y].y - c.y;
				now.x += d.x * data[i][y].w;
				now.y += d.y * data[i][y].w;
				d.x = data[i + size - 1][y].x - c.x;
				d.y = data[i + size - 1][y].y - c.y;
				now.x += d.x * data[i + size - 1][y].w;
				now.y += d.y * data[i + size - 1][y].w;
			}
			if (abs(now.x) < precision && abs(now.y) < precision) ans = max(ans , size);
		}
	}
	if (ans == 0) printf("Case #%d: IMPOSSIBLE\n" , T);
	else printf("Case #%d: %d\n" , T , ans);
}

int main()
{
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
	scanf("%d\n" , &testcase);
	FOR (T , 1 , testcase)
	{
		init();
		work();
	}
	return 0;
}
