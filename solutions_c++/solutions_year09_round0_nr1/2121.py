// cpptest.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <vector>
#include <algorithm>
using namespace std;

const int L = 15;
const int D = 5000;
const int N = 500;

int words[D][L];

int l, d, n;

void Work(int cn)
{
	printf("Case #%d: ", cn);
	int cnt = 0;
	char str[50000];
	scanf("%s", str);
	int len = strlen(str);
	int j = 0, i = 0;
	int pat[L];
	memset(pat, 0, sizeof(pat));
	while(str[i])
	{
		if(str[i] == '(')
		{
			++i;
			while(str[i] != ')')
			{
				pat[j] |= 1<<(str[i]-'a');
				++i;
			}
		} else {
			pat[j] |= 1<<(str[i]-'a');
		}
		++i;
		++j;
	}

		//for (int j = 0; j < l; ++j)
		//	printf("%d", pat[j]);
		//putchar('\n');
	
	for	(i = 0; i < d; ++i)
	{
		for	(j = 0; j < l; ++j)
		{
			if((words[i][j] & pat[j]) != words[i][j])
				break;
		}
		if(j == l)
			++cnt;
	}
	printf("%d\n", cnt);
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	
	char str[L];
	scanf("%d%d%d", &l, &d, &n);
	for	(int i = 0; i < d; ++i)
	{
		scanf("%s", str);
		for	(int j = 0; j < l; ++j)
		{
			words[i][j] = 1<<(str[j]-'a');
		}
	}
	//for	(int i = 0; i < d; ++i)
	//{
	//	for (int j = 0; j < l; ++j)
	//		printf("%d", words[i][j]);
	//	putchar('\n');
	//}
	for	(int i = 0; i < n; ++i)
	{
		Work(i+1);
	}

	return 0;
}



