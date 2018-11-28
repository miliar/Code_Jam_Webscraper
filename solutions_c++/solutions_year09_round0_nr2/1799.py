// C.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include <iostream>
using namespace std;

int map[110][110];
char rmap[110][110];
bool hash[110][110];
int H,W,T,flag,cas = 1;
char ch;

typedef struct node
{
	int x,y;
}node;


node Min(int x,int y,int N,int W,int E,int S)
{
    node tmp;
    if(N <= W && N <= E && N <= S)
    {
        tmp.x = x-1;
        tmp.y = y;
        return tmp;
    }
    if(W <= E && W <= S)
    {
        tmp.x = x;
        tmp.y = y-1;
        return tmp;
    }
    if(E <= S)
    {
        tmp.x = x;
        tmp.y = y + 1;
        return tmp;
    }
    tmp.x = x + 1;
    tmp.y = y;
    return tmp;
}

char dfs(int x,int y)
{
    node lmin=Min(x,y,map[x-1][y],map[x][y-1],map[x][y+1],map[x+1][y]);
    if(map[lmin.x][lmin.y]>=map[x][y])
    {
        if(hash[x][y]==true)
            return rmap[x][y];
        rmap[x][y]=ch;
        hash[x][y]=true;
        ch++;
    }
    else if(hash[lmin.x][lmin.y]==true)
    {
        rmap[x][y]=rmap[lmin.x][lmin.y];
		hash[x][y]=true;
    }
    else
    {
		hash[x][y]=true;
        rmap[x][y]=dfs(lmin.x,lmin.y);
    }
    return rmap[x][y];
}
/*
void bfs()
{
	while(!q.empty())
	{
		out = q.front();
		q.pop();
		
		if (out.ct <= map[out.x - 1][out.y] && out.ct <= map[out.x + 1][out.y] && out.ct <= map[out.x][out.y - 1] && out.ct <= map[out.x][out.y + 1])
		{
			use = true;
			continue;
		}

		if(!out.isok())
			continue;

		int N,W,E,S,ret;
		N = map[out.x - 1][out.y];
		W = map[out.x][out.y - 1];
		E = map[out.x][out.y + 1];
		S = map[out.x + 1][out.y];

		ret = Sort(N,W,E,S);

		if(ret == N)
		{
			in.x = out.x - 1,in.y = out.y,in.ct = map[in.x][in.y];
			if(!hash[in.x][in.y])
			{
				hash[in.x][in.y] = flag;
				use = true;
				q.push(in);
				continue;
			}
			if(hash[in.x][in.y] < hash[out.x][out.y])
				hash[out.x][out.y] = hash[in.x][in.y];
		}
		else if(ret == W)
		{
			in.x = out.x,in.y = out.y - 1,in.ct = map[in.x][in.y];
			if(!hash[in.x][in.y])
			{
				hash[in.x][in.y] = flag;
				use = true;
				q.push(in);
				continue;
			}
			if(hash[in.x][in.y] < hash[out.x][out.y])
				hash[out.x][out.y] = hash[in.x][in.y];

		}
		else if(ret == E)
		{
			in.x = out.x,in.y = out.y + 1,in.ct = map[in.x][in.y];
			if(!hash[in.x][in.y])
			{				
				hash[in.x][in.y] = flag;
				use = true;
				q.push(in);
				continue;
			}
			if(hash[in.x][in.y] < hash[out.x][out.y])
				hash[out.x][out.y] = hash[in.x][in.y];
		}

		else if(ret == S)
		{
			in.x = out.x + 1 ,in.y = out.y,in.ct = map[in.x][in.y];
			if(!hash[in.x][in.y])
			{
				hash[in.x][in.y] = flag;
				use = true;
				q.push(in);
				continue;
			}
			if(hash[in.x][in.y] < hash[out.x][out.y])
				hash[out.x][out.y] = hash[in.x][in.y];
		}
	}

	while(!q.empty())
		q.pop();
}*/



int _tmain(int argc, _TCHAR* argv[])
{
	int i,j;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin >> T;
	while(T --)
	{
		cin >> H >> W;
		for (i = 0; i <= H + 1; ++ i)
			for (j = 0; j <= W + 1; ++ j)
				map[i][j] = INT_MAX;

		for (i = 1; i <= H; ++ i)
			for (j = 1; j <= W; ++ j)
				cin >> map[i][j];

		memset(hash,0,sizeof(hash));

		ch = 'a';
		for (i = 1; i <= H; ++ i)
			for (j = 1; j <= W; ++ j)
			{
				if(!hash[i][j])
				{
					dfs(i,j);
				}
			}
		printf("Case #%d:\n",cas ++);
		for (i = 1; i <= H; ++ i)
		{
			for (j = 1; j < W; ++ j)
			{
				printf("%c ", rmap[i][j]);
			}

			printf("%c\n", rmap[i][j]);
		}
	}
	return 0;
}

