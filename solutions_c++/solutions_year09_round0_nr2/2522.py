#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <queue>
#include <algorithm>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <set>
using namespace std;

const int INF=0xFFFFFF9;
char resmap[102][102];
char let='a';
int a[102][102];
bool mask[102][102];

pair<int,int> FindMaxIJ(int h,int w)
{
	pair<int,int> ij(-1,-1);	
	int max=-1;
	for (int i=1;i<=h;i++)
	{
		for (int j=1;j<=w;j++)
		{
			if (a[i][j]>max&&resmap[i][j]==0)
			{
				max=a[i][j];
				ij.first=i;
				ij.second=j;
			}
		}
	}
	return ij;
}

pair<int,int> FindMin(pair<int,int> ij)
{
	int min=10002;
	pair<int,int> tmp=ij;
	if (a[ij.first-1][ij.second]<min)
	{
		min=a[ij.first-1][ij.second];
		tmp.first=ij.first-1;
		tmp.second=ij.second;
	}
	if (a[ij.first][ij.second-1]<min)
	{
		min=a[ij.first][ij.second-1];
		tmp.first=ij.first;
		tmp.second=ij.second-1;
	}
	if (a[ij.first][ij.second+1]<min)
	{
		min=a[ij.first][ij.second+1];
		tmp.first=ij.first;
		tmp.second=ij.second+1;
	}
	if (a[ij.first+1][ij.second]<min)
	{
		min=a[ij.first+1][ij.second];
		tmp.first=ij.first+1;
		tmp.second=ij.second;
	}
	if (a[ij.first][ij.second]>a[tmp.first][tmp.second])
		return tmp;
	else
		return ij;
}
void voln(pair<int,int> ij)
{
	queue<pair<int,int> > q;
	pair<int,int> tmp;
	tmp=ij;
	q.push(ij);
	char col;
	while (true)
	{
		if (FindMin(tmp)!=tmp)
		{
			tmp=FindMin(tmp);
			q.push(tmp);
		}else
		{
			if (resmap[tmp.first][tmp.second]==0)
			{
				col=let;
				let++;
			}else
			{
				col=resmap[tmp.first][tmp.second];
			}
			break;
		}
	}
	while (!q.empty())
	{
		resmap[q.front().first][q.front().second]=col;
		q.pop();
	}
}
int main()
{
	freopen("B-small.in","r",stdin);
	freopen("B-small.out","w",stdout);
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	int t;
	cin >> t;
	for (int tc=0;tc<t;tc++)
	{
		int h,w;
		cin >> h >> w;
		let='a';	
		for (int i=0;i<102;i++)
		{
			for (int j=0;j<102;j++)
			{
				a[i][j]=10001;
				resmap[i][j]=0;
			}
		}
		for (int i=1;i<=h;i++)
		{
			for (int j=1;j<=w;j++)
			{
				cin >> a[i][j];
			}
		}
		queue<pair<int,int> > q;
		pair<int,int> mij=FindMaxIJ(h,w);
		while (mij.first!=-1)
		{
			voln(mij);
			mij=FindMaxIJ(h,w);
		}
		cout << "Case #"<<tc+1<<":\n";
		if (resmap[1][1]=='b')
		{
			for (int i=1;i<=h;i++)
			{
				for (int j=1;j<=w;j++)
				{
					if (resmap[i][j]=='a')
						resmap[i][j]='b';
					else
						resmap[i][j]='a';
				}
			}
		}
		for (int i=1;i<=h;i++)
		{
			for (int j=1;j<=w;j++)
			{
				if (j!=w)
					cout << resmap[i][j] << ' ';
				else
					cout << resmap[i][j] << endl;
			}
		}
	}

	return 0;
}