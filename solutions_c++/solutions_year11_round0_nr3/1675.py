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

void main2(){
	int n;
	scanf("%d",&n);
	vector<int> v;
	int s=0,ns=0;
	REP(i,n){
		int c;
		scanf("%d",&c);
		s+=c;
		v.push_back(c);
		ns=(ns^c);
	}
	if(ns!=0)printf("NO\n");
	else{
		sort(v.begin(),v.end());
		s-=v[0];
		printf("%d\n",s);
	}
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

