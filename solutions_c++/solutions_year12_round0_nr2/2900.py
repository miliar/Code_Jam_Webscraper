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

int testcase , T;
int n , s , p , data[200] , ans , A , B;

void init()
{
	scanf("%d%d%d" , &n , &s , &p);
	int i;
	FOR (i , 1 , n) scanf("%d" , &data[i]);
	sort(data + 1 , data + n + 1);
}

void work()
{
	int i , j , k;
	A = p + max(0 , p - 2) + max(0 , p - 2);
	B = p + max(0 , p - 1) + max(0 , p - 1);
	ans = 0;
	FORD (i , n , 1)
	{
		if (data[i] >= A)
		{
			if (data[i] >= B)
			{
				ans++;
			}
			else
			{
				if (s)
				{
					s--;
					ans++;
				}
			}
		}
	}
	printf("Case #%d: %d\n" , T , ans);
}

int main()
{
	freopen("B.in" , "r" , stdin);
	freopen("B.out" , "w" , stdout);
	scanf("%d" , &testcase);
	FOR (T , 1 , testcase)
	{
		init();
		work();
	}
	return 0;
}
