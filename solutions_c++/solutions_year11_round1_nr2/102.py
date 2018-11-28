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

const int NN = 10000+8;
const int NLL = 12;


int   ch_idx[128];
i64   power[12];

struct  State
{
	char  str[12];
	int   mask;
	int   point;
	int   idx;
	i64   val;

	void  clear() {
		point = 0;
		val = 0;
	}
}dic[NLL][NN];


int  Best_Ln, Best_Idx, Best_Point, Best_P;


int   dic_n[NLL], dic_mask[NLL];


int   z[2][12][NN], z_n[2][12];

char  ts[32];

int  cur, pre;
map<i64, int>  mask[NLL];

i64  do_it(State& s, char c) {
	if(! ( s.mask & TWO(c-'a') ) ) {
		++s.point; return s.val;
	}
	for(int i=0; s.str[i]; ++i) if(s.str[i] == c)
		s.val += power[i] * ch_idx[c];
	return  s.val;
}

void  calc(char c) {
	cur^=1;  pre^=1;
	for(int i=0; i<NLL; ++i) {
		z_n[cur][i] = 0;  //mask[i].clear();
	}
	map<i64, int>  hash[NLL];
	for(int i=0; i<NLL; ++i) for(int j=0; j<z_n[pre][i]; ++j) {
		State&  s = dic[i][ z[pre][i][j] ];
		int  tmask = mask[i][s.val];
		if(tmask & TWO(c-'a')) hash[i][do_it( s , c)]++;
		else {
			hash[i][s.val]++;
		}
		if((s.point == Best_Point && s.idx < Best_P) || s.point > Best_Point) {
			Best_Ln = i;
			Best_Idx = z[pre][i][j];
			Best_Point = s.point;
			Best_P = s.idx;
		}
	}
	for(int i=0; i<NLL; ++i) mask[i].clear();
	for(int i=0; i<NLL; ++i) for(int j=0; j<z_n[pre][i]; ++j) {
		State&  s = dic[i][ z[pre][i][j] ];
		if( hash[i][ s.val ] > 1 ) {
			z[cur][i][ z_n[cur][i]++ ] = z[pre][i][j];
			mask[i][ s.val ] |= s.mask;
		}
	}
}

void  go() {
	Best_Point = -1;
	cur = 0; pre = 1;
	CLR(z_n, 0);
	for(int i=0; i<NLL; ++i) mask[i].clear();
	for(int i=0; i<NLL; ++i) for(int j=0; j<dic_n[i]; ++j) {
		z[cur][i][ z_n[cur][i]++ ] = j;
		mask[i][ dic[i][j].val ] |= dic[i][j].mask;
	}
	for(int k=0; ts[k]; ++k)
		calc(ts[k]);
	printf(" %s", dic[Best_Ln][Best_Idx].str);
}

int  main() {
	int  testcase;
	freopen("input.in" , "r", stdin);
	freopen("output.out" , "w", stdout);

	for(int i='a'; i<='z'; ++i) ch_idx[i] = i-'a'+1;
	ch_idx[0] = 0;
	power[0] = 1;
	for(int i=1; i<NLL; ++i) power[i] = power[i-1] * 27;

	//printf("ch_idx[z] = %d\n", ch_idx['z']);

	scanf("%d", &testcase);
	FOR(it, 1, testcase) {

		int  N, M;
		scanf("%d%d", &N, &M);

		CLR(dic_n, 0);
		CLR(dic_mask, 0);
		
		for(int i=0; i<N; ++i) {
			scanf("%s", ts);
			int  tn = strlen(ts);
			strcpy(dic[tn][dic_n[tn]].str, ts);
			dic[tn][dic_n[tn]].idx = i;

			int  tmp = 0;
			for(int j=0; j<tn; ++j) tmp |= TWO(ts[j]-'a');
			dic[tn][dic_n[tn]].mask = tmp;

			dic_n[tn]++;
		}
		printf("Case #%d:", it);

		while(M--) {
			scanf("%s", ts);
			for(int i=0; i<NLL; ++i) for(int j=0; j<dic_n[i]; ++j)
				dic[i][j].clear();
			go();
		}
		putchar('\n');
	}
	return 0;
}

