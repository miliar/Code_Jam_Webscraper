#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <ctime>
#include <cassert>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <string>
#include <bitset>
#include <numeric>
#include <complex>
#include <utility>
#include <fstream>
#include <ostream>
#include <istream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <functional>
using namespace std;


#define CLR(a,v)	memset(a,v,sizeof(a))
#define MP(a,b)		make_pair(a,b)
#define SIZE(a)		((int)a.size())
#define LENGTH(a)	((int)a.length())
#define FOR(i,n)	for(int i=0; i<(n); ++i)


template<class T>inline int cMin(T& a, T b) {return b<a ? a=b,1 : 0;}
template<class T>inline int cMax(T& a, T b) {return a<b ? a=b,1 : 0;}
template<class T>inline string to_str(T v) {ostringstream os; os<<v; return os.str();}


typedef int int32;
typedef unsigned int uint32;
typedef long long int64;
typedef unsigned long long uint64;


char *input_file = "E:/google/CodeJam/CodeJam/C-large.in";
char *output_file = "E:/google/CodeJam/CodeJam/C-large.out";
const bool zzzz = true;

const int mod = 10000;
char *ss = "welcome to code jam";
int  nss = 19;
char  cs[512];
int  c[512][32];
int  adj[128][32], deg[128];

void pre_process() {
	int  i, j, k;
	CLR(deg, 0);
	for(i=0; i<nss; ++i)
		adj[ss[i]][deg[ss[i]]++] = i+1;
}

int calc() {
	CLR(c, 0);
	int  i, j, k, cnt=0;
	c[0][0] = 1;
	for(i=0; cs[i]; ++i) {
		for(j=0; j<deg[cs[i]]; ++j) {
			c[i+1][adj[cs[i]][j]] += c[i][adj[cs[i]][j]-1];
			c[i+1][adj[cs[i]][j]] %= mod;
		}
		for(j=0; j<nss; ++j)
			c[i+1][j] = (c[i+1][j] + c[i][j])%mod;
		cnt = (cnt + c[i+1][nss])%mod;
	}
	return cnt;
}

int main() {
	if(zzzz) {freopen(input_file, "r", stdin);freopen(output_file, "w", stdout);}
	pre_process();
	int  it, nt;
	scanf("%d", &nt);
	while(getchar() != '\n');
	for(it=1; it<=nt; ++it) {
		gets(cs);
		printf("Case #%d: %04d\n", it, calc());
	}
	return 0;
}

