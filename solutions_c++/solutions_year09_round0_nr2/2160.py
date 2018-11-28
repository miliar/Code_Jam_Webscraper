
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;


char m[10000][10000];
char vis[100][100];
int hb[100][100];
int h,w;
void dfs(int y,int x,char cc)
{
	vis[y][x]=cc;
	int index=y*100+x;
	if(y>0 && m[index][index-100] && !vis[y-1][x])
		dfs(y-1,x,cc);
	if(y+1<h && m[index][index+100] && !vis[y+1][x])
		dfs(y+1,x,cc);
	if(x>0 && m[index][index-1] && !vis[y][x-1])
		dfs(y,x-1,cc);
	if(x+1<w && m[index][index+1] && !vis[y][x+1])
		dfs(y,x+1,cc);
}
int main()
{
	ifstream inf("B-large.in");
	ofstream outf("out.txt");
	int T;
	inf>>T;
	for(int t=0;t<T;t++)
	{
		inf>>h>>w;
		for(int i=0;i<h;i++)
			for(int j=0;j<w;j++)
				inf>>hb[i][j];
		//Çåm
		memset(m,0,sizeof(m));
		for(int i=0;i<h;i++)
		{
			for(int j=0;j<w;j++)
			{
				int liu=0;
				int low=hb[i][j];
				if(i>0 && hb[i-1][j]<low)
				{
					liu=-100;
					low=hb[i-1][j];
				}
				if(j>0 && hb[i][j-1]<low)
				{
					liu=-1;
					low=hb[i][j-1];
				}
				if(j+1<w && hb[i][j+1]<low)
				{
					liu=1;
					low=hb[i][j+1];
				}
				if(i+1<h && hb[i+1][j]<low)
				{
					liu=100;
					low=hb[i+1][j];
				}
				int index=i*100+j;
				m[index][index+liu]=1;
				m[index+liu][index]=1;
			}
		}
		//Çåvis
		memset(vis,0,sizeof(vis));
		int sc='a';
		for(int i=0;i<h;i++)
			for(int j=0;j<w;j++)
				if(!vis[i][j])
					dfs(i,j,sc++);
		outf<<"Case #"<<t+1<<":"<<endl;
		for(int i=0;i<h;i++)
		{
			for(int j=0;j<w-1;j++)
			{
				outf<<vis[i][j]<<" ";
			}
			outf<<vis[i][w-1];
			outf<<endl;
		}
	}
	return 0;
}