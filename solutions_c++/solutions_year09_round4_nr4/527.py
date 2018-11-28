#include <iostream>
#include <vector>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <cstdio>

using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define GI ({int t;scanf(" %d",&t);t;})
#define GC(x) scanf(" %c",&x)
#define sz size()
#define rz resize
#define inf (int)1e9
#define pb push_back
#define bs binary_search
#define lb lower_bound
#define ub upper_bound

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef double DD;
typedef long long LL;

struct data {
	int x,y,r;
};

int N;
data test[42];

DD rec(int a, int b) {
	int c=3-a-b;
//	cout<<a<<" "<<b<<" "<<sqrt( (DD) ( (DD)((test[a].x-test[b].x)*(test[a].x-test[b].x)) + (DD)((test[a].y-test[b].y)*(test[a].y-test[b].y)) ) )<<endl;
	return max((DD)test[c].r, ( sqrt( (DD) ( (DD)((test[a].x-test[b].x)*(test[a].x-test[b].x)) + (DD)((test[a].y-test[b].y)*(test[a].y-test[b].y)) ) ) +
	 (DD)test[a].r + (DD)test[b].r )/2.0 );
}

int main() {
	DD ans;
	int yo=0;
	for(int _=GI;_--;) {
		N=GI;
		REP (i,N) {
			test[i].x=GI;
			test[i].y=GI;
			test[i].r=GI;
		}
		if(N==1) ans=test[0].r;
		else if(N==2) ans=max(test[0].r,test[1].r);
		else {
			ans=min(rec(0,1),min(rec(0,2),rec(1,2)));
		}
		printf("Case #%d: %0.6lf\n",++yo,ans);
	}
	return 0;
}

