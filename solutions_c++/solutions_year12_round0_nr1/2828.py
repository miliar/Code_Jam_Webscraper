#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>
using namespace std;

int i,j,k;
int T;
int ans;
char G[1000];
char S[1000];

char trans[30];
char g[3][125] = {	"ejp mysljylc kd kxveddknmc re jsicpdrysi",
					"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
					"de kr kd eoya kw aej tysr re ujdr lkgc jv"};
char s[3][125] = {	"our language is impossible to understand",
					"there are twenty six factorial possibilities",
					"so it is okay if you want to just give up"};

void make_trans()
{
	memset(trans,-1,sizeof(trans));
	trans['y'-'a'] = 'a';
	trans['e'-'a'] = 'o';
	trans['q'-'a'] = 'z';
	trans['z'-'a'] = 'q';

	int i,j,k;
	for(i=0;i<3;i++)
	{
		for(j=0;g[i][j] != '\0'; j++)
		{
			if(trans[g[i][j] - 'a'] > 0) continue;

			trans[g[i][j] - 'a'] = s[i][j];
		}
	}
}

void trans_it()
{
	int m,n;
	for(m=0;G[m] != '\0';m++)
		S[m] = trans[G[m] - 'a'];
	S[m] = '\0';
}

int main( )
{
	freopen( "A-small.in", "r", stdin );
	freopen( "A-small.out", "w", stdout );

	make_trans();

	scanf("%d",&T);
	gets(G);
	for(i=1;i<=T;i++)
	{
		gets(G);
		printf("Case #%d: ",i);
		trans_it();
		//puts(G);
		puts(S);
		//printf("%s\n",S);
	}

	return 0;
}
