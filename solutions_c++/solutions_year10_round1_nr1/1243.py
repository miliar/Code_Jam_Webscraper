#include<math.h> 
#include "stdafx.h"
#include<ctype.h>
#include<stdlib.h> 
#include<stack>
#include<queue> 
#include<list>
#include<map>

#include<string.h> 
#include<algorithm> 
#include<iostream>
#include<sstream> 
#include<vector> 
#include<string> 

using namespace std; 

#define vi vector<int>
#define vd vector<double>
#define vs vector<string>
#define fo(i,j,n) for(i=j;i<n;++i)
#define foo(i,j,v) for(i=j;i<v.size();++i)
#define Fo(i,j,n) for(i=n-1;i>=j;--i)
#define li(v) v.begin(),v.end()
#define co continue;
#define re return 
#define max(a,b) ((a>b) ? a : b)

#define min(a,b) ((a<b) ? a : b)
#define max(a,b) ((a>b) ? a : b)

#define inf 55
#define pi (2*acos(0))
#define eps 1e-9
typedef __int64 Long;

char g[inf][inf];
int N,K,blue,red;

void call()
{
	int i,j,k,b=0,r=0;
	fo(i,0,N)
	{
		b=r=0; j = 0;
		if(g[i][j]=='B')b++;else if(g[i][j]=='R')r++;
		fo(j,1,N)
		{
			if(g[i][j]!=g[i][j-1])b=r=0;
			if(g[i][j]=='B')b++; else if(g[i][j]=='R')r++;
			if(b>=K)blue=1; else if(r>=K)red = 1;
		}
	}
	
	fo(j,0,N)
	{
		b=r=0; i = 0;
		if(g[i][j]=='B')b++;else if(g[i][j]=='R')r++;
		fo(i,1,N)
		{
			if(g[i][j]!=g[i-1][j])b=r=0;
			if(g[i][j]=='B')b++; else if(g[i][j]=='R')r++;
			if(b>=K)blue=1; else if(r>=K)red = 1;
		}
	}
	//1
	fo(k,0,N)
	{
		i = 0; j = k; b=r=0;
		if(g[i][j]=='B')b++;else if(g[i][j]=='R')r++;
		++i; --j;
		while((i>=0) && (i<N) && (j>=0) && (j<N) )
		{
			if(g[i][j]!=g[i-1][j+1])b=r=0;
			if(g[i][j]=='B')b++; else if(g[i][j]=='R')r++;
			if(b>=K)blue=1; else if(r>=K)red = 1;
			++i; --j;
		}
	}
	//2
	fo(k,0,N)
	{
		i = k; j = N-1; b=r=0;
		if(g[i][j]=='B')b++;else if(g[i][j]=='R')r++;
		++i; --j;
		while((i>=0) && (i<N) && (j>=0) && (j<N) )
		{
			if(g[i][j]!=g[i-1][j+1])b=r=0;
			if(g[i][j]=='B')b++; else if(g[i][j]=='R')r++;
			if(b>=K)blue=1; else if(r>=K)red = 1;
			++i; --j;
		}
	}
	//3
	Fo(k,0,N)
	{
		i = 0; j = k; b=r=0;
		if(g[i][j]=='B')b++;else if(g[i][j]=='R')r++;
		++i; --j;
		while((i>=0) && (i<N) && (j>=0) && (j<N) )
		{
			if(g[i][j]!=g[i-1][j-1])b=r=0;
			if(g[i][j]=='B')b++; else if(g[i][j]=='R')r++;
			if(b>=K)blue=1; else if(r>=K)red = 1;
			++i; ++j;
		}
	}
	//4
	fo(k,1,N)
	{
		i = k; j = 0; b=r=0;
		if(g[i][j]=='B')b++;else if(g[i][j]=='R')r++;
		++i; --j;
		while((i>=0) && (i<N) && (j>=0) && (j<N) )
		{
			if(g[i][j]!=g[i-1][j-1])b=r=0;
			if(g[i][j]=='B')b++; else if(g[i][j]=='R')r++;
			if(b>=K)blue=1; else if(r>=K)red = 1;
			++i; ++j;
		}
	}
}
int main()
{
	freopen("c://Codejam//A.in","r",stdin);
	freopen("c://Codejam//A.out","w",stdout);
	int T,t,i,j,k;
	scanf("%d",&T); 
	fo(t,1,T+1)
	{
		blue = 0; red = 0;
		scanf("%d%d",&N,&K);
		fo(i,0,inf)fo(j,0,inf)g[i][j]='.';
		fo(i,0,N) scanf("%s",&g[i]);
		fo(i,0,N)
		{
			k=N-1;
			Fo(j,0,N)if(g[i][j]!='.')
			{
				g[i][k]=g[i][j]; if(j!=k)g[i][j]='.'; --k;
			}
		}
		call(); printf("Case #%d: ",t);
		if(red+blue == 0)printf("Neither\n");
		else if(red*blue == 1)printf("Both\n");
		else if(red == 1)printf("Red\n");
		else printf("Blue\n");
	}
} 

