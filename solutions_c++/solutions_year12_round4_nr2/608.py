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
	double r;
	int num;
};
struct Tpoint
{
	double x , y , r;
	int num;
};

int n , T , testcase;
double W , L;
Tdata data[10008];
int a[10008];
Tpoint ans[10008] , p[10008];

inline int cmp(const double& x)
{
	return (x < -precision ? -1 : (x > precision));
}

inline int cmp_r(const void* a , const void* b)
{
	Tdata p1 = *(Tdata*)a , p2 = *(Tdata*)b;
	return cmp(p1.r - p2.r);
}

void init()
{
	scanf("%d%lf%lf" , &n , &W , &L);
	int i;
	FOR (i , 1 , n)
	{
		scanf("%lf" , &data[i].r);
		data[i].num = i;
	}
	qsort(data + 1 , n , sizeof(Tdata) , cmp_r);
}

bool check()
{
	int N = 0 , i;
	double ymax = 0.0;
	Tpoint pnow;
	FORD (i , n , 1)
	{
		if (i == n)
		{
			pnow.x = pnow.y = 0;
		}
		else
		{
			pnow.x = p[N].x + p[N].r + data[i].r + precision;
			pnow.y = p[N].y;
			if (cmp(pnow.x - W) > 0)
			{
				pnow.x = 0.0;
				pnow.y = ymax + data[i].r + precision;
			}
		}
		if (cmp(pnow.y - L) > 0) return 0;
		++N;
		p[N].x = pnow.x;
		p[N].y = pnow.y;
		p[N].r = data[i].r;
		p[N].num = data[i].num;
		ymax = max(ymax , p[N].y + p[N].r);
	}
	return 1;
}

void work()
{
	int i , j , k;
	while (!check())
	{
		FOR (i , 1 , 200)
		{
			int t1 = rand() % n + 1;
			int t2 = rand() % n + 1;
			swap(data[t1] , data[t2]);
		}
	}
	FOR (i , 1 , n) ans[p[i].num] = p[i];
	printf("Case #%d: " , T);
	FOR (i , 1 , n)
	{
		printf("%.6lf %.6lf " , ans[i].x , ans[i].y);
	}
	printf("\n");
}

int main()
{
	freopen("b.in" , "r" , stdin);
	freopen("b.out" , "w" , stdout);
	scanf("%d" , &testcase);
	FOR (T , 1 , testcase)
	{
		init();
		work();
	}
	return 0;
}
