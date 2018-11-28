
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

#define MAXL 16
#define MAXD 5050

char dict[MAXD][MAXL];

char w[MAXL][256];

int main(void)
{
	int l, n, d;
	char c, buf[256];
	int ca;
	int i, j;
	int res;

	scanf("%d %d %d", &l, &d, &n);
	for(i=0; i<d; i++) scanf("%s", dict[i]);

	for(ca=1; ca<=n; ca++)
	{
		printf("Case #%d: ", ca);

		memset(w, 0, sizeof(w));

		res = 0;
		for(i=0; i<l; i++)
		{
			scanf(" %c", &c);
			if(c != '(')
			{
				w[i][c] = 1;
			}
			else
			{
				scanf("%[^)]%*c", buf);
				for(j=0; buf[j]; j++) w[i][buf[j]] = 1;
			}
		}

		for(i=0; i<d; i++)
		{
			for(j=0; j<l; j++) if(!w[j][dict[i][j]]) break;
			
			if(j==l) res++;
		}

		printf("%d\n", res);
	}

	return 0;
}
