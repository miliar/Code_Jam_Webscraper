#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <algorithm>
using namespace std;

typedef long long ll;

int r[1111];

double x[1111];
double y[1111];

double rdbl(int limit)
{
	return ((rand()<<15)+rand())/(double)((RAND_MAX<<15)+RAND_MAX)*limit;
}

int main(void)
{
	freopen("b-small.in","rt",stdin);
	freopen("b-small.out","wt",stdout);
	srand(time(NULL));

	int TK = 0;
	int TKN = 0;
	scanf("%d",&TK);
	while(TK--)
	{
		printf("Case #%d: ",++TKN);
		int N = 0;
		int W = 0;
		int L = 0;
		scanf("%d %d %d",&N,&W,&L);
		for(int i = 0;i < N;i++) scanf("%d",&r[i]);
		for(int i = 0;i < 10000000;i++)
		{
			for(int j = 0;j < N;j++)
			{
				x[j] = rdbl(W);
				y[j] = rdbl(L);
			}

			bool fail = false;
			for(int j = 0;j < N;j++)
			{
				for(int k = j+1;k < N;k++)
				{
					double dx = x[j]-x[k];
					double dy = y[j]-y[k];
					double dr = r[j]+r[k];
					if(dx*dx+dy*dy < dr*dr)
					{
						fail = true;
						break;
					}
				}
				if(fail) break;
			}
			if(!fail)
			{
				for(int j = 0;j < N;j++)
				{
					printf("%.10f %.10f ",x[j],y[j]);
				}
				putchar('\n');
				fprintf(stderr,"Case #%d Ok! At %d Round\n",TKN,i);
				break;
			}
		}
	}
	while(getchar() != EOF);
	return 0;
}
