#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;

const double eps = 1E-9;

bool Equal(double d1, double d2)
{
	return abs(d1-d2) < eps;
}

int main() {

#define GETANS

#ifdef GETANS
	 freopen("A-small-attempt1.in","rt",stdin);
	freopen("ans.out","wt",stdout);
#endif

	int c,t;
	c = 0;
	scanf("%d", &t);
	while(t--)
	{
		c++;
		int n, pd, pg;
		scanf("%d %d %d", &n, &pd, &pg);
/*
Case #1: Possible
Case #2: Broken
Case #3: Possible
*/

		if(n > 1000)
			n = 1000;
		int i,j;
		int m = 1000;
		bool finded = false;
		for(i = 1; i <= n; i++)
		{
			double tmp = (pd/100.0) * i;
			int winToday = int(tmp);
			if(!Equal(winToday, tmp))
			{
				continue;
			}
			int lostToday = i-winToday;
			for(j = 1;j <= m; j++)
			{
				tmp = (pg/100.0) * j;
				int winTotal = int(tmp);
				if(!Equal(winTotal, tmp))
					continue;
				int lostTotal = j - winTotal;

				if(winToday <= winTotal && lostToday <= lostTotal){
					//printf("%d %d\n", i,j);
					finded = true;
					break;
				}
			}

			if(finded)
				break;
		}

		if(finded)
		{
			printf("Case #%d: Possible\n",c);
		}
		else
		{
			printf("Case #%d: Broken\n",c);
		}


		/*
		if(pd != 0 && pg == 0)
		{
			printf("Case #%d: Broken\n", c);
			continue;
		}

		if(pg == 0 && pg != 0)
		{
			printf(
		}

		if(pd != 100 && pg == 100){
			printf("Case #%d: Broken\n", c);
			continue;
		}

		for(i = 0; i <= n; i++)
		{
			int t = i*pd;
			if(t % 100 == 0)
			{
				break;
			}
		}

		if(i < n+1)
		{
			printf("Case #%d: Possible\n",c);
		}
		else
		{
			printf("Case #%d: Broken\n",c);
		}
	*/
	}

	return 0;
}