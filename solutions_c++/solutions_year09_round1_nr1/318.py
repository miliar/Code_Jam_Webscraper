#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <climits>
#include <ctime>
#include <cfloat>
#include <cassert>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <deque>
#include <vector>
#include <bitset>
#include <string>
#include <complex>
#include <utility>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <iostream>
#include <valarray>
#include <algorithm>
#include <functional>
using namespace std;

typedef int i32;
typedef unsigned int u32;
typedef long long i64;
typedef unsigned long long u64;

#define two(i)		(1<<(i))
#define towL(i)		(1LL<<(i))
#define CLR(a,v)	memset(a,v,sizeof(a))
#define MP(a,b)		make_pair(a,b)
#define SIZE(a)		((int)a.size())
#define LENGTH(a)	((int)a.length())
#define REP(i,n)	for(u32 i=0; i<(n); ++i)
#define REPD(i,n)	for(int i=(n)-1; i>=0; --i)
#define FOR(i,s,e)	for(int i=(s); i<=(e); ++i)
#define FORD(i,s,e)	for(int i=(s); i>=(e); --i)


template<class T>inline int cMin(T& a, T b) {return b<a ? a=b,1 : 0;}
template<class T>inline int cMax(T& a, T b) {return a<b ? a=b,1 : 0;}
template<class T>inline string to_str(T v) {ostringstream os; os<<v; return os.str();}

const double  pi = acos(-1.0);
const double  eps = 1e-6;

template<class T>inline T sqr(T v) {return v*v;}
template<class T>inline T iabs(T v) {return v<0?-v:v;}
template<class T>inline int sgn(T v) {return iabs(v)<eps?0:(v<0?-1:1);}
template<class T>inline T lowbit(T n) {return v^(v&(v-1));}
template<class T>inline int count_bit(T n) {int c=0;for(;n; n&=n-1)++c;return c;}
template<class T>inline T gcd(T a, T b)
	{if(a<b) {a^=b;b^=a;a^=b;} while(b) {a%=b;a^=b;b^=a;a^=b;}return a;}
template<class T>inline T lcm(T a, T b) {return a/gcd(a,b)*b;}
/*Given a and b, compute gcd(a,b) = ax + by*/
template<typename T>
T  exgcd(T a, T b, T &x, T &y){
	if(a < 0) {
		T  d = exgcd(b, a, y, x);
		x = -x;  return  d;
    }
	if(b == 0) {x=1; y=0; return a;}
	T  d = exgcd(b, a%b, y, x);
	y -= (a/b)*x;
	return  d;
}

template<class T>inline T mod_inverse(T a, T n)
	{T x,y; exgcd(a,n,x,y); return (x%n+n)%n;}

inline int isPrime(int n) {int i;
	if(n==2)return 1; if(n<2 || !(n&1))return 0;
	for(i=3;i*i<=n;i+=2)if(n%i==0)return 0;return 1;}

char *input_file = "E:/google/CodeJam/CodeJam/A-large.in";
char *output_file = "E:/google/CodeJam/CodeJam/A-large.out";
const bool zzzz = true;


char tag[600000][12];
char is[10240];
int  a[10], na, B;
int  q[1000000], qn;
u32  K[1024];


inline u32 value(u32 v, u32 b) {
	int ans=0;
	while(v>0) {
		ans += sqr(v%b);
		v /= b;
	} return ans;
}

inline bool happy(u32 v, u32 b) {
	qn = 0;
	if(v < 600000) {
		if(tag[v][b] == 2) return true;
		if(tag[v][b] == 1) return false;
		tag[v][b] = 3; q[qn++]=v;
	}
	for(;;) {
		//if(v<300000) q[qn++] = v;
		v = value(v, b);
		//assert(v<300000);
		if(v<600000) {
			//printf("v=%d b=%d  tag=%d\n", v, b, (int)tag[v][b]);
			//system("pause");
			if(tag[v][b]) break;
			tag[v][b] = 3;
			q[qn++] = v;
		}
	}
	//printf("c=%d\n", (int)tag[v][b]);
	char &c = tag[v][b];
	if(c == 3) c=1;
	REP(i, qn) tag[q[i]][b] = c;
	return c==2;
}

inline bool isOK(u32 v) {
	//printf("isOK  v=%d\n", v);
	REP(i, na)
		if(!happy(v, a[i]))
			return false;
	return true;
}

inline u32 calc(int a[], int na) {
	
}

int main() {
	if(zzzz) {freopen(input_file, "r", stdin);freopen(output_file, "w", stdout);}
	//FILE *fout = fopen("E:/zhk.out", "w");
	CLR(tag, 0);
	REP(i, 11) tag[1][i] = 2;
	u32 bit, bit_end = 1<<9, ans, i;
	for(bit=1; bit<bit_end; ++bit) {
		if(bit>=504) {K[bit] = 11814485; continue;}
		na = 0; for(i=0; i<9; ++i) if(bit&(1u<<i)) a[na++] = i+2;
		ans = 2; while(!isOK(ans)) ++ans;
		K[bit] = ans;
		//printf("%u  %u\n", bit, ans);
		//fprintf(fout, "%u %u\n", bit, ans);
	}
	int  T;
	scanf("%d", &T);
	while(getchar() != '\n');
	REP(Ti, T) {
		/*gets(is);*/
		na = 0;
		u32 mask=0;
		while(1) {
			scanf("%d", a+na++);
			mask |= two(a[na-1]-2);
			int c=getchar();
			while(c==' ') c=getchar();
			if(isdigit(c)) {
				ungetc(c, stdin);
				continue;
			}
			break;
		}
		printf("Case #%d: %u\n", Ti+1, K[mask]);
		/*sort(a, a+na);
		na = unique(a, a+na)-a;
		if(mask>=504) {
			printf("Case #%d: %d\n", Ti+1, 11814485);
			continue;
		}
		u32 ans=2;
		while(!isOK(ans))
			++ans;
		printf("Case #%d: %u\n", Ti+1, ans);*/
	}
	return 0;
}

