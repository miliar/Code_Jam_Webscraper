#include <iostream>
#include <fstream>

using namespace std;
ifstream fin("B-large.in");
//ifstream fin("p2.txt");
ofstream fout("p2.ans");

int type[2000][3000];
int mult[2000][3000];
int ans[2000];
int num[2000];
int n, m;

void init()
{	

	fin>>n>>m;
	for (int i=0;i<m;i++)
	{
		fin>>num[i];
		for (int j=0;j<num[i];j++)
		{
			fin>>type[i][j]>>mult[i][j];
			type[i][j]--;
		}
	}
}
void calc()
{
	bool finish=false;
	memset(ans,0,sizeof(ans));
	while (!finish)
	{
		finish=true;
		for (int i=0;i<m;i++)
		{
			int j;
			for (j=0;j<num[i];j++)
				if (mult[i][j]==ans[type[i][j]]) break;
			if (j>=num[i])
			{
				for (j=0;j<num[i];j++)
					if (mult[i][j]==1)
						if (ans[type[i][j]]==1)
						{
							fout<<"IMPOSSIBLE\n";
							return;
						}
						else 
						{
							ans[type[i][j]]=1;
							finish=false;
							break;
						}
				if (j>=num[i])
				{
												fout<<"IMPOSSIBLE\n";
							return;
				}
			}
		}
	}
	for (int i=0;i<n;i++)
	{
		if (i) fout<<' ';
		fout<<ans[i];
	}
	fout<<endl;			
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
}