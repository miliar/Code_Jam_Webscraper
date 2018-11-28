#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <deque>

using namespace std;

const int MAXN = 10005;
int value[MAXN];
struct Node
{
	bool And , canchange;
};

Node node[MAXN];
int m , v; 

int Dp[2][MAXN];

void DFS(int root)
{
	if(root * 2 > m)
	{
		Dp[value[root]][root] = 0 ;
		Dp[1-value[root]][root] = -1;
		return ;
	}
	DFS(2*root);
	DFS(2*root+1);
	Dp[0][root] = Dp[1][root] = INT_MAX;
	int la , lb , ra , rb;
	la = Dp[0][2*root];
	lb = Dp[1][2*root];
	ra = Dp[0][2*root+1];
	rb = Dp[1][2*root+1] ;
	if(node[root].And == true)
	{
		if(la != -1 && ra != -1)
		{
			if(Dp[0][root] > la + ra)
				Dp[0][root] = la + ra ;
		}
		if(la != -1 && rb != -1)
		{
			if(Dp[0][root] > la + rb)
				Dp[0][root] = la + rb ;
		}
		if(lb != -1 && ra != -1)
		{
			if(Dp[0][root] > lb + ra)
				Dp[0][root] = lb + ra ;
		}
		if( lb != -1 && rb != -1)
		{
			if(Dp[1][root] > lb + rb)
				Dp[1][root] = lb + rb ;
		}
	}
	else
	{
		if(la != -1 && ra != -1)
		{
			if(Dp[0][root] > la + ra)
				Dp[0][root] = la + ra ;
		}
		if(la != -1 && rb != -1)
		{
			if(Dp[1][root] > la + rb)
				Dp[1][root] = la + rb ;
		}
		if(lb != -1 && ra != -1)
		{
			if(Dp[1][root] > lb + ra)
				Dp[1][root] = lb + ra ;
		}
		if( lb != -1 && rb != -1)
		{
			if(Dp[1][root] > lb + rb)
				Dp[1][root] = lb + rb ;
		}
	}
	if(node[root].canchange == true)
	{
		if(node[root].And == true)
		{
			if(la != -1 && ra != -1)
			{
				if(Dp[0][root] > la + ra + 1)
					Dp[0][root] = la + ra + 1;
			}
			if(la != -1 && rb != -1)
			{
				if(Dp[1][root] > la + rb + 1)
					Dp[1][root] = la + rb + 1;
			}
			if(lb != -1 && ra != -1)
			{
				if(Dp[1][root] > lb + ra + 1)
					Dp[1][root] = lb + ra + 1;
			}
			if( lb != -1 && rb != -1)
			{
				if(Dp[1][root] > lb + rb + 1)
					Dp[1][root] = lb + rb + 1;
			}
		}
		else
		{
			if(la != -1 && ra != -1)
			{
				if(Dp[0][root] > la + ra + 1)
					Dp[0][root] = la + ra +1;
			}
			if(la != -1 && rb != -1)
			{
				if(Dp[0][root] > la + rb + 1)
					Dp[0][root] = la + rb + 1;
			}
			if(lb != -1 && ra != -1)
			{
				if(Dp[0][root] > lb + ra + 1)
					Dp[0][root] = lb + ra+ 1 ;
			}
			if( lb != -1 && rb != -1)
			{
				if(Dp[1][root] > lb + rb + 1)
					Dp[1][root] = lb + rb + 1;
			}
		}
	}
	if(Dp[0][root] == INT_MAX) Dp[0][root] = -1;
	if(Dp[1][root] == INT_MAX) Dp[1][root] = -1;
}
int main(void)
{
	int cases ;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("111.txt","w",stdout);
	scanf("%d",&cases);
	int i ,j ;
	int f = 0 ; 
	while( cases -- )
	{
		memset(value,-1,sizeof(value));
		int a , b;
		scanf("%d %d",&m,&v);
		for(i = 1; i <= (m - 1)/2 ; i ++)
		{
			scanf("%d %d",&a,&b);
			if(a == 1)
				node[i].And = 1;
			else
				node[i].And = 0;
			if(b == 1)
				node[i].canchange = 1;
			else
				node[i].canchange = 0;
		}
		for(i = (m - 1) /2 + 1 ; i <= m ; i ++)
			scanf("%d",&value[i]);
		DFS(1);
		printf("Case #%d:",++f);
		if(Dp[v][1] == -1)
			printf(" IMPOSSIBLE\n");
		else
			printf(" %d\n",Dp[v][1]);
	}
	return 0;
}