#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

int pattens[15][26];
char words[5000][16];
char s[1000000];
int L, D, N;

int getac(char *pattern)
{
	memset(pattens, 0, sizeof(pattens));

	int pos = 0;
	int kh = 0;
	for (char *ptr = pattern; *ptr; ptr++)
	{
		if (kh)
		{
			if (*ptr == ')') kh = 0, pos++;
			else pattens[pos][*ptr-'a'] = 1;
		}
		else
		{
			if (*ptr == '(') kh = 1;
			else pattens[pos][*ptr-'a'] = 1, pos++;
		}
	}

	int ret = 0;
	for (int i =0 ; i < D; i++)
	{
		int j = 0; 
		for (; j < L; j++)
			if (!pattens[j][words[i][j]-'a']) break;
		if (j == L) ret++;
	}
	
	return ret;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.txt", "w", stdout);

	int T = 0;
	scanf("%d%d%d", &L, &D, &N);
	gets(s);
	for (int i = 0; i < D; i++) gets(words[i]);
	for (int i = 0; i < N; i++)
	{
		gets(s);
		printf("Case #%d: %d\n", ++T, getac(s));
	}
	return 0;
}

