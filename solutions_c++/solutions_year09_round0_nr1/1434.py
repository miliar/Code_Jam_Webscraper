#include <cstdio>
#include<stdlib.h>
#include<string.h>
#include<cmath>
#include<algorithm>
#include<string>
#include<vector>
#include<iostream>
using namespace std;

#define DEBUG 0

struct Dictionary
{
	char word[20];
	bool valid;
}dic[6000];

vector<char> words[20];
int L, D, N, num_count;

void parse(int idx)
{
	char c;

	scanf("%c", &c);
	if(c == '(')
	{
		while(1)
		{
			scanf("%c", &c);
			if(c == ')') break;
			words[idx].push_back(c);
		}
	}
	else
		words[idx].push_back(c);
}

bool isMatch(char c, int idx)
{
	for(int i = 0; i < words[idx].size(); i++)
		if(c == words[idx].at(i))
			return 1;
	return 0;
}

int main()
{
	freopen("A-large.in","r",stdin);
	//freopen("A-small.in","r",stdin);

#if !DEBUG
	freopen ("A-large.out","w",stdout);
#endif

	scanf("%d %d %d\n", &L, &D, &N);

	for(int i = 0; i < D; i++)
		scanf("%s", dic[i].word);

	for(int i = 1; i <= N; i++)
	{
		scanf("\n");
		num_count = 0;

		for(int j = 0; j < D; j++)
			dic[j].valid = 1;

		for(int j = 0; j < L; j++)
			words[j].clear();

		for(int j = 0; j < L; j++)
			parse(j);

		for(int j = 0; j < L; j++)
		{
			for(int k = 0; k < D; k++)
				if(dic[k].valid && !isMatch(dic[k].word[j], j))
					dic[k].valid = 0;
		}

		for(int j = 0; j < D; j++)
			if(dic[j].valid)
				num_count++;
		printf("Case #%d: %d\n", i, num_count);
	}

	

#if !DEBUG
	fclose (stdout);
#endif

	return 0;
}