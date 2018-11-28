#include <vector>
#include <cstdio>
#include <set>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <sstream>
#include <numeric>
#include <queue>
#include <iostream>
#include <string>
#include <cstring>
#include <utility>
#define sz(a) int((a).size())
#define pb push_back
#define mk make_pair
#define fi first
#define se second
#define Rep(i,j,k) for (int i=(j); i<=(k); i++)
#define Repd(i,j,k) for (int i=(j); i>=(k); i--)
#define ALL(c) (c).begin(),(c).end()
#define TR(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define SUM(a) accumulate(all(a),string())
#define online1
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> II;
typedef long long LL;

int n,w,h;
II r[10000];
II c[10000];
II ans[10000];

LL calc(II cc, int r){
	LL cx=cc.fi, cy=cc.se;
	return (LL)r*r*4-(min(cx+r,(LL)w)-max(cx-r,0LL))*(min(cy+r,(LL)h)-max(cy-r,0LL));
}

LL dis(II a, II b){
	return ((LL)a.fi-b.fi)*(a.fi-b.fi)+((LL)a.se-b.se)*(a.se-b.se);
}

pair<II,LL> find(int j, int i, int t){
	II cc;
	if (t==-1)
		cc=mk(rand()%(w+1),rand()%(h+1));
	if (j==0){
		if (t==0)
			cc=mk(0,0);
		if (t==1)
			cc=mk(w,0);
		if (t==2)
			cc=mk(0,h);
		if (t==3)
			cc=mk(w,h);
	}else{
		if (t==0)
			cc=mk(max(c[j].fi-r[j].fi,-r[i].fi) + r[i].fi, max(c[j].se-r[j].fi,r[i].fi) - r[i].fi);
		if (t==1)
			cc=mk(min(c[j].fi+r[j].fi,w-r[i].fi) + r[i].fi, max(c[j].se-r[j].fi,-r[i].fi) + r[i].fi);
		if (t==2)
			cc=mk(max(c[j].fi-r[j].fi,r[i].fi) - r[i].fi, min(c[j].se+r[j].fi,h-r[i].fi) + r[i].fi);
		if (t==3)
			cc=mk(min(c[j].fi+r[j].fi,w+r[i].fi) - r[i].fi, min(c[j].se+r[j].fi,h+r[i].fi) - r[i].fi);
	}
	if (cc.fi<0 || cc.se<0 ||
		cc.fi>w || cc.se>h)
		return mk(mk(-1,-1),-1);
	Rep(k,1,i-1)
		if (dis(c[k],cc)<((LL)r[k].fi+r[i].fi)*(r[k].fi+r[i].fi))
			return mk(mk(-1,-1),-1);
	return mk(cc,calc(cc,r[i].fi));	
}

int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	srand(time(0));
	
	int TT; cin>>TT;
	
	Rep(tt,1,TT){
		cin>>n>>w>>h;
		Rep(i,1,n) cin>>r[i].fi, r[i].se=i;
		sort(r+1,r+n+1,greater<II>());
		
		Rep(i,1,n){
			II cho=mk(-1,-1); LL now=-1;
			
			Rep(j,0,i-1)Rep(t,0,3){
				pair<II,LL> cur=find(j,i,t);
				if (cur.se>now){
					now=cur.se;
					cho=cur.fi;
				}
			}
			
			if (cho.fi==-1){		
				printf("can't find pos for %d\n",r[i].se);		
				
			}
			ans[r[i].se]=cho;
			c[i]=cho;
		}
	
		printf("Case #%d: ",tt);
		Rep(i,1,n)
			printf("%d %d ",ans[i].fi,ans[i].se);
		cout<<endl;
	}

    return 0;
}
