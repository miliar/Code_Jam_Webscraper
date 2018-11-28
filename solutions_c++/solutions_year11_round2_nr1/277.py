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

int n;
char c[110][110];

void main2(){
	cin>>n;
	cout<<endl;
	REP(i,n){
		cin>>c[i];
	}
	vector<ld> wp,owp,oowp;
	vector<int> win,num;
	REP(i,n){
		ld v=0;
		int w=0,ct=0;
		REP(j,n){
			if(c[i][j]=='1'){
				v+=1;w++;
			}
			if(c[i][j]!='.'){
				ct++;
			}
		}
		win.push_back(w);
		num.push_back(ct);
		wp.push_back(v/ct);
	}
	REP(i,n){
		ld v=0;
		int ct=0;
		REP(j,n){
			if(c[i][j]!='.'){
				ct++;
				if(c[i][j]=='1'){
					v+=(ld)(win[j])/(num[j]-1);
				}else{
					v+=(ld)(win[j]-1)/(num[j]-1);
				}
			}
		}
		owp.push_back(v/ct);
	}
	REP(i,n){
		ld v=0;
		int ct=0;
		REP(j,n){
			if(c[i][j]!='.'){
				ct++;v+=owp[j];
			}
		}
		oowp.push_back(v/ct);
	}
	/*
	REP(i,n)cout<<wp[i]<<" ";cout<<endl;
	REP(i,n)cout<<owp[i]<<" ";cout<<endl;
	REP(i,n)cout<<oowp[i]<<" ";cout<<endl;
	*/
	REP(i,n){
		ld ans=wp[i]*0.25+owp[i]*0.5+oowp[i]*0.25;
//		cout<<ans<<endl;
		printf("%.10Lf\n",ans);
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

