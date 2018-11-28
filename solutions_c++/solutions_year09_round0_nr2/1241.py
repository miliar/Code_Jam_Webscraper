//============================================================================
// Name        : watersheds.cpp
// Author      : Kinshul Verma
// Version     :
// Copyright   :
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string.h>
#include <stack>
using namespace std;

int main() {
	int H,W,i,j,x,y,minx,miny,min,count,a,b,t;
	bool flag;
	int alt[101][101];
	char sinks[101][101];
	scanf("%d",&t);
	for(int case_num=1; case_num<=t; case_num++)
	{
		bool visited[101][101]={0};
		scanf("%d %d",&H,&W);
		for(i=0; i<H; i++)
			for(j=0; j<W; j++)
				scanf("%d",&alt[i][j]);
		/*
		for(i=0; i<H; i++)
		{
					for(j=0; j<W; j++)
						printf("%d",alt[i][j]);
					printf("\n");
		}
		*/
		count=0;
		for(i=0; i<H; i++)
		{
			for(j=0; j<W; j++)
			{
				if(visited[i][j] == 0)
				{
					stack <int> path;
					x=i;
					y=j;
					min = alt[x][y];
					minx=x;
					miny=y;
					path.push(x*W+y);
					while(visited[x][y] == 0)
					{
						flag=0;
						if(x-1>=0 && alt[x-1][y]<min)
						{
							minx=x-1;
							miny=y;
							min = alt[minx][miny];
							flag=1;
						}
						if(y-1>=0 && alt[x][y-1]<min)
						{
							minx=x;
							miny=y-1;
							min = alt[minx][miny];
							flag=1;
						}
						if(y+1<W && alt[x][y+1]<min)
						{
							minx=x;
							miny=y+1;
							min = alt[minx][miny];
							flag=1;
						}
						if(x+1<H && alt[x+1][y]<min)
						{
							minx=x+1;
							miny=y;
							min = alt[minx][miny];
							flag=1;
						}
						if(flag==1)
						{
							x=minx;
							y=miny;
							path.push(x*W+y);
						}
						else
						{
							visited[x][y]=1;
							sinks[x][y]=count+97;
							++count;
						}
					}
					while(!path.empty())
					{
						a=path.top()/W;
						b=path.top()%W;
						sinks[a][b]=sinks[x][y];
						visited[a][b]=1;
						path.pop();
					}
				}
			}
		}
		printf("Case #%d:\n",case_num);
		for(i=0; i<H; i++)
		{
			for(j=0; j<W; j++)
				printf("%c ",sinks[i][j]);
			printf("\n");
		}
	}
	return 0;
}
