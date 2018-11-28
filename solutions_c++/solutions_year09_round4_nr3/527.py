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
#include <bitset>

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
int tests;
bool c[100][100];
bool on[100];
int n,m;
int y[100][30];
int cnt[100];
int f[1<<16];
int dfs(int X)
{
	if (f[X]!=inf)
		return f[X];
	vector<int> pos;
	for(int i=0;i<n;++i)
		if (X&(1<<i))
			pos.pb(i);
	int k=L(pos);
	bool ok=true;
	for(int i=0;i<k&&ok;++i)
		for(int j=i+1;j<k&&ok;++j)
			if (c[pos[i]][pos[j]])
				ok=false;
	if (ok)
	{
		f[X]=1;
		return 1;
	}
	for(int Y=1;Y<(1<<k)-1;++Y)
	{
		int P=0,Q=0;
		for(int i=0;i<k;++i)
			if (Y&(1<<i))
				P|=(1<<pos[i]);
			else
				Q|=(1<<pos[i]);
		f[X]=min(f[X],dfs(P)+dfs(Q));
	}
	return f[X];
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output2.txt","w",stdout);
	cin>>tests;
	for(int test=1;test<=tests;++test)
	{
		cin>>n>>m;
		for(int i=0;i<n;++i)
			for(int j=0;j<m;++j)
				cin>>y[i][j];
		if (test<=tests/2)
			continue;
		C(c);
		for(int i=0;i<n;++i)
			for(int j=i+1;j<n;++j)
				for(int k=0;k<m-1;++k)
				{
					ll val=(ll)(y[i][k]-y[j][k])*(ll)(y[i][k+1]-y[j][k+1]);
					if (val<=0)
						c[i][j]=c[j][i]=true;
				}
		for(int i=0;i<(1<<n);++i)
			f[i]=inf;
		cout<<"Case #"<<test<<": "<<dfs((1<<n)-1)<<endl;
	}
	return 0;
}
