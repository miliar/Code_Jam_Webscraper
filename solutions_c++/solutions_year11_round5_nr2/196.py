#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cassert>
#include <sstream>
#include <functional>
#include <algorithm>
#include <map>
#include <string>
#include <vector>
#include <set>
#include <queue>

using namespace std;

int nt;

int n;
int a[10008];
int b[10008];
int c[10008];

bool good(int k)
{
	/*for(int i = 0; i <= 10000; i++)
	if (a[i])
	{
		int len = 1;
		while(a[i + len]) len++;
		if (len < k) return false;
	}*/

	memset(c, 0, sizeof c);
//	puts("");	for(int  j = 0; j < 20; j++) printf("%3d", j); puts("");
	
	int left = n;
	while(left)
	{
		again: ;
		
//		for(int  j = 0; j < 20; j++) printf("%3d", a[j]); puts("");
		
		int i = 0;
		while(!a[i]) i++;
		
		for(int j = 0; j < k; j++)
		if (a[i + j] < 1)
		{
			if (i == 0 || c[i - 1] == 0)
			{
//				printf("i = %d\n", i);
				return false;
			}
//			printf("erased from %d\n", i);
			c[i - 1]--;
			while(a[i])
			{
				a[i]--;
				i++;
				left--;
			}
			if (!left) return true;
			goto again;
		}

		for(int j = 0; j < k; j++) a[i + j]--;
		left -= k;
		c[i + k - 1]++;	

//		printf("taken %d - %d\n", i, i + k - 1);
	}
	return true;
}

int main()
{
	int nt;
	scanf("%d", &nt);
	for(int tt = 1; tt <= nt; tt++)
	{
		fprintf(stderr, "test = %d\n", tt);
		printf("Case #%d: ", tt);
		
		memset(a, 0, sizeof a);
		
		scanf("%d", &n);
		for(int i = 0; i < n; i++)
		{
			int x;
			scanf("%d", &x);
			a[x]++;
		}
		
		if (n == 0)
		{
			puts("0");
			continue;
		}
		/*printf("%d\n", good(6));
		return 0;*/
		
		int L = 1, R = n + 1;
		/*while(R - L > 1)
		{
			int mid = (L + R) / 2;
			memcpy(b, a, sizeof a);
			if (good(mid)) L = mid; else R = mid;
			memcpy(a, b, sizeof b);
		}*/
		while(1)
		{
			memcpy(b, a, sizeof a);
			if (!good(L + 1)) break;
			L++;
			memcpy(a, b, sizeof b);
		}
		
		printf("%d\n", L);
	}
	return 0;
}