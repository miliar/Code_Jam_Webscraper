#include <iostream>
#include <fstream>
#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>
#include <sstream>
#define MAX 1000
using namespace std;
int N,M;
char exist[100010][MAX];
char make[101][MAX];
int solve(int index)
{
	char tmp[MAX]={0};
	int i,sum=0,j;
	for (i=0; i<N; ++i)
	{
		if (strcmp(make[index],exist[i]) == 0) return 0;
	}
	for (i=0; i<strlen(make[index]); ++i)
	{
		if (make[index][i] == '/')
			sum++;
	}
	for (i=1; i<strlen(make[index]); ++i)
	{
		if (make[index][i] == '/')
		{
			memcpy(tmp,make[index],i);
			for (j=0; j<N; ++j)
			{
				if (strcmp(tmp,exist[j]) == 0) 
				{
					sum--;
					break;
				}				
			}
			memcpy(exist[N],tmp,strlen(tmp));
			N++;
		}
	}
	memcpy(exist[N],make[index],strlen(make[index]));
	N++;
	return sum;
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("small1.txt", "w", stdout);
	int nt, it;
	int i,j;
	unsigned int sum;
	scanf("%d", &nt);
	for (it = 1; it <= nt; it++)
	{
		sum = 0;
		memset(exist,0,sizeof(exist));
		memset(make,0,sizeof(make));
		scanf("%d%d\n",&N,&M);
		for (i=0; i<N; ++i)
		{
			gets(exist[i]);
		}
		
		for (i=0; i<M; ++i)
		{
			gets(make[i]);
			sum += solve(i);
			if (N > 100010) printf("!!!!!!!!!!!");
		}
		printf("Case #%d: %d\n",it,sum);
	}
	return 0;
}