#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstdio>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <deque>
#include <cmath>
#include <utility>

using namespace std;


typedef long long ll;

#define all(c) (c).begin(),(c).end()
#define sz(c) (int)(c).size()
#define mp make_pair
#define X first
#define Y second
#define pb push_back
#define DBG(x) cerr<<#x<<" = "<<x<<endl
#define DBGV(x) {cerr<<#x<<": "; for(int i=0;i<sz(c);i++) cerr<<x[i]<<" "; cerr<<endl;}
#define DBGA(x) {cerr<<#x<<": "; for(int i=0;i<int(sizeof(x)/sizeof(x[0]));i++) cerr<<x[i]<<" "; cerr<<endl;}

set< pair<int,int> > a,b;
int main(){
	assert(freopen("C.in","rt",stdin)==stdin);
	assert(freopen("C.out","wt",stdout)==stdout);
	int T,C,n,i,x,y;
	int r1,r2,c1,c2;
	set< pair<int,int> >::iterator it;
	scanf("%d",&T);
	for(C=1;C<=T;C++){
		a.clear();
		b.clear();
		int res=0;
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%d%d%d%d",&c1,&r1,&c2,&r2);
			for(x=c1;x<=c2;x++) for(y=r1;y<=r2;y++) a.insert(mp(x,y));
		}
		while(!a.empty()){
			b.clear();
			for(it=a.begin();it!=a.end();it++){
				x=it->first;
				y=it->second;
				if(a.find(mp(x-1,y))!=a.end()||a.find(mp(x,y-1))!=a.end()) b.insert(*it);
				if(a.find(mp(x+1,y-1))!=a.end()) b.insert(mp(x+1,y));
			}
			a=b;
			res++;
		//	DBG(sz(a));
		}
		printf("Case #%d: %d\n",C,res);
		DBG(C);
	}
	return 0;
}
