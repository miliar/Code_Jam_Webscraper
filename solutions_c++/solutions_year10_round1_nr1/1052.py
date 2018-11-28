#include "stdafx.h"

#include <stdio.h>
#include <string.h>
char a[64][64];
char b[64][64];
void rotate(int n);
void gravity(int n);
bool row(int n, int k, char c);
bool column(int n, int k, char c);
bool leftdiag(int n, int k, char c);
bool rightdiag(int n, int k, char c);
int main()
{
	int T,N,K;
	int i,j,l,tt;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(tt=1;tt<=T;tt++)
	{
		scanf("%d%d",&N,&K);
		for(i=0;i<N;i++)
		{
			scanf("%s",a[i]);
		}
		rotate(N);
		gravity(N);
		bool r=row(N,K,'R') || column(N,K,'R')||leftdiag(N,K,'R')||rightdiag(N,K,'R');
		bool b=row(N,K,'B') || column(N,K,'B')||leftdiag(N,K,'B')||rightdiag(N,K,'B');
		printf("Case #%d: ",tt);
		if(r&&b)
			printf("Both");
		else if(r)
			printf("Red");
		else if(b)
			printf("Blue");
		else
			printf("Neither");
		printf("\n");
	}
}
void rotate(int n)
{
	int i,j,k;
	int ii,jj;
	for(i=0;i<n;i++)
		strcpy(b[i],a[i]);
	/*for(i=0;i<n;i++)
		for(j=0;j<n;j++)
			a[i][j]='.';*/
	for(i=n-1;i>=0;i--)
	{	
		jj=n-1-i;
		for(j=0;j<n;j++)
		{
			ii=j;
			a[ii][jj]=b[i][j];
		}
	}
}
void gravity(int n)
{
	int i,j,k;
	for(i=0;i<n;i++)
		strcpy(b[i],a[i]);
	for(i=0;i<n;i++)
		for(j=0;j<n;j++)
			a[i][j]='.';
	for(j=0;j<n;j++)
	{
		for(i=n-1;i>=0;i--)
		{
			if(b[i][j]!='.')
			{
				for(k=n-1;k>=0;k--)
				{
					if(a[k][j]=='.')
					{
						a[k][j]=b[i][j];
						break;
					}
				}
			}
		}
	}
}

bool row(int n, int k, char c)
{
	int i,j,l;
	bool flag=false;
	for(i=0;i<n;i++)
	{
		for(j=0;j+k-1<n;j++)
		{
			flag=true;
			for(l=j;l<j+k;l++)
			{
				if(a[i][l]!=c)
				{
					flag=false;
					break;
				}
			}
			if(flag==true)
				return true;
		}
	}
	return false;
}
bool column(int n, int k, char c)
{
	int i,j,l;
	bool flag=false;
	for(j=0;j<n;j++)
	{
		for(i=0;i+k-1<n;i++)
		{
			flag=true;
			for(l=i;l<i+k;l++)
			{
				if(a[l][j]!=c)
				{
					flag=false;
					break;
				}
			}
			if(flag==true)
				return true;
		}
	}
	return false;
}
bool leftdiag(int n, int k, char c)
{
	int i,j,l,ll,x,y;
	bool flag=false;
	int h[64];
	for(l=n-k;l>=0;l--)
	{	
		for(ll=0;ll<n;ll++)
		{
			h[ll]='.';
		}
		i=l;
		j=0;
		while(i<n)
		{
			h[j]=a[i][j];
			i++;
			j++;
		}
		for(x=0;x+k-1<n;x++)
		{
			flag=true;
			for(y=x;y<x+k;y++)
			if(h[y]!=c)
			{
				flag=false;
				break;
			}
			if(flag==true)
				return true;
		}
	}
	for(l=n-k;l>0;l--)
	{	
		for(ll=0;ll<n;ll++)
		{
			h[ll]='.';
		}
		i=0;
		j=l;
		while(j<n)
		{
			h[j]=a[i][j];
			i++;
			j++;
		}
		for(x=0;x+k-1<n;x++)
		{
			flag=true;
			for(y=x;y<x+k;y++)
			if(h[y]!=c)
			{
				flag=false;
				break;
			}
			if(flag==true)
				return true;
		}
	}
	return false;
}
bool rightdiag(int n, int k, char c)
{
	int i,j,l,ll,x,y;
	bool flag=false;
	int h[64];
	for(l=n-1;l>=k-1;l--)
	{	
		for(ll=0;ll<n;ll++)
		{
			h[ll]='.';
		}
		i=l;
		j=0;
		while(i>=0)
		{
			h[j]=a[i][j];
			i--;
			j++;
		}
		for(x=0;x+k-1<n;x++)
		{
			flag=true;
			for(y=x;y<x+k;y++)
			if(h[y]!=c)
			{
				flag=false;
				break;
			}
			if(flag==true)
				return true;
		}
	}
	for(l=1;l<=n-k;l++)
	{	
		for(ll=0;ll<n;ll++)
		{
			h[ll]='.';
		}
		i=n-1;
		j=l;
		while(j<n)
		{
			h[j]=a[i][j];
			i--;
			j++;
		}
		for(x=0;x+k-1<n;x++)
		{
			flag=true;
			for(y=x;y<x+k;y++)
			if(h[y]!=c)
			{
				flag=false;
				break;
			}
			if(flag==true)
				return true;
		}
	}
	return false;
}