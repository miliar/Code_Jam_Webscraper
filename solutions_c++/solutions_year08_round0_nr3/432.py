//C. Fly Swatter.cpp 

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <string>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <assert.h>

using namespace std;

const double pi=acos(-1.0);
const double eps=1e-11;

#define SZ(X) ((int)(X.size()))
#define MP(A,B) make_pair(A,B)
#define FOR(i,b,e) for(int i = b;i < e;++i)
#define RE(i,n) FOR(i,0,n)

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))>0)
#define containL(S,X) (((S)&twoL(X))>0)
int64 toInt64(string s){int64 r=0;istringstream sin(s);sin>>r;return r;} 
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;} 
string toString(int64 v){ostringstream sout;sout<<v;return sout.str();} 
string toString(int v){ostringstream sout;sout<<v;return sout.str();} 

template<class T> inline T countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
template<class T> inline T lowbit(T n){return (n^(n-1))&n;}
template<class T> inline T sqr(T x){return x * x;}
template<class T> inline T gcd(T a,T b){if(a < 0) return gcd(-a,b); if(b < 0) return gcd(a,-b); return (b == 0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b){return a*(b/gcd(a,b));}
template<class T> void out(T A[],int n){for(int i = 0;i < n;++i) cout << A[i] << " ";cout << endl;}
template<class T> void out(vector<T> A,int n = -1){if(n==-1) n = A.size();for(int i = 0;i < n;++i) cout << A[i] << " ";cout << endl;}

int ncase;
double f,R,t,r,g;
double res;

double getS(double x,double y)
{
	double tangle = asin(x/R);
	double s =  R * R * tangle / 2;
	
	s += x * y /2;
	return s;
}
void solve()
{
	double cyc = (pi * R * R - pi * sqr(R - t - f))/4;
	R = R - t - f;

	double x1 = g + r - f,x2 = min(x1 + 2 * (f + r),R),y1 = 0,y2 = 0;
	double mem = 0;
	int cnt = 0;
	int cnts = 0;
	while(x1 < R)
	{
		y1 = sqrt(sqr(R) - sqr(x1));
		y2 = sqrt(sqr(R) - sqr(x2));

		double s1,s2,s;
		s1 = getS(x1,y1);
		s2 = getS(x2,y2);
		s = s2 - s1;
				
		mem += s;

		x1 += g + 2 * r;
		x2 = min(x1 + 2 * (f + r),R);
		
		cnt = cnt + (y1 + y2)/2/(g + 2 * r);
		cnts++;
	}
	x1 = r + f;
	y1 = sqrt(sqr(R) - sqr(x1));
	mem += getS(x1,y1);
	mem *= 2;
	mem = mem - cnt * sqr(2 * (r + f)) - (2 * cnts) * sqr(2 * (r + f)) / 2 - sqr(2 * (r + f))/4;
	
	R = R + t + f;

	res = (cyc + mem)/(pi * R * R / 4);
	//assert(res <= 1);

}
int main() 
{
	//freopen("C-small-attempt0.in","r",stdin);
	//freopen("C-small-attempt0.out","w",stdout);

	//freopen("C-large.in","r",stdin);
	//freopen("C-large.out","w",stdout);

	cin >> ncase;
	FOR(i,1,ncase + 1)
	{
		cout << "Case #" << i << ": ";
		cin >> f >> R >> t >> r >> g;
		if(2 * f >= g) res = 1.0;
		else
		{
			solve();
		}
		cout << res << endl;
	}
	return 0;
}
