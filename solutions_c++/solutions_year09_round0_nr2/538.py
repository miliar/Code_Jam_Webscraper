#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;
FILE * fp;
FILE * out;

int t;
int r,c;

int g[103][103];


char ch[30];

int d[103][103];

int f[][2] = {-1,0,0,-1,0,1,1,0};

int find(int & x,int & y)
{
	int mmax = -1;
	for(int i = 0;i < r;i ++)
		for(int j = 0;j < c;j ++)
		{
			if(d[i][j] == -1 && g[i][j] > mmax)
			{
				mmax = g[i][j];
				x = i;
				y = j;
			}
		}
    
	return mmax;
}


int dfs(int x,int y,int k)
{
	if(d[x][y] != -1)
		return d[x][y];

	int mx = x,my = y;
	for(int i = 0;i < 4;i ++)
	{
		int xx = x + f[i][0];
		int yy = y + f[i][1];
		if(xx >= 0 && xx < r && yy >= 0 && yy < c && g[xx][yy] < g[mx][my])
		{
			mx = xx;
			my = yy;
		}
	}
	if(mx != x || my != y)
	{
		d[x][y] = dfs(mx,my,k);
	}
	else
	{
		d[x][y] = k;
	}
	return d[x][y];

}





int main()
{
	fp = fopen("B-large.in","r");
	out = fopen("A-small.out","w");
	fscanf(fp,"%d",&t);
	int cnt = 0;
	while(--t >= 0)
	{
		fscanf(fp,"%d%d",&r,&c);
		for(int i = 0;i < r;i ++)
			for(int j = 0;j < c;j ++)
				fscanf(fp,"%d",&g[i][j]);
		memset(d,-1,sizeof(d));
		int x,y;
		int pos = 0;
		while(find(x,y) != -1)
		{
			if(dfs(x,y,pos) == pos)
			   pos ++;
		}
		memset(ch,-1,sizeof(ch));

		char cc = 'a';
		for(int i = 0;i < r;i ++)
			for(int j= 0;j < c;j ++)
			{
				if(ch[d[i][j]] == -1)
				{
					ch[d[i][j]] = cc;
					cc += 1;
				}
			}
		++cnt;
		fprintf(out,"Case #%d:\n",cnt);
	    for(int i = 0;i < r;i ++)
		{
			for(int j = 0;j < c;j ++)
			{
				if(j > 0)
					fprintf(out," ");
				fprintf(out,"%c",ch[d[i][j]]);
			}
			fprintf(out,"\n");
		}
	}


	
	return 0;
}