#include <iostream>
#include <stdio.h>
#include <queue>

using namespace std;

int h,w;
int alt[101][101];
int visited[101][101];
int labels[101][101];
int direction_x[101][101];
int direction_y[101][101];
struct point{
	int x,y;
};
void do_bfs(int x,int y, int label)
{
	queue<point> q;
	point p;
	p.x = x;
	p.y = y;
	q.push(p);
	int neighbors[][2]={-1,0,+1,0,0,-1,0,+1};
	visited[x][y] = 1;
	labels[x][y] = label;
	while(!q.empty())
	{
		point top = q.front();
		q.pop();
		//printf("top %d %d\n",top.x,top.y);
		for(int counter = 0; counter<4; counter++)
		{
			int x1 = top.x + neighbors[counter][0];
			int y1 = top.y + neighbors[counter][1];
			if(x1 >= 0 && y1 >= 0 && x1 < h && y1 < w)
			{
				if(alt[x1][y1]>alt[x][y] && visited[x1][y1] == 0 )
				{
					if(top.x == direction_x[x1][y1]+x1 && top.y == direction_y[x1][y1]+y1)
					{
						visited[x1][y1] = 1;
						labels[x1][y1] = label;
						point p1;
						p1.x = x1;p1.y = y1;
						q.push(p1);
					}
				}
			}
		}
	}
}
int main()
{
	int t;
	cin>>t;
	int caseno = 1;
	while(t--)
	{

		cin>>h>>w;
		memset(alt,0,sizeof(alt));
		memset(visited,0,sizeof(visited));
		memset(labels,0,sizeof(labels));
		for(int c1 = 0; c1<h; c1++)
			for(int c2 = 0; c2<w; c2++)
			{
				cin>>alt[c1][c2];
			}
		//create direction_x,direction_y
		memset(direction_x,0,sizeof(direction_x));
		memset(direction_y,0,sizeof(direction_y));
		int neighbors[4][2] = {-1,0,0,-1,0,+1,+1,0};
		for(int c1 = 0; c1<h; c1++)
		{
			for(int c2 = 0; c2<w; c2++)
			{
				int x1,y1;
				int minval = 1232312;
				int minpos=-1;
				for(int c3=0; c3<4;c3++)
				{
					x1 = c1 + neighbors[c3][0];
					y1 = c2 + neighbors[c3][1];
					if(x1 >=0 && x1 <h && y1 >=0 && y1<w)
					{
					if(alt[x1][y1] < alt[c1][c2])
					{
						if(alt[x1][y1] <minval)
						{
							minval = alt[x1][y1];
							minpos = c3;
						}
					}
					}
				}
				if(minpos != -1)
				{
					direction_x[c1][c2] = neighbors[minpos][0];
					direction_y[c1][c2] = neighbors[minpos][1];
				}
			}
		}
		bool done = false;
		int curr_label = 0;
		while(!done)
		{
		int mx=-1,my=-1;
		int minv = 100000;
		for(int c1 = 0; c1<h; c1++)
			for(int c2 = 0; c2<w; c2++)
			{
				if(alt[c1][c2]<minv  && visited[c1][c2] == 0)
				{
					minv = alt[c1][c2];
					mx = c1;
					my = c2;
				}
			}
		if(mx == -1)
		{
			done = true;
			break;
		}
		curr_label++;
		
		do_bfs(mx,my,curr_label);
		}

		char maps[20000];
		memset(maps,0,sizeof(maps));
		int curr_c = 'a';
		char relabel[101][101];
		for(int c1 =0;c1<h;c1++)
		{
			for(int c2 = 0; c2<w; c2++)
			{
				if(maps[labels[c1][c2]]==0)
				{
					relabel[c1][c2] = curr_c;
					maps[labels[c1][c2]]=curr_c;
					curr_c++;
				}
				else
				{
					relabel[c1][c2] = maps[labels[c1][c2]];
				}
			}
		}
		printf("Case #%d:\n",caseno++);
		for(int c1 = 0; c1<h; c1++)
		{
			for(int c2 = 0; c2<w; c2++)
			{
				if(c2 != 0)
					printf(" ");
				printf("%c",relabel[c1][c2]);
			}
			printf("\n");
		}
		
	}
	return 0;
}