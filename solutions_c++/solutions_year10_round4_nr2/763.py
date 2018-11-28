#include <algorithm> 
#include <cassert>
#include <cctype> 
#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
#include <cstring> 
#include <iostream>
#include <map> 
#include <set> 
#include <string> 
#include <sstream>
#include <queue> 
#include <vector> 
using namespace std;

int T, P, ans;
vector <int> M;
vector <vector<int> > pr;

void read()
{
	scanf("%d", &P);
	int pp=1;
	for (int i=0; i<P; i++)
		pp*=2;
	int tm;
	M.clear();
	for (int i=0; i<pp; i++)
	{
		scanf("%d", &tm);
		M.push_back(tm);
	}
	pr.clear();
	vector<int> tmp;
	for (int i=0; i<P; i++)
	{
		tmp.clear();
		pp/=2;
		for (int j=0; j<pp; j++)
		{
			scanf("%d", &tm);
			tmp.push_back(tm);
		}
		pr.push_back(tmp);
	}
}


void solve()
{
	int pp=1;
	for (int i=0; i<P; i++)
		pp*=2;
	vector <int> tmp;
	tmp.resize(pp,0);
	vector<vector<int> > mat;
	mat.resize(P,tmp);
	int tt;
	for (int i=0; i<M.size(); i++)
	{
		tt=pp;
		for (int j=P-1; j>=M[i]; j--)
		{
			mat[j][i/tt]=1;
			tt/=2;
		}
	}
	ans=0;
	for (int i=0; i<mat.size();i++)
		for (int j=0; j<mat[i].size();j++)
			ans+=mat[i][j];


}

void write(int i)
{
	printf("Case #%d: %d\n",i,ans);


}
int main()
{
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	char buf[1000];
	string s;


	scanf("%d",&T);
	


	for (int i=0; i<T; i++)
	{
		read();
		solve();
		write(i+1);
	}
	return 0;
}
