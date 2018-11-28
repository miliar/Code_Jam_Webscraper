#include <iostream>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

int H,W;
vector<vector<int> > alt;
vector<vector<int> > G;
vector<int> group;
vector<char> cc;

int xx[] = {-1,0,0,1};
int yy[] = {0,-1,1,0};

bool isgood(int x,int y)
{
	return (x>=0 && y>=0 && x<H && y<W);
}

void gor(int g)
{
	if(group[g] == g) return;
	gor(group[g]);
	group[g] = group[group[g]];
}

void gun(int g1,int g2)
{	
	gor(g1);
	gor(g2);
	group[group[g1]] = group[g2];
}

void process(int pid)
{
	cin >> H >> W;
	alt.resize(H);
	G.resize(H);
	group.clear();
	group.resize(H*W);
	for(int i=0;i<H;i++)
	{
		alt[i].resize(W);
		G[i].resize(W);
		for(int j=0;j<W;j++)
		{
			cin >> alt[i][j];
			G[i][j] = i*W+j;
			group[G[i][j]]=G[i][j];
		}
	}

	for(int i=0;i<H;i++)
	{
		for(int j=0;j<W;j++)
		{
			int minalt = alt[i][j];
			int nnx,nny;
			for(int k=0;k<4;k++)
			{
				int nx = i + xx[k];
				int ny = j + yy[k];
				if(!isgood(nx,ny)) continue;
				if(minalt > alt[nx][ny])
				{
					minalt = alt[nx][ny];
					nnx = nx;
					nny = ny;
				}
			}
			if(minalt < alt[i][j])
			{
				gun(G[i][j], G[nnx][nny]);
			}
		}
	}

	cc.clear();
	cc.resize(50000,0);
	char chr = 'a';

	cout << "Case #" << pid << ":" << endl;
	for(int i=0;i<H;i++)
	{	
		for(int j=0;j<W;j++)
		{
			gor(G[i][j]);
			int gro = group[G[i][j]];
			if(cc[gro] == 0)
			{
				cc[gro] = chr++;
			}
			cout << (char)cc[gro] << " ";
		}
		cout << endl;
	}
}

int main(void)
{
	int N;
	cin >> N;
	for(int i=0;i<N;i++)
	{
		process(i+1);
	}
}
