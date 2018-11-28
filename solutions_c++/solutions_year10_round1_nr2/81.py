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
#define MP          make_pair
#define FOR(i,a,b)  for(int i=(a); i<=(b); ++i)
#define REP(i,n)    for(int i=0; i<(n); ++i)
#define FILL(a,v)   memset(a,v,sizeof(a))
#define PII         pair<int,int>
#define Y           second
#define X           first
/* Prewritten code ends */

const int maxN = 302;
int D, I, M, N;
int a[maxN];
int mem[maxN][maxN];
typedef pair<int,pair<int,int> > P3;
priority_queue<P3,vector<P3>,greater<P3> > q;
void PUSH(int pos, int last, int cc) {
	if(mem[pos][last]>cc) {
		mem[pos][last] = cc;
		q.push(MP(cc,MP(pos,last)));
	}
}
int main() {
	int T;
	scanf("%d",&T);
	FOR(cs,1,T) {
		scanf("%d%d%d%d",&D,&I,&M,&N);
		REP(i,N) scanf("%d",&a[i]);
		FILL(mem,0x7f);
		pair<int,PII> t;
		while(!q.empty()) q.pop();
		PUSH(0,256,0);
		while(!q.empty()) {
			t = q.top(); q.pop();
			int tp = t.Y.X, tl = t.Y.Y;
			if(tp == N) { break; }
			if(abs(tl-a[tp])<=M) PUSH(tp+1,a[tp],t.X);
			//ins
			REP(i,256) if(abs(i-tl)<=M) PUSH(tp,i,t.X+I);
			//del
			REP(i,256) PUSH(tp+1,tl,t.X+D);
			//chg
			REP(i,256) if(abs(tl-i)<=M) PUSH(tp+1,i,t.X+abs(i-a[tp]));
			if(tl == 256) REP(i,256) PUSH(tp+1,i,t.X+abs(i-a[tp]));
		}
		printf("Case #%d: %d\n",cs,t.X);
	}
	return 0;
}
