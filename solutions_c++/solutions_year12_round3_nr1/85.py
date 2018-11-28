#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <algorithm>
#include <stack>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int n;
vector< vector<int> > g;
vector<bool>	v;
bool found;

void visit(int i)
{
	int j;
	if(v[i])
	{
		found = true;
		return;
	}
	v[i] = true;
	for(j=0; j<g[i].size(); ++j)
		visit(g[i][j]);
}

bool solve(int i)
{
	int j;
	for(j=0; j<n; ++j)
		v[j] = false;
	found = false;
	visit(i);
	return found;
}

int main()
{
	int t,k,i,j,m;
	fin>>t;
	for(k=1; k<=t; ++k)
	{
		g.clear();
		fin>>n;
		g.resize(n);
		v.resize(n);
		for(i=0; i<n; ++i)
		{
			fin>>m;
			g[i].resize(m);
			for(j=0; j<m; ++j)
			{
				fin>>g[i][j];
				g[i][j]--;
			}
		}

		bool yes=false;
		for(i=0; i<n; ++i)
			if(solve(i))
			{
				yes = true;
				break;
			}

		fout<<"Case #"<<k<<": ";
		if(yes)
			fout<<"Yes"<<endl;
		else
			fout<<"No"<<endl;
	}

	return 0;
}