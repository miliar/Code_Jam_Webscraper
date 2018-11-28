#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <map>
#include <iostream>
#include <sstream>
#include <queue>
#include <cstring>
#include <ctime>
#include <cfloat>

using namespace std;

#define SZ 1005

int g[SZ];

int gcd(int a, int b)
{
	if(b == 0)
		return a;
	return(gcd(b, a%b));
}

int main()
{
	freopen("C:\\Codejam 2010\\Qualification\\B-small-attempt0.in", "rt", stdin);
	freopen("C:\\Codejam 2010\\Qualification\\B-small.out", "wt", stdout);

	//freopen("C:\\Codejam 2010\\Qualification\\B-large.in", "rt", stdin);
	//freopen("C:\\Codejam 2010\\Qualification\\B-large.out", "wt", stdout);
	int inp, r, kase, n, k, i, j;
	scanf("%d", &inp);
	
	for(kase = 1; kase <= inp; kase++)
	{
		scanf("%d", &n);
		
		for(i = 0; i < n; i++)
		{
			scanf("%d", &g[i]);
		}
		//sort(g, g + n);
		k = g[1] - g[0];
		int mx = g[0];
		for(i = 0; i < n - 1; i++)
		{
			for(j = i + 1; j < n; j++)
			{
				r = abs(g[j] - g[i]);
				k = gcd(k , r);
			}
			if(g[i] > mx)
				mx = g[i];
		}
		r = mx % k;
		if(r != 0)
			r = k - r;
		printf("Case #%d: %I64d\n", kase, r);
	}
	return 0;
}

