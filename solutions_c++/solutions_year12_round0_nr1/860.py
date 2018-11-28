// Author: Zhang Kai (hapsunday@gmail.com)
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <ctime>
#include <climits>
#include <cfloat>
#include <cassert>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <utility>
#include <bitset>
#include <valarray>
#include <complex>
#include <numeric>
#include <iterator>
#include <functional>
#include <algorithm>
using namespace std;


#define ALL(A)		(A).begin(), (A).end()
#define CLR(A, v)	memset(A, v, sizeof(A));
#define FOR(i, N)	for(int i=0; i<(N); ++i)
#define MP(A, B)	make_pair(A, B)
#define TWO(i)		(i<32 ? 1U<<(i) : 1ULL<<(i))
#define CONTAIN(S,i)  (((S)&TWO(i)) != 0)
#define LEN(str)	((int)(str).length())
#define SIZE(v)		((int)(v).size())

#define VAR(v,t)	__typeof__(t) v=(t)
#define F0(i, n)	for(int i=0; i<(int)(n); ++i)
#define F1(i, n)	for(int i=1; i<=(int)(n); ++i)
#define F2(i, s, e)	for(int i=(int)(s); i<(int)(e); ++i)
#define FE(it, s)	for(VAR(it,(s).begin()); it!=(s).end(); ++it)

#define DEBUG_PRINT(x) fprintf(stderr, "%s:%d -->  %s = [%s]\n", \
					__FUNCTION__,__LINE__, #x, to_str(x).c_str());
// debug
#define debug(x)	DEBUG_PRINT(x)
#define trace(x)	fprintf(stderr, "%s:%d --> %s\n", __FUNCTION__,__LINE__, #x);


template<class T>inline int cMin(T& a, T b) {return b<a ? a=b,1 : 0;}
template<class T>inline int cMax(T& a, T b) {return a<b ? a=b,1 : 0;}
template<class T>inline string to_str(T v){ostringstream os;os<<v;return os.str();}

const double pi = acos(-1.0);
const double eps = 1e-9;

template<class T>inline T   isqr(T v) {return v*v;}
template<class T>inline T   iabs(T v) {return v<0?-v:v;}
template<class T>inline int isgn(T v) {return iabs(v)<=eps?0:(v<0?-1:1);}


typedef vector<int>		VI;
typedef vector<string>	VS;
typedef pair<int, int>	PII;

typedef long long i64;
typedef unsigned long long u64;
typedef int i32;
typedef unsigned int u32;

template<typename T>inline T next(){static char buf[64];scanf("%s",buf);
istringstream is(buf);T v;is>>v;return v;}
inline int nextInt(){int v=0;scanf("%d",&v);return v;}
/////////////////////////////////////////////


char* _IN[] = {
	"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"};

char* _OUT[] = {
	"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up"};

char to[128] = {0};
bool in_tag[128] = {false}, out_tag[128] = {false};

char buf[1024];

int  main(int argc, char* argv[]) {
	//ios::sync_with_stdio(false);
	debug("start ...");
	memset(to, 0, sizeof(to));
	F0(k, 3) for(int i=0; _IN[k][i]; ++i) {
		to[_IN[k][i]] = _OUT[k][i];
		in_tag[ _IN[k][i] ] = true;
		out_tag[ _OUT[k][i] ] = true;
	}
	int cnt_in = 0, cnt_out = 0;
	for(int i='a'; i<='z'; ++i) {
		cnt_in += (in_tag[i] ? 1 : 0);
		cnt_out += (out_tag[i] ? 1 : 0);
	}
	//for(int i='a'; i<='z'; ++i) {
	//	if(!in_tag[i]) printf("in_char  %c\n", (char)i);
	//	if(!out_tag[i]) printf("oo_char  %c\n", (char)i);
	//}
	debug(cnt_in);
	debug(cnt_out);
	//for(int i='a'; i<='z'; ++i) putchar(i);
	//putchar('\n');
	//for(int i='a'; i<='z'; ++i) putchar(to[i]);
	//putchar('\n');
	to['q'] = 'z';
	to['z'] = 'q';
	int T;
	scanf("%d", &T); while(getchar()!='\n');
	F1(IT, T) {
		gets(buf);
		// putchar('\n');
		//for(int i=0; buf[i]; ++i) putchar(buf[i]); putchar('\n');
		for(int i=0; buf[i]; ++i) buf[i]=(to[buf[i]]);
		//putchar(buf[strlen(buf)-1]);
		printf("Case #%d: %s\n", IT, buf);
		//putchar('\n');
	}
	debug("end !!!");
	return 0;
}

