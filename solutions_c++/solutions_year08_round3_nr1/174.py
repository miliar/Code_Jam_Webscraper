// pro1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

//#if defined (__GNUC__) && (__GNUC__ <= 2)
//#include <hash_map>
//#include <hash_set>
//#else
//#include <ext/hash_map>
//#include <ext/hash_set>
//using namespace __gnu_cxx;
//#endif
using namespace std;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }
const int mn=1001;
int p,k,l;
int a[mn];
int main()
{
	//freopen("test.txt","r",stdin);
	/*freopen("A-small1.in","r",stdin);
	freopen("A-small1.out","w",stdout);*/
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int cs;
	cin>>cs;
	for(int cases=1;cases<=cs;cases++)
	{
		cin>>p>>k>>l;
		REP(i,l)
			cin>>a[i];
		sort(a,a+l,greater<int>());
		__int64 s=0;
		int mul=1;
		for(int i=0;i<l;i+=k)
		{
			for(int j=0;j<k;j++)
				if(i+j<l) s+=mul*a[i+j];
			mul++;
		}
		if(p*k>=l) cout<<"Case #"<<cases<<": "<<s<<endl;
		else cout<<"Impossible"<<endl;
	}
	return 0;
}

