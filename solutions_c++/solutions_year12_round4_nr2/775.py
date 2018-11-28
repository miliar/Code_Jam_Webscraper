#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
struct Node
{
	int index;
	double radius;
	double x,y;
}nodes[1005];
int compare1(const void* a, const void* b)
{
	Node* aa=(Node*)a;
	Node* bb=(Node*)b;
	return -(aa->radius-bb->radius);
}
int compare2(const void* a, const void* b)
{
	Node* aa=(Node*)a;
	Node* bb=(Node*)b;
	return aa->index-bb->index;
}
int N,W,L;
bool Check(int s, int e)
{
	for(int i=s;i<e;i++)
	{
		for(int j=i+1;j<=e;j++)
		{
			double dist = (nodes[i].radius+nodes[j].radius);
			double dist2 = (nodes[i].x-nodes[j].x)*(nodes[i].x-nodes[j].x)+(nodes[i].y-nodes[j].y)*(nodes[i].y-nodes[j].y);
			if(dist2<dist*dist)
				return false;
		}
	}
	return true;
}
int Dist(int s, int e)
{
	for(int i=s;i<e;i++)
	{
		for(int j=i+1;j<=e;j++)
		{
			double dist = (nodes[i].radius+nodes[j].radius);
			double dist2 = (nodes[i].x-nodes[j].x)*(nodes[i].x-nodes[j].x)+(nodes[i].y-nodes[j].y)*(nodes[i].y-nodes[j].y);
			if(dist2<dist*dist)
				return dist-sqrt(dist2)+1;
		}
	}
	return 0;
}
int main()
{
	freopen("F:\\in.txt","r",stdin);
	freopen("F:\\out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		printf("Case #%d:",t);
		scanf("%d%d%d",&N,&W,&L);
		for(int i=0;i<N;i++)
		{
			scanf("%lf",&nodes[i].radius);
			nodes[i].index=i;
		}
		qsort(nodes,N,sizeof(nodes[0]),compare1);
		nodes[0].x=0;
		nodes[0].y=0;
		nodes[1].x=W;
		nodes[1].y=L;
		for(int i=2;i<N;i++)
		{
			bool found=false;
			for(int x=0;x<=W;)
			{
				int dist;
				for(int y=0;y<L;)
				{
					nodes[i].x=x;
					nodes[i].y=y;
					dist=Dist(0,i);
					if(dist==0)
					{
						found=true;
						break;
					}
					//dist=max(dist/2,1);
					y+=dist;
				}				
				if(found) break;
				x+=dist;
			}
		}
		qsort(nodes,N,sizeof(nodes[0]),compare2);
		for(int i=0;i<N;i++)
		{
			printf(" %.1lf %.1lf",nodes[i].x,nodes[i].y);
		}
		printf("\n");
		if(Check(0,N-1)==false)
		{
			printf("Error!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n");
		}
	}
}