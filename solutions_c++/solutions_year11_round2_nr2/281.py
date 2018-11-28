// #includes {{{
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>
#include <cstring>

#include <cmath>
#include <complex>
using namespace std;
// }}}
// pre-written code {{{
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define RREP(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()

typedef long long Int;
typedef long long ll;
typedef long double ld;
// }}}

int c, d;
ld p[210];
int v[210];

bool feasible(ld t){
	ld pos=p[0]-t;
	REP(i,c){
		if(pos>p[i]+t)return false;
		if(pos<p[i]-t){
			pos=p[i]-t;
		}
		pos+=(ld)d*(v[i]-1);
		if(pos>p[i]+t)return false;
		pos+=d;
	}
	return true;
}

ld bsearch(){
	ld l=0, r=1e+15;
	while(r-l>1e-7){
//		cout<<l<<" "<<r<<endl;
		ld mid=(l+r)/2;
		if(feasible(mid)){
			r=mid;
		}else{
			l=mid;
		}
	}
	return (l+r)/2;
}

void main2(){
	cin>>c>>d;
	REP(i,c){
		cin>>p[i]>>v[i];
	}
	printf("%.10Lf\n",bsearch());
}

int main() {
	int T;scanf("%d", &T);
	REP(ct, T){
		printf("Case #%d: ",ct+1);
		main2();
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread

