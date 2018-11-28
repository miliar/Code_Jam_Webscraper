/*
ID: linjd821
LANG: C++
TASK: 
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include <ctype.h>
#include <map>
#include <string>
#include <set>
#include <bitset>
#include <utility>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <iostream>
#include <fstream>
#include <list>

using  namespace  std;

struct  Node  
{
	char  num[100];
}a[100];

int  N;
bool over(int p)
{
	int i;
	for(i = p+1; i < N; i++)
		if(a[p].num[i] == '1') return 1;
	return 0;
}

void change(int st, int ed)
{
	int  i;
	struct Node tmp = a[ed];
	for(i = ed; i > st; i--)
		a[i] = a[i-1];
	a[st] = tmp;
}

bool OK(int st, int ed)
{
	int  i;
	for(i = st+1; i < N; i++)
		if(a[ed].num[i] == '1') return 0;
	return  1;
}
int main()
{
	int  T, CAS = 1;
	int  i, j;
	//freopen("A2.in", "r", stdin);
	//freopen("A2.out", "w", stdout);
	scanf("%d", &T);
	while(T--)
	{
		scanf("%d", &N);
		for(i = 0; i < N; i++)
			scanf("%s", &a[i].num);
		int  ans = 0;
		for(i = 0; i < N; i++)
		{
			if(over(i))
			{
				for(j = i+1; j < N; j++)
				{
					if(OK(i, j))
					{
						change(i, j);
						ans += j-i;	
						break;
					}
				}
			}
		}
		printf("Case #%d: %d\n", CAS++,ans);
	}
	return  0;
}
