#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int map[128][128];
int info[128][128];
int h,w; //³¤ºÍ¿í

int zerox[10010],zeroy[10010];
int hx[10010],hy[10010];

char ap[26];

int main()
{
	int t,_t;
	cin>>_t;
	for (t=1;t<=_t;t++)
	{
		cin>>h>>w;
		for (int y=0;y<h;y++)
			for (int x=0;x<w;x++)
			{
				cin>>map[y][x];
			}
		memset(info,0,sizeof(info));
		int count=0,head,rear;
		for (int y=0;y<h;y++)
			for (int x=0;x<w;x++)
			{
				int north = (y==0)?100000:map[y-1][x];
				int west = (x==0)?100000:map[y][x-1];
				int east = (x==w-1)?100000:map[y][x+1];
				int south = (y==h-1)?100000:map[y+1][x];
				int self = map[y][x];

				int m = min(min(north,south),min(west,east));

				if (m==north && m<self) { info[y][x]=1; continue;}
				if (m==west && m<self) { info[y][x]=2; continue;}
				if (m==east && m<self) { info[y][x]=3; continue;}
				if (m==south && m<self) { info[y][x]=4; continue;}

				zerox[count]=x; zeroy[count]=y; count++;
			}
/*
		for (int y=0;y<h;y++)
		{
			for (int x=0;x<w;x++)
			{
				printf("{%d} ",map[y][x]);
			}
			putchar('\n');
		}
		for (int y=0;y<h;y++)
		{
			for (int x=0;x<w;x++)
			{
				printf("[%d] ",info[y][x]);
			}
			putchar('\n');
		}
*/

		for (int q=0;q<count;q++)
		{
			head=0; rear=1; hx[0]=zerox[q]; hy[0]=zeroy[q];
			while (head!=rear)
			{
				int x=hx[head],y=hy[head];
				if (x>0 && info[y][x-1]==3) { hx[rear]=x-1; hy[rear]=y; rear++; }
				if (y>0 && info[y-1][x]==4) { hx[rear]=x; hy[rear]=y-1; rear++; }
				if (x<w-1 && info[y][x+1]==2) { hx[rear]=x+1; hy[rear]=y; rear++; }
				if (y<h-1 && info[y+1][x]==1) { hx[rear]=x; hy[rear]=y+1; rear++; }
				map[y][x]=q;
				head++;
			}
		}
		memset(ap,0,sizeof(ap));
		char ori='a';
		for (int y=0;y<h;y++)
			for (int x=0;x<w;x++)
			{
				if (!ap[map[y][x]])
				{
					ap[map[y][x]]=ori++;
				}
			}

		// output
		printf("Case #%d:\n",t);
		for (int y=0;y<h;y++)
		{
			int pp=0;
			for (int x=0;x<w;x++)
			{
				if (pp) putchar(' '); else pp=1;
				putchar(ap[map[y][x]]);
			}
			putchar('\n');
		}
	}
	return 0;
}
