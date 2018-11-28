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

const LL K = 1000000000000000LL;
LL n , d , g , pd , pg , pa;
int T , testcase;

int main()
{
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
	scanf("%d" , &testcase);
	FOR (T , 1 , testcase)
	{
		cin >> n >> pd >> pg;
		printf("Case #%d: " , T);
		bool flag = 0;
		FOR (d , 1 , min(1000LL , n))
		{
			if (d * pd % 100LL == 0)
			{
				LL D = d * pd / 100LL;
				if (K / 100LL * pg - D <= K - d && K / 100LL * pg - D >= 0) flag = 1;
			}
		}
		FORD (d , n , max(1LL , n - 1000LL))
		{
			if (d * pd % 100LL == 0)
			{
				LL D = d * pd / 100LL;
				if (K / 100LL * pg - D <= K - d && K / 100LL * pg - D >= 0) flag = 1;
			}
		}
		if (flag) printf("Possible\n"); else printf("Broken\n");
	}
	return 0;
}
