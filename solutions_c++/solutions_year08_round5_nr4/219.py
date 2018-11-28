#include <iostream>
#include <fstream>

using namespace std;
ifstream fin("D-small-attempt0.in");
ofstream fout("d.out");

bool can[200][200];
int f[200][200];
int n, m, r;
void init()
{
	int x, y;
	fin>>n>>m>>r;
	memset(can,true,sizeof(can));
	for (int i=0;i<r;i++)
	{
		fin>>x>>y;
		can[x-1][y-1]=false;
	}
}
void calc()
{
	int i, j;
	memset(f,0,sizeof(f));
	for (i=0;i<n;i++)
		for (j=0;j<m;j++)
			if (can[i][j])
		{
			if (i==0 && j==0) f[i][j]=1;
			if (i>=2 && j>=1) f[i][j]+=f[i-2][j-1];
			if (i>=1 && j>=2) f[i][j]+=f[i-1][j-2];
			f[i][j]%=10007;
		}
	fout<<f[n-1][m-1]<<endl;
}
int main()
{
	int t;
	fin>>t;
	for (int i=1;i<=t;i++)
	{
		init();
		fout<<"Case #"<<i<<": ";
		calc();
	}
	return 0;
}