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
const int MN=1000+100;
int r[MN];
int p[MN];
bool av[MN];
pie temp[MN];
pie cor[MN];
int w,h,n,t,tc;
int x,y;
int mx;
int main(int argc,char * argv[])
{
	ios_base::sync_with_stdio(false);
	cin>>t;
	while (++tc<=t)
	{
		cin>>n>>w>>h;
		for (int i=0;i<n;i++)
			cin>>r[i],av[i]=1;
		for (int i=0;i<n;i++) temp[i]=pie(r[i],i);
		sort(temp,temp+n,greater<pie> ());
		for (int i=0;i<n;i++) p[i]=temp[i].second;
		x=y=mx=0;
		bool con=true;
		while (con)
		{
			con=false;
			for (int i=0;i<n;i++) if (av[p[i]])
				if (y<=h)
				{
					con=true;
					smx(mx,x+2*r[p[i]]);
					cor[p[i]]=pie(x,y);
					av[p[i]]=false;
					y+=2*r[p[i]];
					break;
				}
			if (con==false && mx!=x)
			{
				x=mx;y=0;
				con=true;
			}
		}
		cout<<"Case #"<<tc<<": ";
		for (int i=0;i<n;i++)
			cout<<fixed<<setprecision(1)<<(double)cor[i].first<<" "<<(double)cor[i].second<<" ";
		cout<<endl;
	}
	return 0;
}
