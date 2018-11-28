//Q2009 pB
#include <stdio.h>
#include <stdlib.h>
#include <stack>
using namespace std;

struct point
{
	int x,y;
} par[105][105], list[30];
int map[105][105]={0},h,w;

void ini(int y,int x)
{
	par[y][x].y=y;
	par[y][x].x=x;
	if(y-1>=1 && map[y-1][x]<map[par[y][x].y][par[y][x].x])
	{
		par[y][x].y=y-1;
		par[y][x].x=x;
	}
	if(x-1>=1 && map[y][x-1]<map[par[y][x].y][par[y][x].x])
	{
		par[y][x].y=y;
		par[y][x].x=x-1;
	}
	if(x+1<=w && map[y][x+1]<map[par[y][x].y][par[y][x].x])
	{
		par[y][x].y=y;
		par[y][x].x=x+1;
	}
	if(y+1<=h && map[y+1][x]<map[par[y][x].y][par[y][x].x])
	{
		par[y][x].y=y+1;
		par[y][x].x=x;
	}
}

point find(int y,int x)
{
	stack<point> s;
	point t,a;
	t.y=y;
	t.x=x;
	while (t.y!=par[t.y][t.x].y || t.x!=par[t.y][t.x].x)
	{
		s.push(t);
		t=par[t.y][t.x];
	}
	t=par[t.y][t.x];
	while(!s.empty())
	{
		a=s.top();
		s.pop();
		par[a.y][a.x]=t;
	}
	return t;
}

int main()
{
	int a,t,x,y,z,l;
	point p;
	FILE *fin=fopen("B-large.in","r"), *fout=fopen("B-large.out","w");
	fscanf(fin,"%d",&t);
	for(a=1;a<=t;++a)
	{
		l=0;
		fscanf(fin,"%d%d",&h,&w);
		for(y=1;y<=h;++y)
			for(x=1;x<=w;++x)
				fscanf(fin,"%d",&map[y][x]);
		for(y=1;y<=h;++y)
			for(x=1;x<=w;++x)
				ini(y,x);
		fprintf(fout,"Case #%d:\n",a);
		for(y=1;y<=h;++y)
		{
			for(x=1;x<=w;++x)
			{
				p=find(y,x);
				for(z=0;z<l;++z)
				{
					if(p.y==list[z].y&&p.x==list[z].x)
					{
						fprintf(fout,"%c",z+'a');
						break;
					}
				}
				if(z==l)
				{
					fprintf(fout,"%c",l+'a');
					list[l++]=p;
				}
				if(x!=w)
					fprintf(fout," ");
			}
			fprintf(fout,"\n");
		}
	}
	return 0;
}
