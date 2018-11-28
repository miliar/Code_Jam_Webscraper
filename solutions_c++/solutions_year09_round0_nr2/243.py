#include <iostream>
#include <string>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define esta(x,c) ((c).find(x) != (c).end())

#define INF 1000000000

int N,H,W;

int dx[4] = {-1,0,0,1};
int dy[4] = {0,-1,1,0};

int h[128][128];
char m[128][128];

int u[128][128][4];

int alt(int x,int y)
{
	if (x < 0 || x >= H || y < 0 || y >= W)
		return INF;
	return h[x][y];
}

char c;

void flood_fill(int x,int y)
{
	if (m[x][y] != 0)
		return;
	m[x][y] = c;
	forn(z,4)
	if (u[x][y][z])
		flood_fill(x+dx[z],y+dy[z]);
}

int main()
{
	freopen("entrada.in","r",stdin);
	freopen("salida.out","w",stdout);
	cin >> N;
	forn(tt,N)
	{
		cin >> H >> W;
		forn(i,H)
		forn(j,W)
			cin >> h[i][j];
		memset(u,0,sizeof(u));
		forn(i,H)
		forn(j,W)
		{
			int optimo = INF;
			forn(z,4)
				optimo = min(optimo,alt(i+dx[z],j+dy[z]));
			if (optimo < alt(i,j))
			{
				forn(z,4)
				{
					int nx = i+dx[z];
					int ny = j+dy[z];
					int altitu = alt(nx,ny);
					if (altitu == optimo)
					{
						u[i][j][z] = 1;
						u[nx][ny][3-z] = 1;
						break;
					}
				}
			}
		}
		c = 'a';
		memset(m,0,sizeof(m));
		forn(i,H)
		forn(j,W)
		if (m[i][j] == 0)
		{
			flood_fill(i,j);
			c++;
		}
		printf("Case #%d:\n",tt+1);
		forn(i,H)
		{
			forn(j,W)
			{
				if (j)
					cout << " ";
				cout << m[i][j];
			}
			cout << endl;
		}
	}
	return 0;
}
