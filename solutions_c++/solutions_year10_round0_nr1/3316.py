#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <queue>

#define pb push_back
#define pint pair <int, int>
#define mp make_pair
#define fi first
#define se second
#define vi vector<int>
#define vii vector<vi>
#define f(I, N) for(int (I) = 0; (I) < (N); (I) ++)
#define fd(I, N) for(int (I) = (N) - 1; (I) >= 0; (I) --)
#define lint long long
#define dbg 1
#define qwe if(dbg)
#define tch vector<short>

using namespace std;

int main()
{
	int t;
	scanf("%d", &t);
	for(int xx = 1;xx <= t;xx ++)
	{
		printf("Case #%d: ", xx);
		int n, k;
		scanf("%d%d", &n, &k);
		lint pow = 1<<n;
		if((k + 1)%pow == 0) printf("ON\n");
		else printf("OFF\n");
		
	}
return 0;
}
