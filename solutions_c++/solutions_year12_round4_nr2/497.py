#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <cmath>
#include <set>
using namespace std;

int r[1100];
int x[1100];
int y[1100];
int X[1100];
int Y[1100];
int index[1100];

struct node
{
	int x,y;
	int r,index;
};

node a[1100];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int re,i,j,k,n,tmp,L,W,tx,ty;
	int cases=1;
	int R;
	cin>>re;
	while(re--)
	{
		cin>>n>>L>>W;
		for(i=0;i<n;i++)
		{
			a[i].index=i;
			cin>>a[i].r;
		}
		
		for(i=0;i<n;i++)
		{
			for(j=i+1;j<n;j++)
			{
				if(a[j].r>a[i].r)
				{
					node ss=a[i];
					a[i]=a[j];
					a[j]=ss;
				}
			}
		}
		
		if(W<L)
		{
			a[0].x=a[0].y=0;
			R=a[0].r;
			for(i=1;i<n;i++)
			{
				ty=a[i-1].y+a[i-1].r+a[i].r;
				if(ty>W)
				{
					a[i].y=0;
					a[i].x=a[i-1].x+R+a[i].r;
					R=a[i].r;
				}
				else
				{
					a[i].y=ty;
					a[i].x=a[i-1].x;
					
				}
			}
		}
		
		else
		{
			a[0].x=a[0].y=0;
			R=a[0].r;
			for(i=1;i<n;i++)
			{
				tx=a[i-1].x+a[i-1].r+a[i].r;
				if(tx>L)
				{
					a[i].x=0;
					a[i].y=a[i-1].y+R+a[i].r;
					R=a[i].r;
				}
				else
				{
					a[i].x=tx;
					a[i].y=a[i-1].y;
				}
			}
			
		}
		
		

	
	
	
		printf("Case #%d:",cases++);
		
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			if(a[j].index==i)
			cout<<" "<<a[j].x<<" "<<a[j].y;
		}
		cout<<endl;
	
		
		
		
	}

	
	return 0;
}