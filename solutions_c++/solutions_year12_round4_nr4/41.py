#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}//NOTES:checkmin(
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}//NOTES:checkmax(
#define SIZE(x) ((int)(x).size())
#define for0(i,n) for(int i=0;i<(n);i++)
#define for1(i,n) for(int i=1;i<=(n);i++)
#define for0r(i,n) for(int i=(n)-1;i>=0;i--)
#define for1r(i,n) for(int i=(n);i>=1;i--)
typedef long long ll;
typedef pair<int,int> PII;


char d[70][70];
int v[70][70];
int X,Y;
int cc[10];
set<PII> P[10];
int R,C;

int ux[3]={1,0,0};
int uy[3]={0,-1,1};

set<set<PII>> F[10];

int doo(int k,set<PII> W)
{
	F[k].insert(W);
	for0(u,3)
	{
		set<PII> Q;
		int f=1;
		for(set<PII>::iterator it=W.begin();it!=W.end();it++)
		{
			int nx=it->first+ux[u];
			int ny=it->second+uy[u];
			if(d[nx][ny]=='#')
			{
				Q.insert(*it);
				continue;
			}
			if(!(v[nx][ny]>>k&1))
			{
				f=0;
				break;
			}
			Q.insert(make_pair(nx,ny));
		}
		if(f==0)continue;
		if(Q.size()==1)return 1;
		if(F[k].count(Q)==0)
		{
			if(doo(k,Q))return 1;
		}
	}
	return 0;
}

void solve()
{	
	scanf("%d %d",&R,&C);
	for0(i,R)
	{
		for0(j,C)
		{
			scanf(" %c",&d[i][j]);
		}
	}
	memset(v,0,sizeof(v));
	memset(cc,0,sizeof(cc));
	for0(i,10)
	{
		P[i].clear();
		F[i].clear();
	}
	for0r(i,R-1)
	{
		for0(j,C)
		{
			if(d[i][j]=='#')continue;
			v[i][j]=v[i+1][j];
			if(isdigit(d[i][j]))
			{
				int c=d[i][j]-'0';
				v[i][j]|=1<<c;
			}
		}
		for0(j,C-1)
		{
			if(d[i][j+1]=='#')continue;
			v[i][j+1]|=v[i][j];
		}
		for0r(j,C-1)
		{
			if(d[i][j]=='#')continue;
			v[i][j]|=v[i][j+1];
		}
		for0(j,C)
		{
			for0(k,10)
			{
				if(v[i][j]>>k&1)
				{
					cc[k]++;
					P[k].insert(make_pair(i,j));
				}
			}
		}
	}
	for0(i,10)
	{
		if(!cc[i])continue;
		printf("%d: %d ",i,cc[i]);
		bool f=doo(i,P[i]);
		puts(f?"Lucky":"Unlucky");
	}
}

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	int T,Tc=0;
	scanf("%d",&T);
	while(++Tc<=T)
	{
		printf("Case #%d:\n",Tc);
		solve();
	}
	return 0;
}