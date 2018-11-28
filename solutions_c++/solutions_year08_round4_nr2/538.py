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
#define LD long double

int t,n,m,AA;
LD A;

int main ()
{
	cin>>t;
	rep(cases,t)
	{
		cin>>n>>m>>AA;
		A=(LD)AA/(LD)2.;
		A*=A;
		cout<<"Case #"<<cases+1<<": ";
		rep(i,n+1) rep(j,m+1)
		{
			rep(ii,n+1) rep(jj,m+1)
			{
				LD a=sqrt((LD)sqr(i)+sqr(j));
				LD b=sqrt((LD)sqr(ii)+sqr(jj));
				LD c=sqrt((LD)sqr(i-ii)+sqr(j-jj));
				LD s=(a+b+c)/(LD)2.;
				LD S=s*(s-a)*(s-b)*(s-c);
				if (abs(S-A)<1e-11)
				{
					cout<<"0 0 "<<i<<" "<<j<<" "<<ii<<" "<<jj<<endl;
					goto dalsi;
				}
			}
		}
		cout<<"IMPOSSIBLE"<<endl;
dalsi:;
	}
	return 0;
}
