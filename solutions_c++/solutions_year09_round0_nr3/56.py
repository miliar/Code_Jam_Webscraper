
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

//

char* tgt = "$welcome to code jam";
int m;

#define MAX 512

char buf[MAX];

int pd[MAX][MAX];

int main(void)
{
	int t;
	int n;
	int i, j, k;
	int ca;
	int cnt;

	m = strlen(tgt+1);
	memset(pd, 0, sizeof(pd));

	gets(buf);
	sscanf(buf, "%d ", &t);

	for(ca=1; ca<=t; ca++)
	{
		printf("Case #%d: ", ca);

		buf[0] = '$';
		gets(buf+1);
		n = strlen(buf+1);

		pd[0][0] = 1;

		for(i=1; i<=n; i++)
		{
			for(j=1; j<=m; j++)
			{
				if(buf[i] != tgt[j])
				{
					pd[i][j] = 0;
				}
				else
				{
					cnt = 0;

					for(k=0; k<i; k++) cnt += pd[k][j-1];

					pd[i][j] = cnt % 10000;
				}
			}
		}

		cnt = 0;

		for(i=1; i<=n; i++) cnt += pd[i][m];

		printf("%04d\n", cnt % 10000);
	}

	return 0;
}
