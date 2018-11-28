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
	int pd,pg,N;
	bool found=false;
	scanf("%d%d%d",&N,&pd,&pg);
	for(int D=1;D<=N;D++){
		if(D*pd%100!=0)continue;
		int wd=D*pd/100, ld=D-wd;
		for(int G=1;G<=10000000;G++){
			if(G*pg%100!=0)continue;
			int wg=G*pg/100, lg=G-wg;
			if(wd<=wg and ld<=lg){
				found=true;
				break;
			}
		}
		if(found)break;
	}
	if(found){
		printf("Possible\n");
	}else{
		printf("Broken\n");
	}
	return;
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

