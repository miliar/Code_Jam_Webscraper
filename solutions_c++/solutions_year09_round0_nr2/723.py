#include <stdio.h>
#include <algorithm>
#include <string>
#include <iostream>
#include <memory.h>

using namespace std;

#define MAXD 110
#define INF 1000000000

int mat[MAXD][MAXD];
pair<int,int> base[MAXD][MAXD];
int lab[MAXD][MAXD];

bool cmp(const pair<int,int>& p1,const pair<int,int>& p2)
{
	if (mat[p1.first][p1.second]!=mat[p2.first][p2.second])
		return mat[p1.first][p1.second]<mat[p2.first][p2.second];
	if (p1.first!=p2.first)
		return p1.first<p2.first;
	return p1.second<p2.second;
}

pair<int,int> get_sink(int i,int j)
{
	if (mat[i][j-1]>=mat[i][j] && mat[i][j+1]>=mat[i][j]
	&&	mat[i-1][j]>=mat[i][j] && mat[i+1][j]>=mat[i][j])
		return make_pair(i,j);
	pair<int,int> pii[4];
	pii[0]=make_pair(i,j-1);
	pii[1]=make_pair(i,j+1);
	pii[2]=make_pair(i+1,j);
	pii[3]=make_pair(i-1,j);
	sort(pii,pii+4,cmp);
	return get_sink(pii[0].first,pii[0].second);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	int h,w;
	cin>>t;
	for (int k=0;k<t;k++)
	{
		memset(lab,0,sizeof(lab));
		cin>>h>>w;
		for (int i=0;i<=h+1;i++)
			mat[i][0]=mat[i][w+1]=INF;
		for (int i=0;i<=w+1;i++)
			mat[0][i]=mat[h+1][i]=INF;
		for (int i=1;i<=h;i++)
			for (int j=1;j<=w;j++)
				cin>>mat[i][j];
		for (int i=1;i<=h;i++)
		{
			for (int j=1;j<=w;j++)
			{
				if (mat[i][j-1]>=mat[i][j] && mat[i][j+1]>=mat[i][j]
				&&	mat[i-1][j]>=mat[i][j] && mat[i+1][j]>=mat[i][j])
				{
					base[i][j]=make_pair(i,j);
					continue;
				}
				base[i][j]=get_sink(i,j);
			}
		}
		char c='a';
		for (int i=1;i<=h;i++)
		{
			for (int j=1;j<=w;j++)
			{
				if (lab[base[i][j].first][base[i][j].second]==0)
					lab[base[i][j].first][base[i][j].second]=lab[i][j]=c++;
				else
					lab[i][j]=lab[base[i][j].first][base[i][j].second];
			}
		}
		cout<<"Case #"<<k+1<<":\n";
		for (int i=1;i<=h;i++)
		{
			cout<<(char)lab[i][1];
			for (int j=2;j<=w;j++)
				cout<<' '<<(char)lab[i][j];
			cout<<endl;
		}
	}
	return 0;
}