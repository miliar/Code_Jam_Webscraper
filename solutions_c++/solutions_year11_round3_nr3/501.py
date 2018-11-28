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

#define SZ 10005
int freq[SZ];

int main()
{
	freopen("C-small-attempt0.in", "rt", stdin);
	freopen("C-small.out", "wt", stdout);

	//freopen("C-large.in", "rt", stdin);
	//freopen("C-large.out", "wt", stdout);
	int inp, r, kase, n, k, i, j, l ,h;
	scanf("%d", &inp);
	
	for(kase = 1; kase <= inp; kase++)
	{
		scanf("%d %d %d", &n, &l, &h);
		for(i = 0; i < n; i++)
		{
			scanf("%d", &r);
			freq[i] = r;
		}
		printf("Case #%d: ", kase);
		for(i = l; i <= h; i++)
		{
			for(j = 0; j < n; j++)
			{
				if(freq[j] % i == 0 || i % freq[j] == 0)
					continue;
				else
					break;
			}
			if(j == n)
			{
				printf("%d\n", i);
				break;
			}
		}
		if(i > h)
		{
			printf("NO\n");
		}
		
	}
	return 0;
}

