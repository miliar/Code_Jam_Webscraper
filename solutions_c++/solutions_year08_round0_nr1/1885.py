#include <fstream>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int N;
	fin>>N;
	for(int c=0;c<N;c++)
	{
		int S;
		fin>>S;
		fin>>ws;
		map<string,int> E;
		for(int e=0;e<S;e++)
		{
			string name;
			getline(fin,name);
			E[name] = e;
		}
		
		int Q;
		fin>>Q;
		fin>>ws;
		int query[2000];
		for(int i=0;i<Q;i++)
		{
			string name;
			getline(fin,name);
			query[i] = E[name];
		}
		
		int m[2000][100];
		memset(m,0,sizeof(m));
		
		for(int i=0;i<Q;i++)
		{
			for(int j=0;j<S;j++)
			{
				if(query[i] == j)
				{
					m[i+1][j] = 2000;
					continue;
				}
				int min = 2000;
				for(int k=0;k<S;k++)
				{
					int s = (k==j)?m[i][k]:m[i][k]+1;
					min = min<s ? min : s;
				}
				m[i+1][j] = min;
			}
		}
		fout<<"Case #"<<(c+1)<< ": " <<*min_element(m[Q],m[Q]+S)<<endl;
	}
	return 0;
}
