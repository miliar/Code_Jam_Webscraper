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
#define abs(x) (((x) > 0) ? (x) : (-(x)))
#define REP(i , n) for ((i) = 0; (i) < (n); ++(i))
#define FOR(i , a , b) for ((i) = (a); (i) <= (b); ++(i))
#define FORD(i , a , b) for ((i) = (a); (i) >= (b); --(i))
typedef long long LL;

struct Tdata
{
	LL x , w;
};

LL n , m , tot , T , testcase;
Tdata data[208];
int cnt[208];
LL sum , ans;

inline int cmpx(const void *a , const void *b)
{
	Tdata p1 = *(Tdata*)a , p2 = *(Tdata*)b;
	return p1.x - p2.x;
}

void init()
{
	cin >> n >> m;
	m *= 2;
	int i , j , k;
	MM(data , 0);
	MM(cnt , 0);
	FOR (i , 1 , n)
	{
		cin >> data[i].x >> data[i].w;
		data[i].x *= 2;
	}
	qsort(data + 1 , n , sizeof(Tdata) , cmpx);
	FOR (i , 2 , n) data[i].x -= data[1].x;
	data[1].x = 0LL;
	FOR (i , 1 , n) cnt[i] = cnt[i - 1] + data[i].w;
}

bool check(LL x)
{
	LL now;
	int i , j , k , p = 1;
	now = -x;
	FOR (i , 2 , cnt[n])
	{
		if (i > cnt[p]) p++;
		now += m;
		if (now < data[p].x - x) now = data[p].x - x;
		LL delta = abs(now - data[p].x);
		if (abs(now - data[p].x) > x) return 0;
	}
	return 1;
}

void work()
{
	int i , j , k , p;
	LL l = 0 , r = 1000000000000000000LL;
	while (l < r)
	{
		LL mid = (l + r) / 2LL;
		if (check(mid)) r = mid;
		else l = mid + 1;
	}
	printf("Case #%d: " , T);
	if (r & 1) cout << r / 2LL << ".500000" << endl; else cout << r / 2LL << ".0000000" << endl;
}

int main()
{
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
	cin >> testcase;
	FOR (T , 1 , testcase)
	{
		init();
		work();
	}
	return 0;
}
