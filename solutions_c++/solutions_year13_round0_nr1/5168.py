#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <list>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <climits>
#include <ctime>

#define pb       	push_back
#define fi       	first
#define se       	second
#define KARE(a)	 	( (a)*(a) )
#define MAX3(a,b,c)	( MAX( a,MAX(b,c) ) )
#define inf		 	1000000000
#define eps      	(1e-9)
#define esit(a,b)  	( abs( (a)-(b) ) < eps )
#define SET(A,b) memset(A,b,sizeof (A) )
#define SIZE(A) ((int)(A).size())
#define yeral() (node *)calloc(1,sizeof(node))
#define dbg(x) cerr<<#x<<":"<<x<<endl

using namespace std;

typedef long long int lint;
typedef pair<int,int> ii;

int T,X,pl1,pl2;
char mat[10][10];
int search(char ch)
{
	int pl=0;
	for(int i=1;i<=4;i++)
	{
		X=0;
		for(int j=1;j<=4;j++)
			if(mat[i][j]==ch || mat[i][j]=='T')
				X++;
		if(X==4)
			pl=1;
	}
	//~ printf("C=%c %d\n",ch,pl);
	for(int i=1;i<=4;i++)
	{
		X=0;
		for(int j=1;j<=4;j++)
			if(mat[j][i]==ch || mat[j][i]=='T')
				X++;
		if(X==4)
			pl=1;
	}
	X=0;
	//~ printf("C=%c %d\n",ch,pl);
	for(int i=1;i<=4;i++)
		if(mat[i][i]==ch || mat[i][i]=='T')
			X++;
	if(X==4)
		pl=1;
	X=0;
	for(int i=1;i<=4;i++)
		if(mat[i][5-i]==ch || mat[i][5-i]=='T')
			X++;
	if(X==4)
		pl=1;
	//~ printf("C=%c %d\n",ch,pl);
	return pl;
}
int main()
{
	freopen("oku.txt","r",stdin);
	freopen("yaz.txt","w",stdout);
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
				scanf(" %c",&mat[i][j]);
		pl1=search('X');
		pl2=search('O');
		if(pl1)
			printf("Case #%d: X won",tt);
		else if(pl2)
			printf("Case #%d: O won",tt);
		else 
		{
			int fl=1;
			for(int i=1;fl && i<=4;i++)
				for(int j=1;fl && j<=4;j++)
					if(mat[i][j]=='.')
					{
						printf("Case #%d: Game has not completed",tt);
						fl=0;
					}
			if(fl)
				printf("Case #%d: Draw",tt);
		}
		if(tt<T)
			puts("");
	}
}
