#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <cmath>
#include <set>
#include <cassert>
#include <cstdio>
#include <queue>
using namespace std;
#define LET(x,a) __typeof(a) x(a)
#define FOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define EACH(it,v) FOR(it,(v).begin(),(v).end())
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define GI ({int t;scanf("%d",&t);t;})
#define GII ({LL t;scanf("%Ld",&t);t;})
#define INF (int)1e8
#define MAX 55
#define mkp make_pair
typedef long long LL;
typedef double D;
#define sz size()
#define bset(i,j) (((1)<<(j))&(i))
int main()
{
	int runs=GI, caseno=1;
	while(runs--) {
		int t=GI, na=GI, nb=GI;
		vector < pair<int,int> > va, vb;
		REP(i,na) {
			int a, b, c, d;
			scanf("%d:%d %d:%d", &a, &b, &c, &d);
			va.pb(mkp(b+a*60, d+c*60));
		}
		REP(i,nb) {
			int a, b, c, d;
			scanf("%d:%d %d:%d", &a, &b, &c, &d);
			vb.pb(mkp(b+a*60, d+c*60));
		}
		sort(va.begin(), va.end());
		sort(vb.begin(), vb.end());
		int ansa=na, ansb=nb, done[na>?nb];
		memset(done, 0, sizeof(done));
		REP(i,na) REP(j,nb) {
			if(!done[j] && vb[j].first >= va[i].second + t) {
				done[j] = 1;
				ansb--;
				break;
			}
		}			
		memset(done, 0, sizeof(done));
		REP(i,nb) REP(j,na) {
			if(!done[j] && va[j].first >= vb[i].second + t) {
				done[j] = 1;
				ansa--;			
				break;
			}
		}
		printf("Case #%d: %d %d\n", caseno++, ansa, ansb);	
	}
}
	
	
	
	
	
	
	
	
	
