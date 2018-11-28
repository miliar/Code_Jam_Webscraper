
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

int  com[256][256];
int  opp[256][256];
char  tmpStr[1024];
char  os[1024];
int  osn;

int  main() {
	int  testcase;
	freopen("J:/Downloads/B-large.in" , "r", stdin);
	//freopen("J:/Downloads/B-small-attempt0.in" , "r", stdin);
	freopen("A-large.out" , "w", stdout);
	scanf("%d", &testcase);
	FOR(it, 1, testcase) {
		CLR(com, -1);
		CLR(opp, 0);
		int  C;
		scanf("%d", &C);
		REP(i, C) {
			scanf("%s", tmpStr);
			com[tmpStr[0]][tmpStr[1]] = tmpStr[2];
			com[tmpStr[1]][tmpStr[0]] = tmpStr[2];
		}
		int  D;
		scanf("%d", &D);
		REP(i, D) {
			scanf("%s", tmpStr);
			opp[tmpStr[1]][tmpStr[0]] = 1;
			opp[tmpStr[0]][tmpStr[1]] = 1;
		}
		int  N;
		scanf("%d", &N);
		scanf("%s", tmpStr);
		osn = 0;
		REP(i, N) {
			os[osn++] = tmpStr[i];
			if(osn>1 && com[ os[osn-2] ][ os[osn-1] ] >= 0) {
				os[osn-2] = com[ os[osn-2] ][ os[osn-1] ];
				osn--;
			}
			else {
				for(int i=0; i+1<osn; ++i) {
					if(opp[ os[i] ][ os[osn-1] ]) {
						osn = 0; break;
					}
				}
			}
		}
		printf("Case #%d: [", it);
		for(int i=0; i<osn; ++i) {
			if(i) printf(", ");
			putchar(os[i]);
		} printf("]\n");
	}
	return 0;
}

