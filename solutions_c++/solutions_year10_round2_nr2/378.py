
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

#define MAX 128

int x[MAX], v[MAX];
int vai[MAX];

int main(void)
{
	int nc, ca;
	int n, k, b, t;
	int i, j, l;
	int res, sum;

	scanf("%d", &nc);
	for(ca=1; ca<=nc; ca++)
	{
		printf("Case #%d: ", ca);

		scanf("%d %d %d %d", &n, &k, &b, &t);

		for(i=0; i<n; i++) scanf("%d", &x[i]);
		for(i=0; i<n; i++) scanf("%d", &v[i]);

		sum = 0;
		for(i=0; i<n; i++)
		{
			int ms = (b-x[i])/t;
			if((b-x[i]) % t) ms++;

			vai[i] = (v[i] >= ms);
			if(vai[i]) sum++;
		}
		if(sum < k)
		{
			puts("IMPOSSIBLE");
			continue;
		}

		sum = res = 0;				
		for(i=n-1; i>=0; i--)
		{
			if(!vai[i])
				sum++;
			else
			{
				res += sum;
				k--;
				if(!k) break;
			}
		}

bla:
		printf("%d\n", res);
	}

	return 0;
}
