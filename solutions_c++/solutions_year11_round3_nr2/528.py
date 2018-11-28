#pragma warning (disable : 4786)
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

__int64 pos[SZ];
__int64 cpos[SZ];
int cval[SZ];

int main()
{
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("B-small.out", "wt", stdout);

	//freopen("B-large.in", "rt", stdin);
	//freopen("B-large.out", "wt", stdout);
	int inp, r, kase, n, m, c, d, k, i, j, l, t;
	string s1, s2;
	scanf("%d", &inp);
	
	for(kase = 1; kase <= inp; kase++)
	{
	
		scanf("%d %d %d %d", &l, &t, &n, &c);

		for(i = 0; i < c; i++)
		{
			scanf("%d", &cval[i]);
		}

		pos[0] = 0;
		for(i = 1; i <= n; )
		{
			for(j = 0; j < c; j++)
			{
				pos[i] = pos[i - 1] + cval[j];
				i++;
			}
		}
		for(i = 0; i <= n; i++)
		{
			pos[i] = pos[i] * 2;
		}
		
		__int64 mx = 100000000000000000;
		__int64 res = 0;
		__int64 sv = 0;

		printf("Case #%d: ", kase);

		if(l == 0)
		{
			printf("%I64d\n", pos[n]);
		}
		if(l == 1)
		{
			for(i = 0; i < n; i++)
			{
				res = pos[n];
				if(pos[i] >= t)
				{
					res = res - (pos[i + 1] - pos[i]) / 2;
				}
				else
				{
					if(pos[i + 1] > t)
					{
						res =  res - (pos[i + 1] - t) / 2;
					}
				}
				if(res < mx)
					mx = res;
			}
			printf("%I64d\n", mx);
		}
		if(l == 2)
		{
			for(i = 0; i < n - 1; i++)
			{
				res = pos[n];
				if(pos[i] >= t)
				{
					res = res - (pos[i + 1] - pos[i]) / 2;
				}
				else
				{
					if(pos[i + 1] > t)
					{
						res =  res - (pos[i + 1] - t) / 2;
					}
				}
				for(j = i + 1; j < n; j++)
				{
					__int64 tres = res;
					if(pos[j] >= t)
					{
						tres = tres - (pos[j + 1] - pos[j]) / 2;
					}
					else
					{
						if(pos[j + 1] > t)
						{
							tres =  tres - (pos[j + 1] - t) / 2;
						}
					}
					if(tres < mx)
						mx = tres;
				}
			}
			printf("%I64d\n", mx);
		}

		
	
	}
	return 0;
}

