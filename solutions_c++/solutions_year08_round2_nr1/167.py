#include <vector>
#include <iostream>
#include <string>
#include <cstdio>
#include <set>
#include <map>
#include <queue>
#include <cassert>
#include <cstdlib>
#include <cmath>
#include <sstream>
#include <algorithm>
#include <stack>
using namespace std;

#define LET(x,a) typeof(a) x(a)
#define FOR(i,a,b) for(LET(i,a); i!=b; i++)
#define EACH(i,v) for(LET(i,v.begin()); i!=v.end(); i++)
#define REP(i,n) FOR(i,0,n)
#define DBG(x) cout<<#x<<" --> "<<x<<"\t"
#define DBE(x) cout<<#x<<" --> "<<x<<"\n"
#define sz size()
#define ins insert
#define pb push_back
#define INF (int)1e8
#define COUNT(f,x) ({int _=0; f if(x) _++; _;})
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef vector<VS> VVS;
typedef pair<long long,long long> PII;
typedef long long LL;
typedef long double LD;
#define GI ({int t;scanf("%d",&t);t;})
#define INF (int)1e8

vector<PII> V;

int main() {
	int T = GI;
	REP(kase, T) {
		V.clear();
		int n=GI,A=GI,B=GI,C=GI,D=GI,x0=GI,y0=GI,M=GI;
		long long X = x0, Y = y0;
		V.pb(PII(X,Y));
		REP(i,n-1) {
			X = (A * X + B) % M;
		  Y = (C * Y + D) % M;
  		V.pb(PII(X,Y));
		}
		int count = 0;
		REP(i,V.sz) FOR(j,i+1,V.sz) FOR(k,j+1,V.sz) {
			X = V[i].first+V[j].first+V[k].first;
			Y = V[i].second+V[j].second+V[k].second;
			if((X%3 == 0) and (Y%3 == 0)) count ++;
		}
		printf("Case #%d: %d\n", kase+1, count);
	}
	return 0;
}

