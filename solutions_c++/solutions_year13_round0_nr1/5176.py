#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <string>
using namespace std;
#define LL long long
#define maxn 210
#define maxe 101010
#define INF 1e40
#define fi first
#define se second
#define mp make_pair
#define pi acos(-1.0)
char g[5][5];
int jud(char c)
{
	int i,j,a1=0,b1=0,a2=0,b2=0;
	for(i=0;i<4;i++)
	{
		if(g[i][i]==c) a1++;
		if(g[i][i]=='T') b1++;
		if(g[i][3-i]==c) a2++;
		if(g[i][3-i]=='T') b2++;
	}
	if(a1==4||(a1==3&&b1==1)) return 1;
	if(a2==4||(a2==3&&b2==1)) return 1;
	for(i=0;i<4;i++)
	{
		int a=0,b=0;
		for(j=0;j<4;j++)
		{
			if(g[i][j]==c) a++;
			if(g[i][j]=='T') b++;
		}
		if(a==4||(a==3&&b==1)) return 1;
	}
	for(i=0;i<4;i++)
	{
		int a=0,b=0;
		for(j=0;j<4;j++)
		{
			if(g[j][i]==c) a++;
			if(g[j][i]=='T') b++;
		}
		if(a==4||(a==3&&b==1)) return 1;
	}
	return 0;
}
int main()
{
	int i,j,tt=0,ncase,v;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&ncase);
	while(ncase--)
	{
		for(i=0;i<4;i++)
			scanf("%s",g[i]);
		int ff=0;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				if(g[i][j]=='.')
					ff=1;
		printf("Case #%d: ",++tt);
		if(jud('X'))
			puts("X won");
		else if(jud('O'))
			puts("O won");
		else if(!ff) 
			puts("Draw");
		else
			puts("Game has not completed");
	}
}