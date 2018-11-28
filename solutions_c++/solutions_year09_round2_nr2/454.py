#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

void next(char *m)
{
	char n[100];
	strcpy(n,m);
	int s = strlen(n);	
	int i;
	next_permutation(n,n+s);
	if (strcmp(m,n)<0) 
	{
		strcpy(m,n);
		return;
	}
	n[s] = '0';
	n[s+1] = 0;
	s++;
	sort(n,n+s);
	for (i=1; i<s; i++)
	{
		if (n[i] != '0') 
		{
			n[0] = n[i];
			n[i] = '0';
			strcpy(m,n);
			return;
		}
	}
	return;
}

int main()
{
	int t;
	char number[30];
	scanf("%d",&t);

	for(int i=0; i<t; i++)
	{
		scanf("%s",number);
		next(number);
		printf("Case #%d: %s\n",i+1,number);
	}

	return 0;
}
