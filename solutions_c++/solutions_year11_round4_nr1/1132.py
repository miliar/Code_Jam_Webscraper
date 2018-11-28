#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <cstring>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional> 
#include <numeric>
using namespace std;
#define foreach(i,v) for(__typeof((v).end()) i=(v).begin();i!=(v).end();++i)
#define rforeach(i,v) for(__typeof((v).rend()) i=(v).rbegin();i!=(v).rend();++i)
#define FOR(i,b,e) for(int i=(b);i<(e);++i)
#define FORE(i,b,e) for(int i=(b);i<=(e);++i)
#define debug(x) cerr << #x << " = " << (x) << "\n"
typedef long long LL;
typedef pair<double,double> P;
#define v first
#define len second
#define eps (1e-9)

int main(){
	int t;
	cin >> t;
	FORE(z,1,t){
		int x, s, r, n;
		double t;
		cin >> x >> s >> r >> t >> n;
		P p[n+1];
		FOR(i,0,n){
			int b, e, w;
			cin >> b >> e >> w;
			p[i] = P(w,e-b);
		}
		double len = x;
		FOR(i,0,n)
			len -= p[i].len;
		p[n] = P(0,len);
		sort(p,p+n+1);
		double ans = 0;
		FOR(i,0,n+1){
			double run = p[i].len/(p[i].v+r);
			run = min(run,t);
			t -= run;
			ans += run;
			double rlen = run*(p[i].v+r);
			ans += (p[i].len-rlen)/(p[i].v+s);
		}
		printf("Case #%d: %.12f\n",z,ans);
	}
	return 0;
}
