#include<stdio.h>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

#define min(a,b) ((a)<(b)?(a):(b))
#define inf 1<<30

int mat[110][110],h,w,vi[110][110];
char a[110][110];

struct abc
{
	int i,j;
};

abc func(int i,int j)
{
	abc tmp;
	tmp.i=i;
	tmp.j=j;
	if(i<0 || j<0 || i>=h || j>=w)
	{
		return tmp;
	}
	int mn=inf,a=-1,b=-1,c=-1,d=-1;
	
	if(i)
	{
		a=mat[i-1][j];
		mn=min(mn,a);
	}
	if(j)
	{
		b=mat[i][j-1];
		mn=min(mn,b);
	}
	if(i<h-1)
	{
		d=mat[i+1][j];
		mn=min(mn,d);
	}
	if(j<w-1)
	{
		c=mat[i][j+1];
		mn=min(mn,c);
	}
	if(mn==a && mn<mat[i][j])
	{
		tmp.i=i-1;
	}
	else if(mn==b&& mn<mat[i][j])
	{
		tmp.j=j-1;
	}
	else if(mn==c&& mn<mat[i][j])
	{
		tmp.j=j+1;
	}
	else if(mn==d&& mn<mat[i][j])
	{
		tmp.i=i+1;
	}
	return tmp;
}

void flood(int i,int j,char ch)
{
	if(i<0 || j<0 || i>=h || j>=w || vi[i][j])
	{
		return;
	}
	vi[i][j]=1;
	a[i][j]=ch;
	abc tmp=func(i,j);
	if(tmp.i!=i || tmp.j!=j)
	{
		flood(tmp.i,tmp.j,ch);
	}
	tmp=func(i-1,j);
	if(tmp.i==i && tmp.j==j)
	{
		flood(i-1,j,ch);
	}
	tmp=func(i+1,j);
	if(tmp.i==i && tmp.j==j)
	{
		flood(i+1,j,ch);
	}
	tmp=func(i,j-1);
	if(tmp.i==i && tmp.j==j)
	{
		flood(i,j-1,ch);
	}
	tmp=func(i,j+1);
	if(tmp.i==i && tmp.j==j)
	{
		flood(i,j+1,ch);
	}
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("Bl.out","w",stdout);
	int cs,t=1,i,j;
	char flchr;
	cin>>cs;
	while(cs--)
	{
		cin>>h>>w;
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				cin>>mat[i][j];
			}
		}
		memset(vi,0,sizeof(vi));
		flchr='a';
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				if(!vi[i][j])
				{
					flood(i,j,flchr);
					flchr++;
				}
			}
		}
		cout<<"Case #"<<t++<<":"<<endl;
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				if(j)
					cout<<" ";
				cout<<a[i][j];
			}
			cout<<endl;
		}
	}
	return 0;
}