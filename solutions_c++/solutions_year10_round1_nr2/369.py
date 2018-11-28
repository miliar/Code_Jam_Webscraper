#include <string>
#include <string.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <cassert>
using namespace std;

/*PREWRITTEN CODE BEGINS HERE*/

#define REP(i,n) for(int i=0,_n=(n); i<_n; ++i)
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; ++i)
#define RESET(a,c) memset(a,(c),sizeof(a))


/*PREWRITTEN CODE ENDS HERE*/
inline int RI() { int xx; scanf("%d",&xx); return xx; }
typedef long double LD;
const int INF = 1010000000;
const double EPS = 1e-9;
/*SOLUTION BEGINS HERE*/

int mem[260][110];
int D, I, M, N;
int t[110];

struct E{
	int val, poz, dst;
	E(){}
	E(int _val, int _poz, int _dst) : val(_val), poz(_poz), dst(_dst) {}
	bool operator<(const E&a) const {
		return dst > a.dst;
	}
};	
int dij()
{
	
	REP(i, 260) REP(j, 110) mem[i][j] = INF;
	priority_queue<E> pq;
	#define ADD(val, poz, dst) do{ if(mem[(val)][(poz)] > dst) { mem[(val)][(poz)] = (dst); pq.push( E((val), (poz), (dst))); } }while(0)
	

	REP(i, 256) ADD(i, 0, I);
	ADD(t[0], 1, 0);
	//REP(i, 256) ADD(i, 0,  abs(i-t[0]));
	int ret = INF;	
	
	while(!pq.empty()) {
		E e = pq.top(); pq.pop();
		int last = e.val, poz = e.poz, dst = e.dst;
		
		if(mem[last][poz] != dst) continue;
		if(poz == N) { ret = min(ret, dst); continue; }
		
		int diff = abs(last - t[poz]);
		if(diff <= M) ADD(t[poz], poz+1, dst);

		//usuniecie
		ADD(last, poz+1,  dst+D);

		//dodanie
		FOR(i,0, 255) if( abs(i-last) <= M) ADD(i, poz, dst + I);
		
		//zmiana last
		FOR(i, 0, 255) ADD(i, poz, dst + abs(last-i));
	
		
		FOR(i,0, 255) {
			if(abs(last-i) <= M)  ADD(i,poz+1, dst+abs(t[poz]-i)); //ret = min(ret, abs(t[poz]-i) + go(i, poz+1));
			if(abs(t[poz]-i) <= M) ADD(t[poz],poz+1, dst+abs(last-i)); //ret = min(ret, abs(last-i) + go(t[poz], poz+1));
		} 
		
	}

	return ret;
}
int go(int last, int poz)
{
	if(poz == N) return 0;
	int &ret = mem[last][poz];
	if(ret != -1) return ret;
	
	ret = D+go(last, poz+1);
	
	int diff = abs(last - t[poz]);
	if(diff <= M) ret = min(ret, go(t[poz], poz+1));

	FOR(i,0, 255) {
		if(abs(last-i) <= M) ret = min(ret, abs(t[poz]-i) + go(i, poz+1));
		if(abs(t[poz]-i) <= M) ret = min(ret, abs(last-i) + go(t[poz], poz+1));
	}
	
	if(M && diff > M) ret = min( ret,  ((diff+M-1)/M - 1) * I  + go(t[poz], poz+1));
	
	return ret;
}

int solve()
{
	scanf("%d %d %d %d", &D, &I, &M, &N);
	REP(i, N) scanf("%d", &t[i]);

	RESET(mem,-1);
	
	//if(D == 0 || I == 0 || M == 255 || N == 1) return 0;

	return dij();

	int ret = D*N;
	REP(i, N-1) ret = min(ret, D*i + go(t[i], i+1));
	return ret;
}
int main(void)
{
	int T = RI();
	FOR(i,1,T) {
		printf("Case #%d: %d\n", i, solve());
	}
	return (0);
}
