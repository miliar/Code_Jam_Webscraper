#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
#define MAX_LONG_LONG 9223372036854775807
#define MAX_INT  2147483647
#define MAX_LONG 2147483647
using namespace std;


int main() {
	freopen("..//input.txt", "rt", stdin);
	freopen("..//output.txt", "wt", stdout);
	int tc; 
	long position[10000], isMark[10000], g[10000]; 
	__int64 money[10000];
	scanf("%d", &tc);
	for(int t = 1; t <= tc; t ++)
	{
		memset(money, 0, sizeof(money));
		memset(position, 0, sizeof(position));
		memset(isMark, 0, sizeof(isMark));
		memset(g, 0, sizeof(g));
		long R,k, N;
		scanf("%ld %ld %ld", &R, &k, &N);
		for(int i = 0; i < N; i ++)
		{
			scanf("%ld", &g[i]);
		}

		long pos=0;
		long lastpos = 0;
		__int64 tmp;
		int x;
		int groups;
		for(i = 0;  i < 10000; i ++)
		{
			x = i;
			tmp = 0;
			groups = N;
			while(tmp + g[pos] <= k && groups > 0)
			{
				tmp += g[pos];
				pos ++;
				pos = pos % N;
				groups --;
			}
			lastpos = pos==0?(N-1):(pos - 1);
			position[i]=lastpos;
			money[i] = tmp;
			if(isMark[lastpos] == 1)
				break;
			else
				isMark[lastpos] = 1;			
		}
		long cycle = 0;
		__int64 cmon = 0;
		__int64 mon2 = 0;
		for(i = 0; i < 10000; i ++)
		{
			if(position[i] == position[x])
			{
				cycle = x - i;
				break;
			}
		}
		for(int j = i + 1; j <= x; j ++)
		{
			cmon += money[j];
		}

		for(j = 0; j <= i; j ++)
		{
			mon2 = mon2 + money[j];
		}
		long times, left;
		times = (R - i - 1) / cycle;
		left = (R - i - 1) % cycle;

		cmon = cmon * times;
		cmon += mon2;
		for(j = i + 1; j < left + i + 1; j ++ )
		{
			cmon += money[j];
		}
		
		printf("Case #%d: %I64d\n", t, cmon);
	}
}