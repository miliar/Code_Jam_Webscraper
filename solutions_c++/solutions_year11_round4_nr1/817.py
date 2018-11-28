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

struct Tdata
{
	int x , y , s , l;
};

int n , m , tot , testcase , T;
double w , r , ans , t;
Tdata data[1008];

void init()
{
	scanf("%d%lf%lf%lf%d" , &m , &w , &r , &t , &n);
	int i , j , k;
	tot = 0;
	FOR (i , 1 , n)
	{
		scanf("%d%d%d" , &data[i].x , &data[i].y , &data[i].s);
		data[i].l = data[i].y - data[i].x;
		tot += data[i].y - data[i].x;
	}
	tot = m - tot;
	data[++n].l = tot; data[n].s = 0;
}

inline int cmp(const void *a , const void *b)
{
	Tdata p1 = *(Tdata*)a , p2 = *(Tdata*)b;
	return p1.s - p2.s;
}

void work()
{
	qsort(data + 1 , n , sizeof(Tdata) , cmp);
	int i , j , k;
	ans = 0.0;
	FOR (i , 1 , n)
	{
		double tp = (double)data[i].l / ((double)data[i].s + (double)r);
		tp = min(tp , t);
		double wt = ((double)data[i].l - ((double)data[i].s + (double)r) * tp) / ((double)data[i].s + (double)w);
		t -= tp;
		ans += tp + wt;
	}
	printf("Case #%d: %.8lf\n" , T , ans);
}

int main()
{
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
	scanf("%d" , &testcase);
	FOR (T , 1 , testcase)
	{
		init();
		work();
	}
	return 0;
}
