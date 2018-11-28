#include <stdio.h>
#include<limits.h>
#include<stdlib.h>
#include<string.h>

int n;
int seanz;
char se[101][100];
int qanz;
int q[1000];

int dyn[1001][101];

void initdyn()
{
	int i,j;
	for(i=0; i<1001; i++)
	{
		for(j=0; j<101; j++)
		{
			dyn[i][j]=-1;
		}
	}
}

void readdata()
{
	int i,j;
	char tmp[101];
	scanf("%d\n", &seanz);
	for(i=0; i<seanz; i++)
	{
		gets(se[i]);
	}
	scanf("%d\n", &qanz);
	for(i=0; i<qanz; i++)
	{
		gets(tmp);
		for(j=0; j<seanz; j++)
		{
			if(strcmp(tmp,se[j])==0)
			{
				q[i] = j;
				break;
			}
		}
	}
}

int getMin(int pos, int actse)
{
	int i,j;

	if(dyn[pos][actse]!=-1)
	{
		return dyn[pos][actse];
	}

	if(pos==qanz)
		return 0;

	if(actse!=q[pos])
	{
		dyn[pos][actse] = getMin(pos+1, actse);
		return dyn[pos][actse];
	}

	int actmin=INT_MAX;
	for(i=0; i<seanz; i++)
	{
		if(i!=actse)
		{
			int actv = 1+getMin(pos+1, i);
			if(actv<actmin)
				actmin = actv;
		}
	}
	dyn[pos][actse] = actmin;
	return actmin;
}

int main()
{
	int i,j,k,l;
	scanf("%d", &n);

	for(i=0; i<n; i++)
	{
		initdyn();
		readdata();

		int actmin = INT_MAX;
		for(j=0; j<seanz; j++)
		{
			int actv = getMin(0,j);
			if(actv<actmin)
				actmin = actv;
			if(actv == 0)
				break;
		}

		// Result Output
		printf("Case #%d: %d\n", i+1, actmin);
	}

	return 0;
}
