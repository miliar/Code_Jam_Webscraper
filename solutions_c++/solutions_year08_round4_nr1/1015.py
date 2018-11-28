#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
int i,j,l,m,n,h,hh,ans,fmin[10000][2];
bool ver[10000],type[10000],ch[10000],v;
int findmin(int x,bool y)
{
	int k,p,t,mm;	
	if (fmin[x][y]!=-1) {return(fmin[x][y]);}
	else
	{
		if (ch[x])
		{
			if (y==1)
			{
				if (type[x]==1)
				{
					mm=findmin((x+1)*2-1,1)+findmin((x+1)*2,1);
					k=findmin((x+1)*2-1,1)+findmin((x+1)*2,1);
					p=findmin((x+1)*2-1,0)+findmin((x+1)*2,1);
					t=findmin((x+1)*2-1,1)+findmin((x+1)*2,0);
					if (k>p) {k=p;}
					if (k>t) {k=t;}
					if (mm>k+1) {mm=k+1;}
				}
				else
				{
						k=findmin((x+1)*2-1,1)+findmin((x+1)*2,1);
					p=findmin((x+1)*2-1,0)+findmin((x+1)*2,1);
					t=findmin((x+1)*2-1,1)+findmin((x+1)*2,0);
					if (k>p) {k=p;}
					if (k>t) {k=t;}
					mm=findmin((x+1)*2-1,1)+findmin((x+1)*2,1);
					if (mm+1<k) {mm+=1;} else {mm=k;}
				}
					}
			else
			{
				if (type[x]==1)
				{
					k=findmin((x+1)*2-1,0)+findmin((x+1)*2,0);
					p=findmin((x+1)*2-1,0)+findmin((x+1)*2,1);
					t=findmin((x+1)*2-1,1)+findmin((x+1)*2,0);
					if (k>p) {k=p;}
					if (k>t) {k=t;}
					mm=findmin((x+1)*2-1,0)+findmin((x+1)*2,0);
					if (mm+1<k) {mm+=1;} else {mm=k;}		
	
				}
				else
				{
					mm=findmin((x+1)*2-1,0)+findmin((x+1)*2,0);
					k=findmin((x+1)*2-1,0)+findmin((x+1)*2,0);
					p=findmin((x+1)*2-1,0)+findmin((x+1)*2,1);
					t=findmin((x+1)*2-1,1)+findmin((x+1)*2,0);
					if (k>p) {k=p;}
					if (k>t) {k=t;}
					if (mm>k+1) {mm=k+1;}
	
				}
			}
		}
			else
			{
				if (y==1)
			{
				if (type[x]==1)
				{
					mm=findmin((x+1)*2-1,1)+findmin((x+1)*2,1);				
				}
				else
				{
				k=findmin((x+1)*2-1,1)+findmin((x+1)*2,1);
				p=findmin((x+1)*2-1,0)+findmin((x+1)*2,1);
				t=findmin((x+1)*2-1,1)+findmin((x+1)*2,0);
				if (k>p) {k=p;}
				if (k>t) {k=t;}
				mm=k;
			}
		}
		else
		{
			if (type[x]==1)
			{
				k=findmin((x+1)*2-1,0)+findmin((x+1)*2,0);
				p=findmin((x+1)*2-1,0)+findmin((x+1)*2,1);
				t=findmin((x+1)*2-1,1)+findmin((x+1)*2,0);
				if (k>p) {k=p;}
				if (k>t) {k=t;}
				mm=k;
			}
			else
			{
				mm=findmin((x+1)*2-1,0)+findmin((x+1)*2,0);				
			}
		}
		}
	}
	fmin[x][y]=mm;
	return(mm);
}
int main()
{
	freopen("a-small.in","r",stdin);
	freopen("a-small.out","w",stdout);
	scanf("%d\n",&hh);
	for(h=1;h<=hh;h++)
	{
		for(i=0;i<10000;i++)
			for(j=0;j<2;j++)
			{
				fmin[i][j]=-1;
			}
		scanf("%d%d\n",&n,&v);
		for(i=0;i<((n-1)/2);i++) {scanf("%d%d",&l,&j);type[i]=l;ch[i]=j;}
		for(i=((n-1)/2);i<n;i++) {scanf("%d",&ver[i]);fmin[i][ver[i]]=0;fmin[i][!ver[i]]=n+1;}
		ans=findmin(0,v);
		if (ans<n) {printf("Case #%d: %d\n",h,ans);}
		else {printf("Case #%d: IMPOSSIBLE\n",h);}
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
