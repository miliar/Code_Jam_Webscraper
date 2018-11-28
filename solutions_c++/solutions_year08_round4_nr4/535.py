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

int t,n;
string s,r;
int p[20];
int ret;

int main ()
{
	cin>>t;
	rep(cases,t)
	{
		cout<<"Case #"<<cases+1<<": ";
		cin>>n>>s;
		rep(i,n) p[i]=i;
		ret=inf;
		do
		{
			int pom=1;
			r=s;
			rep(i,s.sz)
			{
				rep(j,n) r[i+j]=s[i+p[j]];
				i+=n-1;
			}
			char posl=r[0];
			rep(i,r.sz) if (r[i]!=posl) posl=r[i],pom++;
			ret=min(ret,pom);
		} while(next_permutation(p,p+n));
		cout<<ret<<endl;
	}
	return 0;
}
