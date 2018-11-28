#include <iostream>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cmath>
#include <vector>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <string>
#define SET(p) memset(p,-1,sizeof(p))
#define CLR(p) memset(p,0,sizeof(p))
#define LL long long int
#define ULL unsigned long long int
#define S(n)					scanf("%d",&n)
#define Sl(n)					scanf("%lld",&n)
#define Sf(n) 					scanf("%lf",&n)
#define Ss(n) 					scanf("%s",n)
using namespace std;
char str[10][10];
bool win(char c)
{
	int i,j,k;
	//check horizontal
	for(i=0;i<4;i++)
	{
		int cn=0,t=0;
		for(j=0;j<4;j++)
		{
			if(str[i][j]==c)
			cn++;
			else if(str[i][j]=='T')
			t++;
		}
		if(cn==4||(cn==3&&t==1))
		return true;
	}
	
	for(j=0;j<4;j++)
	{
		int cn=0,t=0;
		for(i=0;i<4;i++)
		{
			if(str[i][j]==c)
			cn++;
			else if(str[i][j]=='T')
			t++;
		}
		if(cn==4||(cn==3&&t==1))
		return true;
	}
	
		int cn=0,t=0;
	for(i=0;i<4;i++)
	{
		
			if(str[i][i]==c)
			cn++;
			else if(str[i][i]=='T')
			t++;
		
	
	}
	if(cn==4||(cn==3&&t==1))
	return true;
	
	cn=0,t=0;
	
	for(i=0;i<4;i++)
	{
		
			if(str[i][3-i]==c)
			cn++;
			else if(str[i][3-i]=='T')
			t++;
		
	
	}
	if(cn==4||(cn==3&&t==1))
	return true;
	
	return false;
	
}
bool allfilled()
{
	int i,j,k;
	for(i=0;i<4;i++)
	for(j=0;j<4;j++)
	if(str[i][j]=='.')
	return false;
	
	return true;
}
int main()
{
	int i,j,k,l,m,n,t;
	#ifndef ONLINE_JUDGE
	freopen("test2.in","r",stdin);
	freopen("op1.txt","w",stdout);
	#endif
	S(t);
	k=1;
	while(t--)
	{
		for(i=0;i<4;i++)
		Ss(str[i]);
		
		if(win('X'))
		printf("Case #%d: X won\n",k++);
		else if(win('O'))
		printf("Case #%d: O won\n",k++);
		else if(allfilled())
		printf("Case #%d: Draw\n",k++);
		else
		printf("Case #%d: Game has not completed\n",k++);	
		
	}
	return 0;
}
