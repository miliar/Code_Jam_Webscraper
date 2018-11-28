#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <set>
using namespace std;
#define MM(a , x) memset(a , x , sizeof(a))
#define sqr(x) ((x) * (x))
#define abs(x) ((x > 0) ? (x) : -(x))
#define REP(i , n) for ((i) = 0; (i) < (n); ++(i))
#define FOR(i , a , b) for ((i) = (a); (i) <= (b); ++(i))
#define FORD(i , a , b) for ((i) = (a); (i) >= (b); --(i))
typedef long long LL;

set<int> hasht;
int testcase , T;
int A , B , ans , n , limit;

void work()
{
	int i , j , k;
	ans = 0;
	n = 0; limit = 1;
	i = A;
	while (i)
	{
		n++;
		i /= 10;
		limit *= 10;
	}
	limit /= 10;
	FOR (i , A , B)
	{
		k = i;
		hasht.clear();
		FOR (j , 1 , n)
		{
			if (k >= limit && i < k && k <= B)
			{
				if (hasht.find(k) == hasht.end())
				{
					hasht.insert(k);
					ans++;
				}
			}
			int h = k / limit;
			int tp = (k % limit) * 10 + h;
			k = tp;
		}
	}
	printf("Case #%d: %d\n" , T , ans);
}

int main()
{
	freopen("C.in" , "r" , stdin);
	freopen("C.out" , "w" , stdout);
	scanf("%d" , &testcase);
	FOR (T , 1 , testcase)
	{
		scanf("%d%d" , &A , &B);
		work();
	}
}
