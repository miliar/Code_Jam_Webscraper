#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<fstream>
using namespace std;
#define pi 3.141592653589793

#define ABS(x) ((x)>0?(x):-(x))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define DIST(x,y) ABS((x)-(y))
int gcd(int x,int y){if(y==0)return x;else return(gcd(y,x%y));}

int main()
{
	ifstream fin ("input.in");
	ofstream fout ("output.out");
	int c,n,m,t,x,y;
	//vector <vector <int> > shake;
	//vector <vector <int> > malt;
	vector <vector <pair<int,int> > > v;
	vector <int> ans;
	fin >>c;
	for (int i = 0; i < c; i++)
	{
		//shake.clear();
		//malt.clear();
		ans.clear();
		fin >> n >> m;
		ans.resize(n);
		v.clear();
		//shake.resize(m);
		//malt.resize(m);
		v.resize(m);
		for (int j = 0; j < m; j++)
		{
			fin >> t;
			//shake[j].resize(t);
			//malt[j].resize(t);
			for (int k = 0; k < t; k++)
			{
				fin >>x>>y;
				v[j].push_back(make_pair(y,x-1));
				//shake[j][k] = x-1;
				//malt[j][k] = y-1;
			}
			sort(v[j].begin(),v[j].end());
		}

		//Iterate
		int l;
		for (l = 0; l < m; l ++)
		{
			int p;
			for (p = 0; p < v[l].size(); p++)
			{
				if (ans[v[l][p].second] == v[l][p].first)
					break;
			}
			if (p == v[l].size())
			{
				if (v[l][p-1].first == 0)
					break;
				else
				{
					ans[v[l][p-1].second] = 1;	//malted
					l = -1;
					continue;
				}
			}
		}
		if (l != m)
		{
			fout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
		}
		else
		{
			fout << "Case #" << i + 1 << ": " ;
			for (int z = 0; z < n; z++)
				fout <<ans[z] << " ";
			fout <<endl;
		}
	}
	return 0;
}