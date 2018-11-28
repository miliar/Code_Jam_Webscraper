
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

char comb[MAX][MAX];
char opp[MAX][MAX];

char s[MAX];

int qt[MAX];

int main(void)
{
	int nc;

	scanf("%d", &nc);
	for(int ca=1; ca<=nc; ca++)
	{
		printf("Case #%d: ", ca);
		//--------------------

		memset(comb, 0, sizeof(comb));
		memset(opp, 0, sizeof(opp));

		int c, d;

		scanf("%d", &c);
		for(int i=0; i<c; i++)
		{
			char buf[MAX];
			scanf("%s", buf);
			comb[buf[0]][buf[1]] = comb[buf[1]][buf[0]] = buf[2];
		}

		scanf("%d", &d);
		for(int i=0; i<d; i++)
		{
			char buf[MAX];
			scanf("%s", buf);
			opp[buf[0]][buf[1]] = opp[buf[1]][buf[0]] = 1;
		}

		int n;
		scanf("%d %s", &n, s);

		char deck[MAX], top = 0;
		for(int i=0; i<n; i++)
		{
			deck[top++] = s[i];

			char a=deck[top-1], b = deck[top-2];
			if(comb[a][b])
			{
				deck[top-2] = comb[a][b];
				top--;
			}
			else
			{
				int j;
				for(j=0; j<top-1; j++) if(opp[deck[j]][deck[top-1]]) break;
				if(j<top-1) top = 0;
			}
		}

		printf("[");
		for(int i=0; i<top; i++)
		{
			if(i>0) printf(", ");
			putchar(deck[i]);
		}
		printf("]\n");
	}

	return 0;
}
