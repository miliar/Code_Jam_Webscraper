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
#define MX 13

int t,n,m;
char M[MX][MX];
int mem[MX][1<<MX];
int ans;

int go(int x,int y,int maska,int mam)
{
	if (x==n+1) {ans=max(ans,mam);return 0;}
	if (x>1&&y==1)
	{
		if (mem[x][maska]!=-1) return mem[x][maska];
	}
	int ret=0,nx,ny,nmaska;
	nx=y==m?x+1:x;ny=y==m?1:y+1;nmaska=((maska<<1)&((1<<m)-1));
	if (M[x][y]=='x') ret=go(nx,ny,nmaska,mam);
	else
	{
		ret=go(nx,ny,nmaska,mam);
		if (M[x][y]!='x')
		{
			//cout<<"kladiem "<<x<<" "<<y<<endl;
			bool a,b,c,d;
			a=b=c=d=0;
			if (M[x][y+1]=='x') a=1;
			if (M[x][y-1]=='x') b=1;
			if (M[x+1][y+1]=='x') c=1;
			if (M[x+1][y-1]=='x') d=1;
			M[x][y+1]='x';
			M[x][y-1]='x';
			M[x+1][y+1]='x';
			M[x+1][y-1]='x';
			nmaska|=1<<(y-1);
			ret=max(ret,go(nx,ny,nmaska,mam+1)+1);
			if (!a) M[x][y+1]='.';
			if (!b) M[x][y-1]='.';
			if (!c) M[x+1][y+1]='.';
			if (!d) M[x+1][y-1]='.';
		}
	}
	if (x>1&&y==1)
	{
		//cout<<x<<" "<<y<<" "<<maska<<endl;
		mem[x][maska]=ret;
	}
	return ret;
}

int f(int x,int maska)
{
	if (x==n) return 0;
	if (mem[x][maska]!=-1) return mem[x][maska];
	int ret=0;
	rep(i,1<<m)
	{
		rep(j,m) if (((1<<j)&i)&&M[x][j]=='x') goto dalsi;
		rep(j,m-1) if (((1<<j)&i)&&((1<<(j+1))&i)) goto dalsi;
		rep(j,m-1) if (((1<<j)&i)&&((1<<(j+1))&maska)) goto dalsi;
		rep(j,m-1) if (((1<<j)&maska)&&((1<<(j+1))&i)) goto dalsi;
		ret=max(ret,f(x+1,i)+__builtin_popcount(i));
dalsi:;
	}
	return mem[x][maska]=ret;
}

int main ()
{
	cin>>t;
	rep(cases,t)
	{
		cin>>n>>m;
		ans=0;
		rep(i,n) rep(j,m) cin>>M[i][j];
		memset(mem,-1,sizeof(mem));
		cout<<"Case #"<<cases+1<<": "<<f(0,0)<<endl;
	}
	return 0;
}

