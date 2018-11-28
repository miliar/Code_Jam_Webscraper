#include<stdio.h>
#include <iostream>
#include <stdlib.h>

using namespace std;


const double f10 = 1.0;
const double f20 = 2.0;

int d,r,p,c;
int g[501][501];bool win;char lll;
int best, T;
bool work(double cx,double cy,int x,int y);

void init()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&T);
}


bool check(int fx,int fy)
{
	if( work((fx+(best-1)*f10/f20),(fy+(best-1)*f10/f20),fx,fy) )
		return true;
	return false;
}


bool work(double xxx,double yyy,int x,int y)
{
	double tx=0.0,ty=0.0;
	int i,j,k,l;
	
	for(i=x;i<x+best;i++)
		for(j=y;j<y+best;j++)
		{
			if(!( (i==x&&j==y) || (i==x&&(j==y+best-1)) || ((i==x+best-1)&&j==y) || ((i==x+best-1)&&(j==y+best-1)) ))
			{
				tx+=(xxx-i*f10)*(g[i][j]+d)*f10;
				ty+=(yyy-j*f10)*(g[i][j]+d)*f10;
			}
		}
	if(!(tx==0.0 && ty==0.0)) return false;
	return true;
}

void calc()
{
	
	int i,j,k,l;
	for(p=1;p<=T;p++)
	{
		scanf("%d%d%d",&r,&c,&d);
		for(i=1;i<=r;i++)
		{
			scanf("\n");
			for(j=1;j<=c;j++)
			{
				scanf("%c",&lll);
				g[i][j]=lll-'0';
			}
		}
		best=r<c?r:c;win=false;
		while(best>=3)
		{
			for(i=1;i+best-1<=r;i++)
				for(j=1;j+best-1<=c;j++)
					if(check(i,j)){
						win=true;break;}
			if(win) break;
			best--;
			} 
		if(best>=3) printf("Case #%d: %d\n",p,best);
		else printf("Case #%d: IMPOSSIBLE\n",p);
	}
	scanf("%d",&T);
}

int main()
{
	init();
	calc();
	return 0;
}
