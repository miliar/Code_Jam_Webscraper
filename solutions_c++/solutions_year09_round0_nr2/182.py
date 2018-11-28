#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

bool marked[105][105];

int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};
int height[105][105];

char ret[105][105];

int H, W;

char ch;

bool inb(int r, int c)
{
	return (r>=0 && r<H && c>=0 && c<W);
}

void go(int r, int c)
{
	vector<pair<int,int> > vp;
	while(true)
	{
		vp.push_back(pair<int,int>(r,c));
		
		int lowest = height[r][c], nr=-1, nc=-1;
		for(int i=0; i<4; i++)	if(inb(r+dx[i],c+dy[i]) && height[r+dx[i]][c+dy[i]] < lowest)
		{
			lowest = height[r+dx[i]][c+dy[i]];
			nr = r+dx[i];
			nc = c+dy[i];
		}
		if(nr == -1 && !marked[r][c])
		{
			for(int i=0; i<vp.size(); i++)
			{
				ret[vp[i].first][vp[i].second] = ch;
				marked[vp[i].first][vp[i].second] = true;
			}
			ch++;
			return;
		}
		else if(nr == -1 && marked[r][c])
		{
			for(int i=0; i<vp.size(); i++)
			{
				ret[vp[i].first][vp[i].second] = ret[r][c];
				marked[vp[i].first][vp[i].second] = true;
			}
			return;
		}
		else if(marked[nr][nc])
		{
			for(int i=0; i<vp.size(); i++)
			{
				ret[vp[i].first][vp[i].second] = ret[nr][nc];
				marked[vp[i].first][vp[i].second] = true;
			}
			return;
		}
		r = nr;
		c = nc;
	}
}

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-small.txt");
	
	int T;
	fin>>T;
	for(int tt=0; tt<T; tt++)
	{
		fin>>H>>W;
		for(int i=0; i<H; i++)	for(int j=0; j<W; j++)	marked[i][j] = false;
		for(int i=0; i<H; i++)	for(int j=0; j<W; j++)	fin>>height[i][j];
		ch = 'a';
		for(int i=0; i<H; i++)	for(int j=0; j<W; j++)	if(!marked[i][j])
			go(i,j);
		
		fout<<"Case #"<<tt+1<<":\n";
		for(int i=0; i<H; i++)
		{
			for(int j=0; j<W; j++)
			{
				fout<<ret[i][j];
				if(j<W-1)	fout<<" ";
			}
			fout<<"\n";
		}
	}
	
	return 0;
}
