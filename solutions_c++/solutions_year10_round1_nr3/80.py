#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

/* Prewritten code begins */
#define PII         pair<int,int>
#define MP          make_pair
#define FOR(i,a,b)  for(int i=(a); i<=(b); ++i)
#define LL          long long
/* Prewritten code ends */

map<PII,bool> mem;
int aa[1000001] = {0,0};
int small[1024][1024];
int g(int a, int b);
int f(int a, int b) {
	if(a>b) swap(a,b);
	if(a == 1) return b!=1;
	PII t = MP(a,b);
	if(mem.count(t)) return mem[t];
	FOR(k,1,(a-1)/b) if(!g(a-k*b,b)) return mem[t] = 1;
	FOR(k,1,(b-1)/a) if(!g(a,b-k*a)) return mem[t] = 1;
	return mem[t] = 0;
}
int g(int a, int b) {
	if(a>b) swap(a,b);
	if(a == 1) return b != 1;
	if(b<1024) return small[a][b];
	return f(a,b);
}
int h(int x, int b1, int b2) {
	if(x<b1) return 0;
	if(x>b2) return b2-b1+1;
	return x-b1+1;
}
int main() {
	int T, A1, A2, B1, B2;
	int mx = 1000000;
	LL res;
	FOR(i,1,1023) FOR(j,i+1,1023) small[i][j] = f(i,j);
	FOR(i,2,mx) {
		mem.clear();
		aa[i] = aa[i-1];
		while(g(i,aa[i]+1)) aa[i]++;
	}
	scanf("%d",&T);
	FOR(cs,1,T) {
		scanf("%d%d%d%d",&A1,&A2,&B1,&B2);
		mem.clear(); res = 0;
		FOR(a,A1,A2) res += h(aa[a],B1,B2);
		FOR(b,B1,B2) res += h(aa[b],A1,A2);
		printf("Case #%d: %lld\n",cs,res);
	}
	return 0;
}
