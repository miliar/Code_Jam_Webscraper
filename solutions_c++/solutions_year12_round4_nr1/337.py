//In the name of Allah
//
//
//////////////////////
// Program: 
// Written By Alireza Farhadi (LGM)
//////////////////////
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cctype>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <utility>
#include <vector>
#include <bitset>
#include <deque>
#include <iomanip>
#include <complex>
#include <fstream>
#include <sstream>
#include <map>
//#include <climits>
//#include <list>

using namespace std;

#if ( _WIN32 || __WIN32__ )
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

#define show(x) cerr<<((#x))<<" = "<<((x))<<" "<<endl
#define bit(a,b) (((a)>>(b))&1)
#define gcd __gcd
#define endl '\n'
#define bcnt(x) ((__builtin_popcount(x)))
#define sz(x) ((int((x).size())))
#define sqr(x) ((((x))*((x))))
#define fx(x) fixed<<setprecision(x)

template<class T> inline void smn(T &a,const T &b){if(b<a) a=b;}
template<class T> inline void smx(T &a,const T &b){if(b>a) a=b;}
template<class T> inline T rev(const T & a){T _=a; reverse(_.begin(),_.end()); return _;}

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pie;

const double eps=1e-9;
const ld leps=1e-14;
const int MN=10000+10;
pie list[MN];
bool m1[MN][MN],m2[MN][MN];
bool d1[MN][MN];
int d2[MN][MN];
int t,n,D,tc=0;
int f[MN];
int sum(int,int);
bool f1(int a,int b)
{
	if (m1[a][b])
		return d1[a][b];
	m1[a][b]=1;
	bool & res=d1[a][b];
	int t=list[b].first-list[a].first;
	smn(t,list[b].second);
	if (D-list[b].first<=t) return res=1;
	int tmp=upper_bound(f+1,f+n+1,list[b].first+t)-f-1;
	if (tmp>b)
		if (sum(b,b+1)-sum(b,tmp+1)>0)
			return res=1;
	return res=0;
}
int sum(int a,int b)
{
	if (m2[a][b])
		return d2[a][b];
	m2[a][b]=1;
	if (b>=n+1) return d2[a][b]=0;
	return d2[a][b]=f1(a,b)+sum(a,b+1);
}
int main(int argc,char * argv[])
{
	ios_base::sync_with_stdio(false);
	cin>>t;
	while (t-->0)
	{
		tc++;
		memset(m1,0,sizeof(m1));
		memset(m2,0,sizeof(m2));
		cin>>n;
		list[0].first=0;
		for (int i=1;i<=n;i++)
			cin>>list[i].first>>list[i].second;
		for (int i=1;i<=n;i++)
			f[i]=list[i].first;
		cin>>D;
		bool av=false;
		av=f1(0,1);
		cout<<"Case #"<<tc<<": "<<(av?"YES":"NO")<<endl;
	}
	return 0;
}
