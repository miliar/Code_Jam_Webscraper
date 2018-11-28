#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int N,S,Q,change,remain;

char engines[100][102];
bool ben[100];

void clean()
{
	int i;
	remain = S;
	for (i=0;i<100;++i)
		ben[i] = false;
}

void mark(int i)
{
	if (ben[i]== false)
	{
		--remain;
		if (remain==0)
		{
			clean();
			--remain;
			++change;
		}
		ben[i]=true;
	}
}

int find(char *q)
{
	int i;
	for (i=0;i<S;++i)
		if (strcmp(engines[i],q)==0)
			return i;
	return -1;
}

void main()
{
	FILE *f;
	FILE *o;
	int i,j;
	char query[1000];
	f=fopen("A-large.in","rt");
	o=fopen("A-large.out","wt");
	fscanf(f,"%d\n",&N);
	for (i=0;i<N;++i)
	{
		fscanf(f,"%d\n",&S);
		for (j=0;j<S;++j)
		{
			fgets(engines[j],101,f);
			while (engines[j][strlen(engines[j])-1]==0x0A || engines[j][strlen(engines[j])-1]==0x0D)
			{
				engines[j][strlen(engines[j])-1] = 0;
			}
		}
		fscanf(f,"%d\n",&Q);
		clean();
		change=0;
		for (j=0;j<Q;++j)
		{
			fgets(query,101,f);
			while (query[strlen(query)-1]==0x0A || query[strlen(query)-1]==0x0D)
			{
				query[strlen(query)-1] = 0;
			}
			int f = find(query);
			if (f>=0)
				mark(f);
		}
		fprintf(o,"Case #%d: %d\n",i+1,change);
	}
	fclose(f);
	fclose(o);
}