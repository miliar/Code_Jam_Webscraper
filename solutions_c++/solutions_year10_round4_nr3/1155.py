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

const int N=110;
int a[N][N];

void apply(){
	int a2[N][N];
	REP(x, N){
		REP(y, N){
			a2[x][y]=a[x][y];
			if(a[x][y]==1){
				if(x-1>=0 and a[x-1][y]==1){
					continue;
				}
				if(y-1>=0 and a[x][y-1]==1){
					continue;
				}
				a2[x][y]=0;
			}
			else{
				if(x-1<0 or a[x-1][y]==0){
					continue;
				}
				if(y-1<0 or a[x][y-1]==0){
					continue;
				}
				a2[x][y]=1;
			}
		}
	}
	REP(x, N)REP(y, N)a[x][y]=a2[x][y];
}

void print(){
	REP(i, 10){
		REP(j, 10){
			cout<<a[i][j]<<" ";
		}
		cout<<endl;
	}
	cout<<endl;
}

void main2(){
	int R;
	cin>>R;
	memset(a, 0, sizeof(a));
	REP(x, N){
		REP(y, N){
			a[x][y]=0;
		}
	}
	REP(i, R){
		int x1, y1, x2, y2;
		cin>>x1>>y1>>x2>>y2;
		for(int x=x1;x<=x2;x++){
			for(int y=y1;y<=y2;y++){
				a[x][y]=1;
			}
		}
	}
	int t=0;
//	print();
	while(true){
		t++;
		apply();
		bool died=true;
		REP(i, N){
			REP(j, N){
				if(a[i][j]){
					died=false;
					break;
				}
			}
			if(not died)break;
		}
		if(died){
			cout<<t<<endl;
			return;
		}
	}
}

int main() {
	int T;
	cin>>T;
	REP(ct, T){
		printf("Case #%d: ", ct+1);
		main2();
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread

