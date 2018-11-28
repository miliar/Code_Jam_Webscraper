#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

int gcd(int a, int b)
{
	if(a%b == 0) return b;
	return gcd(b, a%b);
}

int main()
{
	int t;
	scanf("%d", &t);
	int tt = t;
	while(t--)
	{
		long long n;
		int pg, pd, wd, wg, td, tg;
		cin>>n>>pd>>pg;
		
		if(pg == 0 && pd != 0)
		{
			printf("Case #%d: Broken\n", tt-t);
			continue;
		}
		
		if(pg == 100 && pd != 100)
		{
			printf("Case #%d: Broken\n", tt-t);
			continue;
		}
		
		int g = gcd(pd, 100);
		wd = pd/g;
		td = 100/g;
		
		if(n>=td)
			printf("Case #%d: Possible\n", tt-t);
		else
			printf("Case #%d: Broken\n", tt-t);
	}
	return 0;
}
