#include "stdlib.h"
#include "stdio.h"
#include <algorithm>
using namespace std;

#define MAXN 100
#define ORANGE 0
#define BLUE 1

int T, N;
int b[MAXN][2];
bool o[MAXN];
int bcnt[2];

void read_case(int t)
{
	char col;
	int pos;
	
	//printf("Case %d\n",t);
	
	b[0][ORANGE]=1; b[0][BLUE]=1;
	bcnt[ORANGE]=1; bcnt[BLUE]=1;
	
	scanf("%d\n",&N);
	for (int i=0; i<N; i++)
	{
		scanf("%c %d ",&col,&pos);
		//printf("%c %d\n",col,pos);
		if (col=='O')
		{
			o[i]=ORANGE;
			b[bcnt[ORANGE]++][ORANGE] = pos;
		}
		else
		{
			o[i]=BLUE;
			b[bcnt[BLUE]++][BLUE] = pos;
		}
	}
	/*
	for (int i=0; i<bcnt[ORANGE]; i++)
		printf("%d ",b[i][ORANGE]);
		printf("\n");
	for (int i=0; i<bcnt[BLUE]; i++)
		printf("%d ",b[i][BLUE]);
		printf("\n");
	*/
}

int solve()
{
	int t[2];
	int cost, diff,total(0);
	t[ORANGE]=1; t[BLUE]=1;
	
	for (int i=0; i<N; i++)
	{
		if (o[i]==ORANGE)
		{
			cost = max(b[t[ORANGE]][ORANGE] - b[t[ORANGE]-1][ORANGE], -b[t[ORANGE]][ORANGE] + b[t[ORANGE]-1][ORANGE]) + 1;
			diff = b[t[BLUE]][BLUE] - b[t[BLUE]-1][BLUE];
			if (diff > 0)
				b[t[BLUE]-1][BLUE] += min (diff,cost);
			else
				b[t[BLUE]-1][BLUE] -= min (-diff,cost);
			t[ORANGE]++;
		}
		else
		{
			cost = max(b[t[BLUE]][BLUE] - b[t[BLUE]-1][BLUE], -b[t[BLUE]][BLUE] + b[t[BLUE]-1][BLUE]) + 1;
			diff = b[t[ORANGE]][ORANGE] - b[t[ORANGE]-1][ORANGE];
			if (diff > 0)
				b[t[ORANGE]-1][ORANGE] += min (diff,cost);
			else
				b[t[ORANGE]-1][ORANGE] -= min (-diff,cost);
			t[BLUE]++;
		}
		//printf("%d : %d  -  pos[ORANGE]=%d, pos[BLUE]=%d\n",o[i],cost,b[t[ORANGE]-1][ORANGE],b[t[BLUE]-1][BLUE]);
		total += cost;	
	}
	return total;
}

int main()
{
	scanf("%d\n",&T);
	for (int i=0; i<T; i++)
	{
		read_case(i);
		printf("Case #%d: %d\n",i+1,solve());
	}
	return 0;
}
