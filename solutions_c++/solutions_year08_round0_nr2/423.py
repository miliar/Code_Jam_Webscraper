//B. Train Timetable.cpp 

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

const int SCALE = 60 * 24;
int a[SCALE];
int b[SCALE];
int ncase;
int t,na,nb;
int resa,resb;

void solve()
{
	memset(a,0,sizeof(a));
	memset(b,0,sizeof(b));
	resa = 0,resb = 0;
	string str;
	set <int> mem;
	RE(i,na)
	{
		string sh,sm;
		int ih,im;

		cin >> str;
		sh = str.substr(0,2);
		sm = str.substr(3);	
		ih = toInt(sh);
		im = toInt(sm);
		a[ih * 60 + im]--;
		mem.insert(ih * 60 + im);

		cin >> str;		
		sh = str.substr(0,2);
		sm = str.substr(3);	
		ih = toInt(sh);
		im = toInt(sm);
		if(ih * 60 + im + t < SCALE) b[ih * 60 + im + t]++,mem.insert(ih * 60 + im + t);

	}

	RE(i,nb)
	{
		string sh,sm;
		int ih,im;

		cin >> str;
		sh = str.substr(0,2);
		sm = str.substr(3);	
		ih = toInt(sh);
		im = toInt(sm);
		b[ih * 60 + im]--;
		mem.insert(ih * 60 + im);

		cin >> str;		
		sh = str.substr(0,2);
		sm = str.substr(3);	
		ih = toInt(sh);
		im = toInt(sm);
		if(ih * 60 + im + t < SCALE) a[ih * 60 + im + t]++,mem.insert(ih * 60 + im + t);
	}
	int acnt = 0;
	int bcnt = 0;
	set <int> ::iterator it;
	for(it = mem.begin();it != mem.end();++it)
	{
		int tmp;
		tmp = (*it);
		tmp = a[*it];
		acnt += tmp;
		tmp = b[*it];
		bcnt += tmp;
		/*acnt += a[*it];
		bcnt += b[*it];*/
		resa = min(resa,acnt);
		resb = min(resb,bcnt);
	}
	resa = -resa;
	resb = -resb;
}
int main() 
{

	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);

	cin >> ncase;
	FOR(i,1,ncase + 1)
	{
		cout << "Case #" << i << ": ";
		cin >> t >> na >> nb;
		solve();
		cout << resa << " " << resb << endl;
	}
	return 0;
}
