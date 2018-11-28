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

int main()
{
	//freopen("C-small-attempt0.in", "rt", stdin);
	//freopen("C-small.out", "wt", stdout);

	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "wt", stdout);
	int inp, r, kase, n, k, i, j;
	scanf("%d", &inp);
	
	for(kase = 1; kase <= inp; kase++)
	{
		int mn = 100000000;
		int sum = 0;
		k = 0;
		scanf("%d", &n);
		for(i = 0; i < n; i++)
		{
			scanf("%d", &r);
			if(r < mn)
				mn = r;
			sum = sum + r;
			k = k ^ r;
		}
		printf("Case #%d: ", kase);
		if(k > 0)
			printf("NO\n");
		else
			printf("%d\n", sum - mn);
		
	}
	return 0;
}

