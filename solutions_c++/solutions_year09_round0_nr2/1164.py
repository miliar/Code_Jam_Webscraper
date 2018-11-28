//find and union
#include<iostream>
#include<queue>
using namespace std;

const int inf = 1000000000;
#define MR 110
int wys[MR][MR], h, w, p[MR*MR], r[MR*MR];

struct pole
{
	int h, w;
}x, y;

queue<pole> q;

void makeset(int x)
{
	p[x] = x;
	r[x] = 0;
}//make set
void unionset (int x,int y)
{
	if(r[x]>r[y])
		p[y]=x;
	else
	{
		p[x]=y;
		if(r[x] == r[y])
			r[y]++;
	}
}//union set
int findset(int x)
{
	if(p[x]!=x)
		p[x] = findset(p[x]);
	return p[x];
}//find set

int mn(int x, int y)
{
	return x < y ? x : y;
}

pole ktore(int h1, int w1)	//do ktorego pola splynie woda
{
	pole x;
	x.h = x.w = 0;
	int nv = inf, sv = inf, wv = inf, ev = inf;
	if(h1)
		nv = wys[h1-1][w1];
	if(h1 < h-1)
		sv = wys[h1+1][w1];
	if(w1)
		wv = wys[h1][w1-1];
	if(w1 < w-1)
		ev = wys[h1][w1+1];
	int m = mn(nv, mn(wv, mn(ev, sv)));
	if(m == inf)
		return x;
	if(m == nv)
	{
		x.h = h1-1;
		x.w = w1;
	}
	else if(m == wv)
	{
		x.h = h1;
		x.w = w1-1;
	}
	else if(m == ev)
	{
		x.h = h1;
		x.w = w1+1;
	}
	else
	{
		x.h = h1+1;
		x.w = w1;
	}	
	return x;
}
int main()
{
	//freopen("test.in", "r", stdin);
	//freopen("test.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for(int c = 0; c < tests; c++)
	{
		int k = 0;
		scanf("%d%d", &h, &w);
		for(int i = 0; i < h; i++)
			for(int j = 0; j < w; j++)			
				scanf("%d", &wys[i][j]);
			
		for(int i = 0; i < h; i++)
			for(int j = 0; j < w; j++)
				makeset(i*w + j);

		for(int i = 0; i < h; i++)
			for(int j = 0; j < w; j++)
			{
				x = ktore(i, j);
				if(wys[x.h][x.w] < wys[i][j])
				{
					if(findset(x.h*w + x.w) != findset(i*w + j))					
						unionset(findset(x.h*w + x.w), findset(i*w + j));					
				}
			}

		for(int i = 0; i < h; i++)
			for(int j = 0; j < w; j++)
				wys[i][j] = 0;
		k = 0;
		for(int i = 0; i < h; i++)
			for(int j = 0; j < w; j++)
				if(!wys[i][j])
				{
					k++;
					wys[i][j] = k;
					x.h = i;
					x.w = j;
					q.push(x);
					while(!q.empty())
					{
						x = q.front();
						if(x.h > 0 && !wys[x.h-1][x.w] && findset((x.h-1)*w + x.w) == findset(x.h*w + x.w))
						{
							y.h = x.h-1;
							y.w = x.w;
							wys[y.h][y.w] = k;
							q.push(y);
						}
						if(x.h < h-1 && !wys[x.h+1][x.w] && findset((x.h+1)*w + x.w) == findset(x.h*w + x.w))
						{
							y.h = x.h+1;
							y.w = x.w;
							wys[y.h][y.w] = k;
							q.push(y);
						}
						if(x.w > 0 && !wys[x.h][x.w-1] && findset(x.h*w + x.w-1) == findset(x.h*w + x.w))
						{
							y.h = x.h;
							y.w = x.w-1;
							wys[y.h][y.w] = k;
							q.push(y);
						}
						if(x.w < w-1 && !wys[x.h][x.w+1] && findset(x.h*w + x.w+1) == findset(x.h*w + x.w))
						{
							y.h = x.h;
							y.w = x.w+1;
							wys[y.h][y.w] = k;
							q.push(y);
						}
						q.pop();
					}
				}
		printf("Case #%d:\n", c+1);
		for(int i = 0; i < h; i++)
		{
			for(int j = 0; j < w; j++)			
				printf("%c ", 96+wys[i][j]);			
			printf("\n");
		}
	}
	return 0;
}