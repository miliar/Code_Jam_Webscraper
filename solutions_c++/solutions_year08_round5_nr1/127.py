#include <stdio.h>
#include <algorithm>
#include <string>
#include <iostream>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <sstream>
#include <map>
#include <assert.h>
using namespace std;
#define N 3000
#define M 1000000
int dir[][2]={{0,1},{1,0},{0,-1},{-1,0}};
char table[6001][6001];
int XX[M],Y1[M],Y2[M];
int YY[M],X1[M],X2[M];
char all[M+1];
int myindex1[M],myindex2[M];
bool cmpX1(int a,int b)
{
	return X1[a]<X1[b];
}
bool cmpX2(int a,int b)
{
	return X2[a]<X2[b];
}
int tmp[10*N];
void scanX(int ytop,int xmax)
{
	for(int i=0;i<ytop;i++)
		myindex1[i]=myindex2[i]=i;
	sort(myindex1,myindex1+ytop,cmpX1);
	sort(myindex2,myindex2+ytop,cmpX2);
	int p1=0,p2=0;
	set<int> tree;
	set<int>::iterator it;
	for(int x=0;x<xmax;x++)
	{
		while(p2<ytop&&X2[myindex2[p2]]==x)
			assert(tree.end()!=tree.find(YY[myindex2[p2]])),
			tree.erase(tree.find(YY[myindex2[p2++]]));

		while(p1<ytop&&X1[myindex1[p1]]==x)
			tree.insert(YY[myindex1[p1++]]);
		int top=0;
		for(it=tree.begin();it!=tree.end();it++)
			tmp[top++]=*it;
		for(int i=1;i+1<top;i+=2)
		for(int y=tmp[i];y<tmp[i+1];y++)
			table[x][y]=1;
	}
}
bool cmpY1(int a,int b)
{
	return Y1[a]<Y1[b];
}
bool cmpY2(int a,int b)
{
	return Y2[a]<Y2[b];
}
void scanY(int xtop,int ymax)
{
	for(int i=0;i<xtop;i++)
		myindex1[i]=myindex2[i]=i;
	sort(myindex1,myindex1+xtop,cmpY1);
	sort(myindex2,myindex2+xtop,cmpY2);
	int p1=0,p2=0;
	set<int> tree;
	set<int>::iterator it;
	//puts("------------------------");
	for(int y=0;y<ymax;y++)
	{
		while(p2<xtop&&Y2[myindex2[p2]]==y)
			//printf("erase %d\n",XX[myindex2[p2]]),
			assert(tree.end()!=tree.find(XX[myindex2[p2]])),
			tree.erase(tree.find(XX[myindex2[p2++]]));

		while(p1<xtop&&Y1[myindex1[p1]]==y)
			tree.insert(XX[myindex1[p1++]]);//,printf("insert %d %d\n",myindex1[p1-1],XX[myindex1[p1-1]]);
				int top=0;
		for(it=tree.begin();it!=tree.end();it++)
			tmp[top++]=*it;
		for(int i=1;i+1<top;i+=2)
		for(int x=tmp[i];x<tmp[i+1];x++)
			table[x][y]=1;
	}
}
int main()
{
	int t,ca=1;
	for(scanf("%d",&t);t--;)
	{
		int n;
		scanf("%d",&n);
		int x=0,y=0,x1=0,x2=0,y1=0,y2=0;
		int d=0;
		int xtop=0,ytop=0;
		char buf[50];
		int top=0;
		for(int i=0;i<n;i++)
		{
			int rep;
			scanf("%s %d",buf,&rep);
			int len=strlen(buf);
			while(rep--)
				memcpy(all+top,buf,len),top+=len;
		}
		int px=x,py=y;
		if(all[top-1]=='F')
			all[top++]='R';
		for(int i=0;i<top;i++)
		{
			if(all[i]=='F')
			{
				x+=dir[d][0];y+=dir[d][1];
			}
			else 
			{
				if(px==x)
				{
					if(py!=y)
					{
						XX[xtop]=px;
						Y1[xtop]=min(py,y);
						Y2[xtop++]=max(py,y);
					}
				}
				else
				{
					assert(py==y);
					if(px!=x)
					{
						YY[ytop]=y;
						X1[ytop]=min(px,x);
						X2[ytop++]=max(px,x);
					}
				}
				if(all[i]=='R')d=(d+1)%4;
				else d=(d+3)%4;
				px=x;py=y;
			}
			x1=min(x1,x);
			x2=max(x2,x);
			y1=min(y,y1);
			y2=max(y,y2);
	//		printf("%d %d--->%d %d\n",px,py,x,y);
		}
	//	printf("xtop=%d ytop=%d\n",xtop,ytop);
	//	for(int i=0;i<xtop;i++)
	//		printf("%d,%d-->%d,%d\n",XX[i],Y1[i],XX[i],Y2[i]);
	//	for(int i=0;i<ytop;i++)
	//		printf("%d,%d--->%d,%d\n",X1[i],YY[i],X2[i],YY[i]);
		x2-=x1;y2-=y1;
		for(int i=0;i<xtop;i++)
			XX[i]-=x1,Y1[i]-=y1,Y2[i]-=y1;
		for(int i=0;i<ytop;i++)
			YY[i]-=y1,X1[i]-=x1,X2[i]-=x1;
		for(int i=0;i<x2;i++)
		for(int j=0;j<y2;j++)
			table[i][j]=0;
		scanX(ytop,x2);
		scanY(xtop,y2);
		int ans=0;
		for(int i=0;i<x2;i++)
		for(int j=0;j<y2;j++)
			if(table[i][j])ans++;//,printf("%d %d\n",x,y);
		printf("Case #%d: %d\n",ca++,ans);
	}
	return 0;
}
