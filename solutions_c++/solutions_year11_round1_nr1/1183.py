// include file
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <ctime>

#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <bitset>

#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <list>
#include <functional>

using namespace std;

// typedef
typedef __int64 ll;

// 
#define read freopen("A-small-attempt1.in","r",stdin)
#define write freopen("out.txt","w",stdout)

const double eps = 1e-6;
const double INFf = 1e100;
const int INFi = 1000000000;
const double Pi = acos(-1.0);

template<class T> inline T sqr(T a){return a*a;}
template<class T> inline T TMAX(T x,T y)
{
	if(x>y) return x;
	return y;
}
template<class T> inline T TMIN(T x,T y)
{
	if(x<y) return x;
	return y;
}
template<class T> inline T MMAX(T x,T y,T z)
{
	return TMAX(TMAX(x,y),z);
}
template<class T> inline T MMIN(T x,T y,T z)
{
	return TMIN(TMIN(x,y),z);
}
template<class T> inline void SWAP(T &x,T &y)
{
	T t = x;
	x = y;
	y = t;
}


// code begin
int T;
ll N,Pd,Pg,D,G,Dwin,Dall;

ll gcd(ll a,ll b)
{
	if(b==0) return a;
	return gcd(b,a%b);
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	int cas=1;
	while(T--)
	{
		scanf("%I64d %I64d %I64d",&N,&Pd,&Pg);
		
		ll gd = gcd(Pd,100);
		ll bx = 100/gd;
		Dall = N - N%bx;
		Dwin = (Dall*Pd)/100;
		
		ll x = Pg - Dwin;
		ll y = 100- Dall;

		// x+Pg*t
		// y+100*t
		
		bool f = false;
		
		if( Pg==0)
		{
			if( Pd==0 ) f = true;
		}
		else if(Pg==100)
		{
			if(Pd==100) f=true;
		}
		else{
			f = true;
		}
		if(Dall ==0 ) f=false;

		if(f) printf("Case #%d: Possible\n",cas++);
		else printf("Case #%d: Broken\n",cas++);
	}

	return 0;
}