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

int n , m , ans , T , testcase;
int data[1008];

void init()
{
	scanf("%d" , &n);
	int i;
	FOR (i , 1 , n) scanf("%d" , &data[i]);
}

void work()
{
	int i , j , k;
	ans = 0;
	FOR (i , 1 , n) ans ^= data[i];
	printf("Case #%d: " , T);
	if (ans != 0) {printf("NO\n"); return;}
	ans = 0;
	sort(data + 1 , data + n + 1);
	FOR (i , 2 , n) ans += data[i];
	printf("%d\n" , ans);
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
