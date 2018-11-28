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
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()

typedef long long Int;
typedef long long ll;
typedef long double ld;
// }}}

#define RREP(i,a,b) for(int i=a;i<=b;i++)

const int M=510;
const ld EPS=1e-3;

void main2(){
	char w[M][M];
	int R,C,D;
	cin>>R>>C>>D;
	REP(i,R){
		cin>>w[i];
		REP(j,C){
			w[i][j]-='0';
		}
	}
	bool opt=false;
	int maxi=-1;
	REP(i,R)REP(j,C){
		for(int k=3;;k++){
			if(i==0 and j==2 and k==3)opt=true;
			else opt=false;
			if(i+k>R or j+k>C)break;
			ld x=(ld)i+(ld)(k-1)/2,y=(ld)j+(ld)(k-1)/2;
			ld sx=0,sy=0;
			REP(i2,k)REP(j2,k){
//				if(opt)cout<<i2<<" "<<j2<<endl;
				if(i2==0){
					if(j2==0 or j2==k-1)continue;
				}else if(i2==k-1){
					if(j2==0 or j2==k-1)continue;
				}
				int m=w[i+i2][j+j2];
				ld x1=(ld)i+i2,y1=(ld)j+j2;
//				if(opt)cout<<i2<<" "<<j2<<endl;
//				cout<<x1<<" "<<y1<<endl;
				sx+=(x1-x)*m;sy+=(y1-y)*m;
			}
			if(abs(sx)<EPS and abs(sy)<EPS){
				maxi=max(k,maxi);
			}
//			if(opt)cout<<abs(sx)<<" "<<abs(sy)<<endl;
		}
	}
	if(maxi>=0){
		cout<<maxi;
	}else{
		cout<<"IMPOSSIBLE";
	}
	cout<<endl;
}

int main() {
	int T;scanf("%d", &T);
	REP(ct, T){
		printf("Case #%d: ",ct+1); main2();
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread

