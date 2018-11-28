#include<iostream>
#include<queue>
#include<new>
#include<cstdio>
#include<algorithm>
#include<list>
#include<vector>
#include<map>
#include<utility>
#include<cstring>
#include<climits>
#include<cmath>
#include<stack>
using namespace std;

int count(int a, int b)
{
	int pairs = 0;
	int i;
	int n;
	int m;
	int j, k, l;
	int len;
	char ctemp;
	char sn[100], sm[100], temp[100];
	for(i = a; i <= b; i++)
	{
		sprintf(sn, "%d", i);
		len = strlen(sn);
		n = i;
		strcpy(sm, sn);
		do
		{
			ctemp = sm[0];
			for(j = 0;j < len - 1; j++)
			{
				sm[j] = sm[j+1];
			}
			sm[j] = ctemp;//temp[0];
			sm[j+1] = '\0';
			m = atoi(sm);
			sprintf(temp, "%d", m);
			if(strlen(temp) == len && m > n && m <= b)
			{
				pairs++;
			}
		}
		while(strcmp(sn, sm) != 0);
	}
//	pairs /= 2;
	return pairs;
}

int main()
{
	int T, I, a, b, pairs;
	scanf("%d", &T);
	for(I = 1; I < T + 1; I++)
	{
		scanf("%d %d", &a, &b);
		pairs = count(a, b);
		printf("Case #%d: %d\n", I, pairs);
	}
}
