#include<ctime>
#include<cstdio>
#include<vector>
#include<string>
#include<climits>
#include<cstdlib>
#include<cstddef>
#include<string.h>
#include<iostream>
#include<algorithm>
#define LL long long
#define _max(a, b) ((a) > (b) ? (a) : (b))
#define _min(a, b) ((a) < (b) ? (a) : (b))
using namespace std;

int t;
char s[11111];
char d[] = {
'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 
'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w',
'j', 'p', 'f', 'm', 'a', 'q'};
int main()
{
//*
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
//*/
	scanf("%d\n", &t);
	for (int test = 1; test <= t; test++, puts(""))
	{
		gets(s);
		int n = strlen(s);
		printf("Case #%d: ", test);
		for (int i = 0; i < n; i++)
			printf("%c", s[i] == ' ' ? ' ' : d[s[i] - 'a']);
	}
	return 0;
}
