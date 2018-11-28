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

int ci[1005];

int main() {

#define GETANS

#ifdef GETANS
	 freopen("C-large.in","rt",stdin);
	 freopen("ans.out","wt",stdout);
#endif

	int c,t;
	c = 0;
	scanf("%d", &t);
	while(t--)
	{
		memset(ci, 0, sizeof(ci));
		c++;
		int n,i,j;
		int ans, min;
		scanf("%d", &n);

		ans = 0;
		min = 0x1fffffff;
		for(i = 0; i < n; i++)
		{
			scanf("%d", ci+i);
			ans += ci[i];
			if(min > ci[i])
				min = ci[i];
		}

		int can = ci[0]^ci[1];
		for(i = 2; i < n; i++)
			can = can^ci[i];

		if(can != 0)
		{
			printf("Case #%d: NO\n", c); 
		}
		else
		{
			printf("Case #%d: %d\n", c, ans-min); 
		}
	}

	return 0;
}