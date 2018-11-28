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

typedef pair<int,int> pii;

struct P{
	int f,p;//f=vel:start, f=0:end
	P(int f,int p):f(f),p(p){}
};

bool operator<(const P &l,const P &r){
	if(l.p!=r.p)return l.p<r.p;
	else return l.f<r.f;
}

void main2(){
	set<P> st;
	int X,S,R,t,N;
	cin>>X>>S>>R>>t>>N;
	st.insert(P(0,0));
	st.insert(P(0,X));
	REP(i,N){
		int b,e,w;
		cin>>b>>e>>w;
		st.insert(P(w,b));
		st.insert(P(0,e));
	}
	bool start=true;
	set<P>::iterator prev;
	int v=0;
	multiset<pii> st2;
	FOR(it,st){
	//	cout<<it->p<<endl;
		if(start){
			start=false;
		}else{
			int diff=it->p-prev->p;
		//	cout<<diff<<" "<<v<<endl;
			st2.insert(pii(v,diff));
			v=it->f;
		}
		prev=it;
	}
	ld rest=(ld)t,tm=0;
//	cout<<endl;
	FOR(it,st2){
		int diff=it->second,w=it->first;
//		cout<<w<<" "<<diff<<endl;
		ld t3=(ld)diff/(w+R), t1=(ld)diff/(w+S);
		if(rest>0){
			if(t3<rest){
				rest-=t3;
				tm+=t3;
			}else{
				ld dis=rest*(w+R);
				ld t2=((ld)diff-dis)/(w+S);
				tm+=rest+t2;
				rest=0;
			}
		}else{
			tm+=t1;
		}
	}
	printf("%.10Lf\n",tm);
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

