
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>
#include <time.h>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <bitset>
#include <vector>
#include <deque>
#include <utility>
#include <complex>
#include <list>
#include <sstream>
#include <iostream>
#include <functional>
#include <numeric>
#include <algorithm>
#include <iomanip>
using namespace std;


template<class T>inline T iabs(const T& v) {return v<0 ? -v : v;}
template<class T>inline T strTo(string s){istringstream is(s);T v;is>>v;return v;}
template<class T>inline string toStr(const T& v){ostringstream os;os<<v;return os.str();}
template<class T>inline int cMin(T& a, const T& b){return b<a?a=b,1:0;}
template<class T>inline int cMax(T& a, const T& b){return a<b?a=b,1:0;}
template<class T>inline int cBit(T n){return n?cBit(n&(n-1))+1:0;}


#define DEBUG(a)     printf("%s = %s\n", #a, toStr(a).c_str())


#define TWO(i)       (1<<(i))
#define CONTAIN(s,i) (((s)>>(i))&1)
#define MP(a,b)      make_pair(a,b)
#define CLR(arr,v)   memset(arr, v, sizeof(arr))
#define FOR(i,s,e)   for(int i(s),__(e); i<=__; ++i)
#define FORD(i,s,e)  for(int i(s),__(e); i>=__; ++i)
#define REP(i,n)     for(int i(0),__(n); i< __; ++i)
#define REPD(i,n)    for(int i((n)-1);   i>= 0; --i)

typedef int i32;
typedef unsigned int u32;
typedef long long i64;
typedef unsigned long long u64;
typedef pair<int,int>  PII;
typedef vector<int>    VI;

vector<int>  type, pos, npos;

int  cp[2], zz[2];

int  go(int tp, int pp) {
	if(iabs(pp - cp[tp]) <= zz[tp])
		cp[tp] = pp;
	else cp[tp] += (pp < cp[tp] ? -zz[tp] : zz[tp]);
	zz[tp] = 0;

	int  tt = iabs(pp - cp[tp]) + 1;

	cp[tp] = pp;
	zz[tp^1] += tt;

	return tt;

}

int  main() {
	int  testcase;
	freopen("J:/Downloads/A-large.in" , "r", stdin);
	freopen("A-large.out" , "w", stdout);
	scanf("%d", &testcase);
	FOR(it, 1, testcase) {
		int  N;
		scanf("%d", &N);
		char  dummy[4];
		int  tmp;

		zz[0] = zz[1] = 0;
		cp[0] = cp[1] = 1;
		int  ans = 0;
		REP(i, N) {
			scanf("%s%d", dummy, &tmp);
			if(dummy[0] == 'O') ans += go(0, tmp);
			else ans += go(1, tmp);
		}
		
		printf("Case #%d: %d\n", it, ans);
	}
	return 0;
}

