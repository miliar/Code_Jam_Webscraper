#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
using namespace std;  

#define PB push_back  
#define MP make_pair  
#define SZ(v) ((int)(v).size())  
#define FOR(i,a,b) for(int i=(a);i<(b);++i)  
#define REP(i,n) FOR(i,0,n)  
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)  
#define REPE(i,n) FORE(i,0,n)  
#define FORSZ(i,a,v) FOR(i,a,SZ(v))  
#define REPSZ(i,v) REP(i,SZ(v))  
typedef long long ll;  

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<VPII> VVPII;

void run(int casenr) {
	int len,vwalk,vrun,trun,n;
	scanf("%d%d%d%d%d",&len,&vwalk,&vrun,&trun,&n);
	VI s(n),e(n),w(n);
	REP(i,n) scanf("%d%d%d",&s[i],&e[i],&w[i]);

	VPII parts;
	REPE(i,n) {
		parts.PB(MP(0,(i==n?len:s[i])-(i==0?0:e[i-1])));
		if(i<n) parts.PB(MP(w[i],e[i]-s[i]));
	}
	sort(parts.begin(),parts.end());

	double left=trun,ret=0;
	REPSZ(i,parts) {
		double v=parts[i].first,d=parts[i].second;
		double drun=min(d,(v+vrun)*left);
		ret+=drun/(v+vrun)+(d-drun)/(v+vwalk);
		left-=drun/(v+vrun);
	}
	printf("Case #%d: %.9lf\n",casenr,ret);
}

int main() {
	int n; scanf("%d",&n); FORE(i,1,n) run(i);
	return 0;
}

 
