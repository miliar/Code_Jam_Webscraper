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
#define fl endl<<flush

template<class T> inline void smn(T &a,const T &b){if(b<a) a=b;}
template<class T> inline void smx(T &a,const T &b){if(b>a) a=b;}
template<class T> inline T _rev(const T & a){T _=a; reverse(_.begin(),_.end()); return _;}

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pie;
typedef pie pii;
typedef complex<double> point;

const double eps=1e-8;
const ld leps=1e-14;
const int MN=10;
int t,tc;
char mp[MN][MN];
bool check(char a)
{
	for (int i=0;i<4;i++)
	{
		bool same=true;
		for (int j=0;j<4;j++) if (mp[i][j]!=a && mp[i][j]!='T') same=false;
		if (same) return 1;
	}
	for (int i=0;i<4;i++)
	{
		bool same=true;
		for (int j=0;j<4;j++) if (mp[j][i]!=a && mp[j][i]!='T') same=false;
		if (same) return 1;
	}
	bool same=true;
	for (int i=0;i<4;i++) if (mp[i][i]!=a && mp[i][i]!='T') same=false;
	if (same) return 1;
	same=true;
	for (int i=0;i<4;i++) if (mp[i][3-i]!=a && mp[i][3-i]!='T') same=false;
	if (same) return 1;
	return 0;
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin>>t; tc=1;
	while (t-->0)
	{
		for (int i=0;i<4;i++) for (int j=0;j<4;j++) cin>>mp[i][j];
		cout<<"Case #"<<tc++<<": ";
		if (check('X')) 
		{
			cout<<"X won"<<endl;
			goto hell;
		}
		if (check('O'))
		{
			cout<<"O won"<<endl;
			goto hell;
		}
		for (int i=0;i<4;i++) for (int j=0;j<4;j++) if (mp[i][j]=='.')
		{
			cout<<"Game has not completed"<<endl;
			goto hell;
		}
		cout<<"Draw"<<endl;
hell:;
	}
	return 0;
}

