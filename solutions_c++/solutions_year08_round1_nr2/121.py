#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define INF 1e9
using namespace std;
vector <pair<int,int> > a[2020];
int w[2010];
int n, m;
int is_ok()
{
	int ok, i, j;
	for (i=0;i<m;i++)
	{
		ok=0;
		for (j=0;j<a[i].size();j++)
		{
			if (w[a[i][j].first]==a[i][j].second)
			{
				ok=1;
				break;
			}
		}
		if (!ok)
			return i;
	}
	return -1;
}
int proc(int k)
{
	int i, j;
	for (i=0;i<a[k].size();i++)
	{
		if (a[k][i].second==1)
		{
			w[a[k][i].first]=1;
			return 0;
		}
	}
	return -1;
}
int main()
{
	ifstream fin("a.in");
	ofstream fout("a.out");
	int i, j, k, l, t, T, p;
	fin>>T;
	for (t=1;t<=T;t++)
	{
		fin>>n>>m;
		for (i=0;i<n;i++)
			w[i]=0;
		for (i=0;i<m;i++)
		{
			a[i].clear();
			fin>>l;
			for (j=0;j<l;j++)
			{
				fin>>k>>p;
				a[i].push_back(pair<int,int>(k-1,p));
			}
		}
		int ok=1;
		while(1)
		{
			l=is_ok();
			if (l==-1)
				break;
			if (proc(l)==-1)
			{
				ok=0;
				break;
			}
		}
		if (!ok)
			fout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
		else
		{
			fout<<"Case #"<<t<<":";
			for (i=0;i<n;i++)
				fout<<" "<<w[i];
			fout<<endl;
		}
	}
	fin.close();
	fout.close();
	return 0;
}