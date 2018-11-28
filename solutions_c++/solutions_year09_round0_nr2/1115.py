#define _CRT_SECURE_NO_WARNINGS
#include <ctime>
#include <cfloat>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <complex>

using namespace std;

#define pb push_back
#define L(s) (int)((s).end()-(s).begin())
#define rep(i,n) for(int (i)=0;(i)<(n);++(i))
#define all(s) (s).begin(),s.end()
#define pi 3.1415926535897932384626433832795
#define vi vector<int>
#define inf 1000000000
#define ll long long
#define C(a) memset((a),0,sizeof((a)))
#pragma comment(linker, "/STACK:16777216")
int dx[4]={-1,0,0,1};
int dy[4]={0,-1,1,0};
int n,m,t;
char a[100][100];
int h[100][100];
int mini[100][100];
char mn;
char fin;
bool ok(int x,int y)
{
	return (x>=0&&y>=0&&x<n&&y<m);
}
void dfs1(int i,int j)
{
	if (mini[i][j]>=h[i][j])
		return;
	for(int k=0;k<4;++k)
	{
		int p=i+dx[k];
		int q=j+dy[k];
		if (ok(p,q)&&h[p][q]==mini[i][j])
		{
			if (a[p][q]=='z'+1)
				dfs1(p,q);
			else
				mn=min(mn,a[p][q]);
			return;
		}
	}
}
void dfs2(int i,int j)
{
	a[i][j]=mn;
	if (mini[i][j]>=h[i][j])
		return;
	for(int k=0;k<4;++k)
	{
		int p=i+dx[k];
		int q=j+dy[k];
		if (ok(p,q)&&h[p][q]==mini[i][j])
		{
			dfs2(p,q);
			return;
		}
	}
}
int main()
{	
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	for(int test=1;test<=t;++test)
	{
		cin>>n>>m;
		for(int i=0;i<n;++i)
			for(int j=0;j<m;++j)
			{
				cin>>h[i][j];
				a[i][j]='z'+1;
				mini[i][j]=inf;
			}
		for(int i=0;i<n;++i)
			for(int j=0;j<m;++j)
				for(int k=0;k<4;++k)
				{
					int p=i+dx[k];
					int q=j+dy[k];
					if (ok(p,q)&&h[p][q]<mini[i][j])
						mini[i][j]=h[p][q];
				}
		fin='a';
		for(int i=0;i<n;++i)
			for(int j=0;j<m;++j)
				if (a[i][j]=='z'+1)
				{
					mn=fin;
					dfs1(i,j);
					if (mn==fin)
						++fin;
					dfs2(i,j);
				}
		cout<<"Case #"<<test<<":"<<endl;
		for(int i=0;i<n;++i)
			for(int j=0;j<m;++j)
			{
				cout<<a[i][j];
				if (j<m-1)
					cout<<" ";
				else
					cout<<endl;
			}
	}
	return 0;
}