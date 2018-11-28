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

int n , m , tot , testcase;
double ans;
int data[1008];
bool vis[1008];

void init()
{
	scanf("%d" , &n);
	int i;
	MM(vis , 0);
	FOR (i , 1 , n)
	{
		scanf("%d" , &data[i]);
	}
}

void work()
{
	ans = 0.0;
	int i , j;
	FOR (i , 1 , n) if (i != data[i]) ans++;
	printf("Case #%d: %.6lf\n" , testcase , ans);
}

int main()
{
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
	int T;
	scanf("%d" , &T);
	FOR (testcase , 1 , T)
	{
		init();
		work();
	}
	return 0;
}
