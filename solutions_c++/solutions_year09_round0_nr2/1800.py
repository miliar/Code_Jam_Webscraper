#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;
int v[101][101];
int a[101][101];
int n, m;
int has_edge(pair<int,int> p1, pair<int,int> p2)
{
	if (p2.first >= n || p2.first < 0)
		return 0;
	if (p2.second >= m || p2.second < 0)
		return 0;
	int mi = 10000000;
	int kx, ky;
	if (p2.first > 0)
		if (v[p2.first - 1][p2.second] < mi)
		{
			mi = v[p2.first - 1][p2.second];
			kx=p2.first - 1;
			ky=p2.second;
		}
	if (p2.second > 0)
		if (v[p2.first][p2.second - 1] < mi)
		{
			mi = v[p2.first][p2.second - 1];
			kx=p2.first;
			ky=p2.second - 1;
		}
	if (p2.second < m-1)
		if (v[p2.first][p2.second + 1] < mi)
		{
			mi = v[p2.first][p2.second + 1];
			kx=p2.first;
			ky=p2.second + 1;
		}
	if (p2.first < n-1)
		if (v[p2.first + 1][p2.second] < mi)
		{
			mi = v[p2.first + 1][p2.second];
			kx=p2.first + 1;
			ky=p2.second;
		}
	if (mi >= v[p2.first][p2.second])
		return 0;
	if (kx == p1.first && ky==p1.second)
		return 1;
	return 0;
}
int is_sink(pair<int,int> p)
{
	pair<int,int> p2;
	p2.first = p.first;
	p2.second = p.second + 1;
	if (has_edge(p2,p))
		return 0;
	p2.first = p.first;
	p2.second = p.second - 1;
	if (has_edge(p2,p))
		return 0;
	p2.first = p.first + 1;
	p2.second = p.second;
	if (has_edge(p2,p))
		return 0;
	p2.first = p.first - 1;
	p2.second = p.second;
	if (has_edge(p2,p))
		return 0;
	return 1;
}
int bfs(int x, int y, int lab)
{
	int i, j;
	int d[110][110];
	for (i=0;i<n;i++)
		for (j=0;j<m;j++)
			d[i][j]=1e6;
	d[x][y]=0;
	queue<pair<int,int> > q;
	pair<int,int> p,p2;
	p.first=x;
	p.second=y;
	q.push(p);
	while(!q.empty())
	{
		p=q.front();
		q.pop();
		a[p.first][p.second] = lab;
		p2.first=p.first + 1;
		p2.second=p.second;
		if (has_edge(p,p2) && d[p2.first][p2.second] > d[p.first][p.second] + 1)
		{
			q.push(p2);
			d[p2.first][p2.second] = d[p.first][p.second] + 1;
		}
		p2.first=p.first - 1;
		p2.second=p.second;
		if (has_edge(p,p2) && d[p2.first][p2.second] > d[p.first][p.second] + 1)
		{
			q.push(p2);
			d[p2.first][p2.second] = d[p.first][p.second] + 1;
		}
		p2.first=p.first;
		p2.second=p.second + 1;
		if (has_edge(p,p2) && d[p2.first][p2.second] > d[p.first][p.second] + 1)
		{
			q.push(p2);
			d[p2.first][p2.second] = d[p.first][p.second] + 1;
		}
		p2.first=p.first;
		p2.second=p.second - 1;
		if (has_edge(p,p2) && d[p2.first][p2.second] > d[p.first][p.second] + 1)
		{
			q.push(p2);
			d[p2.first][p2.second] = d[p.first][p.second] + 1;
		}
	}
	return 0;
}
char c[101][101];
int main()
{
	int i, j, k, l, d, res;
	int ch[50];
	int T;
	ifstream fin("b.in");
	ofstream fout("b.out");
	fin>>T;
	for (int t=1;t<=T;t++)
	{
		fin>>n>>m;
		memset(a,0,sizeof(a));
		for (i=0;i<n;i++)
			for (j=0;j<m;j++)
				fin>>v[i][j];
		k=0;
		for (i=0;i<n;i++)
			for (j=0;j<m;j++)
			{
				pair<int,int> p;
				p.first=i;
				p.second=j;
				if (is_sink(p))
					bfs(i,j,k++);
			}
		k=0;
		for (i=0;i<50;i++)
			ch[i]=-1;
		for (i=0;i<n;i++)
			for (j=0;j<m;j++)
			{
				if (ch[a[i][j]] == -1)
				{
					ch[a[i][j]]=k++;
					c[i][j]=k-1+'a';
				}
				else
					c[i][j]=ch[a[i][j]]+'a';
			}
		fout<<"Case #"<<t<<":"<<endl;
		for (i=0;i<n;i++)
		{
			for (j=0;j<m;j++)
				fout<<c[i][j]<<" ";
			fout<<endl;
		}
	}
	fin.close();
	fout.close();
	return 0;
}
