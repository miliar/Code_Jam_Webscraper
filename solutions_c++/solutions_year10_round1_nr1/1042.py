#include <iostream>
using namespace std;

int T,N,K;

struct tri
{
	int left, up, upleft, upright;
};

char g[51][51];
char gp[51][51];
tri a[51][51];

void init()
{
	int i,j;
	cin>>N>>K;
	memset(g, 0, sizeof(g));
	memset(gp, 0, sizeof(gp));
	memset(a, 0, sizeof(a));
	for(i=1; i<=N; ++i)
	{
		for(j=1; j<=N; ++j)cin>>g[i][j];
	}
}

void rot()
{
	int i,j, x, y;
	for(i=1,x=1; i<= N; ++i,++x)
	{
		for(j=N,y=1; j>0; --j,++y)
		{
			gp[x][y] = g[j][i];
		}
	}

	for(i=N-1; i>0; --i)
	{
		for(j=1; j<=N; ++j)
		{
			if(gp[i][j] != '.' && gp[i+1][j] == '.')
			{
				int i1, j1;
				i1 = i;
				j1 = j;
				while(gp[i1][j1] != '.' && gp[i1+1][j1] == '.' && i1 < N)
				{
					swap(gp[i1][j1], gp[i1+1][j1]);
					++i1;
				}
			}
		}
	}
}

tri GetTri(int i, int j)
{
	tri m;
	m.left = 0;
	m.up = 0;
	m.upleft = 0;
	m.upright = 0;

	if(gp[i][j] == '.')return m;

	if(gp[i][j] == gp[i][j-1] && j-1 > 0)m.left = a[i][j-1].left;
	if(gp[i][j] == gp[i-1][j] && i-1 > 0)m.up = a[i-1][j].up;
	if(gp[i][j] == gp[i-1][j-1] && i-1>0 && j-1 > 0)m.upleft = a[i-1][j-1].upleft;
	if(gp[i][j] == gp[i-1][j+1] && i-1>0 && j+1 <= N)m.upright = a[i-1][j+1].upright;
	++m.left; 
	++m.up;
	++m.upleft;
	++m.upright;
	return m;

}

int dp()
{
	int fred, fblue;
	int i,j;
	fred = fblue = 0;
	for(i=1; i<=N; ++i)
	{
		for(j=1; j<=N; ++j)
		{
			a[i][j] = GetTri(i, j);
			if(a[i][j].left >= K || a[i][j].up >= K || a[i][j].upleft >= K || a[i][j].upright >= K)
			{
				if(gp[i][j] == 'R')fred = 1;
				else fblue = 1;
			}
		}
	}
	if(fred + fblue == 0)return 0;
	else if(fred + fblue == 2)return 2;
	else if(fred == 1)return 3;
	else return 4;
}

void output(int cases, int result)
{
	if(result == 0)cout<<"Case #"<<cases<<": Neither"<<endl;
	else if(result == 2)cout<<"Case #"<<cases<<": Both"<<endl;
	else if(result == 3)cout<<"Case #"<<cases<<": Red"<<endl;
	else cout<<"Case #"<<cases<<": Blue"<<endl;
}

int main()
{
	int i;
	cin>>T;
	for(i=1; i<=T; ++i)
	{
		init();
		rot();
		output(i, dp());
	}
	return 0;
}