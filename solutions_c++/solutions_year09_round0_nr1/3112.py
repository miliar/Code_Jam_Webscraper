#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;

#define DMAX 5000
#define LMAX 15
char words[DMAX][LMAX+1];
char patterns[LMAX][26];
int L, D, N;

void init()
{
	for(int i=0;i<LMAX; i++)
	{
		for(int j=0;j<26;j++)
			patterns[i][j] = 0;
	}
}

void create_pattern(char *ipattern)
{
	//memset(patterns, 0, LMAX*26);
	init();
	int pos = 0;
	char *p = ipattern;
	bool state = false;
	while(*p)
	{
		if(*p == '(')
			state = true;
		else if(*p == ')')
		{
			state = false;
			pos++;
		}
		else
		{
			patterns[pos][*p - 'a'] = 1;
			if(!state)
				pos++;
		}
		p++;
	}
}

int match_count(char ipattern[])
{	
	create_pattern(ipattern);
	int count = 0;
	for(int i=0;i<D;i++)
	{
		char *p = words[i];
		int pos = 0;
		while(*p)
		{
			if(patterns[pos][*p - 'a'] != 1)
				break;
			p++;
			pos++;
		}
		if(*p == '\0') 
			count++;
	}
	return count;
}

int main()
{
	scanf("%d %d %d", &L, &D, &N);
	for(int i=0;i<D;i++)
	{
		scanf(" %[abcdefghijklmnopqrstuvwxyz]", words[i]);
	}
	for(int i=0;i<N;i++)
	{
		char Test[500];
		scanf(" %[^\n]",Test);
		printf("Case #%d: %d\n", i+1, match_count(Test));
	}
	return 0;
}

