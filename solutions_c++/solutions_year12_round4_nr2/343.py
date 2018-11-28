// #includes {{{
#include <algorithm>
#include <numeric>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <cmath>
using namespace std;
// }}}
// pre-written code {{{
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define RREP(i,a,b) for(int i=(int)(a);i<(int)(b);++i)
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
//#define IFOR(i,it,c) for(__typeof((c).begin())it=(c).begin();it!=(c).end();++it,++i)
#define ALL(c) (c).begin(), (c).end()
#define MP make_pair
//#define PB push_back
#define TO_STRING(VariableName) # VariableName
//#define DB(c) cout<<TO_STRING(c)<<"="<<(c)<<endl

#define EXIST(e,s) ((s).find(e)!=(s).end())

#define RESET(a) memset((a),0,sizeof(a))
#define SET(a) memset((a),-1,sizeof(a))
#define PB push_back

typedef long long Int;
typedef unsigned long long uInt;
typedef long double rn;

typedef pair<int,int> pii;

#ifdef DEBUG
#include"debug.h"
#include"print.h"
#endif
// }}}

const int M=1010;
int N,W,L;
vector<pii> r;
pii ans[M];

void check(){
	REP(i,N){
		assert(0<=ans[i].first and ans[i].first<=W);
		assert(0<=ans[i].second and ans[i].second<=L);
	}
}

void main2(){
	r.clear();
	cin>>N>>W>>L;
	REP(i,N){
		int r_;
		cin>>r_;
		r.push_back(MP(r_,i));
	}
	sort(ALL(r),greater<pii>());
//	REP(i,N)cerr<<r[i]<<" ";
//	cerr<<endl;
	int x=0,y=0,y2;
	int i=0;
	bool sy=true,sx;
	for(;i<N;){
		sx=true;
		x=0;
		int dy=0;
		for(;i<N;i++){
			int y0;
			if(sy)y0=y;
			else y0=y+r[i].first;
			if(sx){
				ans[r[i].second]=MP(x,y0);
//				ans[i]=MP(x,y0);
			}else if(x+r[i].first<=W){
				ans[r[i].second]=MP(x+r[i].first,y0);
//				ans[i]=MP(x+r[i].first,y0);
				x+=r[i].first*2;
			}else{
				break;
			}
			if(sy)dy=max(dy,r[i].first);
			else dy=max(dy,r[i].first*2);
			if(sx)x+=r[i].first;
			else x+=r[i].first*2;
			sx=false;
		}
		sy=false;
		y+=dy;
//		cerr<<y<<endl;
	}
//	assert(y<=L);
	REP(i,N){
		cout<<ans[i].first<<" "<<ans[i].second;
		if(i<N-1)cout<<" ";
	}
	cout<<endl;
	check();
}

//{{{ main function
int main() {
	int T;scanf("%d", &T);
	REP(ct, T){
		printf("Case #%d: ",ct+1);
		main2();
	}
	return 0;
}
//}}}
