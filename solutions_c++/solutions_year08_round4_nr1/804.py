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
#define MAX 100010
#define mkp make_pair
typedef long long LL;
typedef double D;
#define sz size()
#define bset(i,j) (((1)<<(j))&(i))
#define AND 1
#define OR 0
int gate[MAX], can[MAX], m, val[MAX];
int go(int node, int v)
{
	if(node > m) return INF;
	if(node >= (m+1)/2) {
		if(val[node] == v) return 0;
		return INF;
	}
	int ans=INF;
	if(v == 1) {
		if(gate[node] == OR) {
			ans <?= go(2*node, 1)<?go(2*node+1, 1);
			if(can[node])
			ans <?= go(2*node,1)+go(2*node+1,1)+1;
		}
		else {
			ans <?= go(2*node,1)+go(2*node+1,1);
			if(can[node])
			ans <?= (go(2*node, 1)<?go(2*node+1, 1)) + 1;
		}
	}
	else {
		if(gate[node] == OR) {
			ans <?= go(2*node, 0)+go(2*node+1, 0);
			if(can[node])
			ans <?= (go(2*node,0)<?go(2*node+1,0))+1;
		}
		else {
			ans <?= go(2*node,0)<?go(2*node+1,0);
			if(can[node])
			ans <?= (go(2*node, 0)+go(2*node+1, 0)) + 1;
		}
	}
//	cout<<ans <<" for "<<node <<" "<<v<<"\n";
	return ans;
}
int main()
{
	int t=GI;
	REP(kase,t) {
		printf("Case #%d: ", kase+1);
		REP(i,MAX) gate[i]=can[i]=0, val[i]=-1;
		m=GI;
		int v=GI;
		REP(i,(m-1)/2) gate[i+1]=GI, can[i+1]=GI;
		REP(i,(m+1)/2) {
			val[(m+1)/2-1+i+1]=GI;

			}
		
		int ans=go(1, v);
		if(ans < INF) 
		printf("%d", ans);
		else
		printf("IMPOSSIBLE");
		printf("\n");
	}		
	
}
	
	
	
	
	
	
	
	
	
