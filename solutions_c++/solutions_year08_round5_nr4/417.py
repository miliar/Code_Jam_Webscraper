/*
ID: ferromr1
PROG:
LANG: C++
*/
#include<cstdio>
#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include<stack>
#include<queue>
#include<string>
#include<algorithm>
#include<numeric>
#include<cstdlib>
#include<cmath>
#include<set>
#include<map>
#include<ctime>
#include<utility>
using namespace std;

#define pb push_back
#define mp make_pair
#define sz size()
#define all(qq) qq.begin(),qq.end()
#define rall(qq) qq.rbegin(),qq.rend()
#define clr(qq) memset((qq),0,sizeof(qq))
#define fill(qq) memset((qq),0x3F,sizeof(qq))
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define repd(i,n) for(int i=(int)(n-1);i>=0;i--)
#define rep2(i,a,b) for(int (i)=(int)(a);i<(int)(b);i++)
#define fore(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++)
#define rint(qq) int(floor(qq+0.5))
#define sqr(qq) ((qq) * (qq))
#define ll long long
#define inf 999999999
#define fi first
#define se second
#define MX 200
#define mod 10007

int t,n,m,r;
int mem[MX][MX];
bool zle[MX][MX];
int moves[][2]={2,1,1,2};


ll go(int x,int y)
{
	if (x>=n||y>=m) return 0;
	if (zle[x][y]) return 0;
	if (x==n-1&&y==m-1) {return 1;}
	if (mem[x][y]!=-1) {return mem[x][y];}
	ll ret=0;
	rep(i,2) ret=(ret+go(x+moves[i][0],y+moves[i][1]))%mod;
	return mem[x][y]=ret;
}

int main ()
{
	cin>>t;
	rep(cases,t)
	{
		memset(mem,-1,sizeof(mem));
		clr(zle);
		cin>>n>>m>>r;
		while(r--)
		{
			int a,b;
			cin>>a>>b;
			zle[a-1][b-1]=1;
		}
		ll ret=go(0,0);
		cout<<"Case #"<<cases+1<<": "<<ret<<endl;
	}
	return 0;
}

