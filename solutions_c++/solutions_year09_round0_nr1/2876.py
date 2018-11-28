#include <iostream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define L_MAX 30
#define D_MAX 6000
#define N_MAX 10000

using namespace std;

char text[D_MAX][L_MAX]={'\0'}, N_text[1000][N_MAX]={'\0'}, L_text[L_MAX][1000]={'\0'};

bool comp(int, int, int);
void cut(int);

int main()
{
	int L, D, N, cont;
	int i, j, k;
	
	scanf(" %d%d%d", &L, &D, &N);

	for(i=0 ; i<D ; i++)
		scanf(" %s", text[i]);

	for(i=0 ; i<N ; i++)
		scanf("%s", N_text[i]);

	for(i=0 ; i<N ; i++)
	{
		cont = 0;
		cut(i);
		for(j=0 ; j<D ; j++)
		{
			if(comp(L, j, i))
				cont++;
		}	

		printf("Case #%d: %d\n", i+1, cont);
		for(j=0; j<L_MAX; j++)
			for(k=0; k<L_MAX; k++)
				L_text[j][k]='\0';
	}

	return 0;
}

void cut(int cutN)
{
	int len, i, pot, j, k;
	len = strlen(N_text[cutN]);
	pot=0;
	j=0;
	k=0;
	for(i=0; i<len; i++)
	{
		if(N_text[cutN][i]=='(')
		{
			pot=1;
			continue;
		}
		if(pot==1)
		{
			L_text[j][k++] = N_text[cutN][i];
			if(N_text[cutN][i+1]==')')
			{
				pot=0;
				j++;
				k=0;
			}
		}
		else
		{
			if(N_text[cutN][i]==')')
				continue;
			else
				L_text[j++][k] = N_text[cutN][i];
		}
	}

}

bool comp(int L, int indexT, int indexN)
{
	int i, j, cont, len;
	cont=0;
	for(i=0; i<L; i++)
	{
		len = strlen(L_text[i]);
		for(j=0 ; j<len ; j++)
		{
			if(L_text[i][j] == text[indexT][i])
				cont++;
		}
	}

	if(cont==L)	return true;
	else return false;
}