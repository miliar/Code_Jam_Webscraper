#include <stdio.h>
#include <iostream>
#include <string>
#include <string.h>
#include <map>
#define MAXENGINES 105
#define MAXQUERIES 1005

using namespace std;

int ncases, nengines, nqueries, iqueries[MAXQUERIES], table[MAXQUERIES][MAXENGINES];
string engines[MAXENGINES], queries[MAXQUERIES];
map<string,int> m;

int gotable()
{
	int i, j, min1=0, min2=0, m1=10000, m2=10000;
	memset(table, 0, MAXQUERIES*MAXENGINES*sizeof(int));
	for(i=nqueries-1; i>=0; i--)
	{
		for(j=0; j<nengines; j++)
		{
			if(iqueries[i]==j) //switch
			{
				if(min1==min2)
					table[i][j]=min1+1;
				else 
				{
					if(table[i+1][j]==min1)
						table[i][j]=min2+1;
					else
						table[i][j]=min1+1;
				}
			}
			else
			{
				table[i][j]=table[i+1][j];
			}
			if(table[i][j]<m1)
			{
				m2=m1;
				m1=table[i][j];
			}
			else if(table[i][j]<m2)
				m2=table[i][j];
		}
		min1=m1, min2=m2, m1=10000, m2=10000;
	}
	return min1;
}

int main()
{
	int i, j;
	scanf("%d", &ncases);
	for(i=0; i<ncases; i++)
	{
		scanf(" %d ", &nengines);
		for(j=0; j<nengines; j++)
		{
			getline(cin, engines[j]);
			m[engines[j]]=j;
		}
		scanf("%d ", &nqueries);
		for(j=0; j<nqueries; j++)
		{
			getline(cin, queries[j]);
			iqueries[j]=m[queries[j]];
		}
		printf("Case #%d: %d\n", i+1, gotable());
	}
	return 0;
}
