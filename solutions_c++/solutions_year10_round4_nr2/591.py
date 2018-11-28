#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cassert>

using namespace std;

#define allof(c) ((c).begin()),((c).end())
#define debug(c) cerr<<"> "<<#c<<" = "<<(c)<<endl;
#define iter(c) __typeof((c).begin())
#define tr(i,c) for(iter(c) i=(c).begin();i!=(c).end();i++)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define REP(i,a,b) for(int i=(int)(a);i<=(int)(b);i++)
#define mp make_pair
#define fst first
#define snd second
#define pb push_back

#define INFTY 100000000000LL

typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long ll;

int re[1<<11];
int m[1<<11];
int cost[11][1<<11];
int p;

map<pair<pii,int>,ll> dp;	//l,r,v
map<pair<pii,int>,ll> visited;	//l,r,v

ll go(int l,int r,int v,int d,int id){
	if(d==0){
//		debug(l)debug(r)debug(re[l])
		if(re[l]<=0) return 0;
		return INFTY;
	}
	if(visited[mp(mp(l,r),v)]){
		return dp[mp(mp(l,r),v)];
	}
	//tsukau
	REP(i,l,r-1) re[i]--;
	ll a=go(l,(l+r)/2,(v<<1)|1,d-1,2*id)+go((l+r)/2,r,(v<<1)|1,d-1,2*id+1)+cost[d-1][id];
//	debug(d-1)debug(id)debug(cost[d-1][id])
	//tsukawanai
	REP(i,l,r-1) re[i]++;
	ll b=go(l,(l+r)/2,(v<<1),d-1,2*id)+go((l+r)/2,r,(v<<1),d-1,2*id+1);
	
	visited[mp(mp(l,r),v)]=true;
	dp[mp(mp(l,r),v)]=min(a,b);
	
	return min(a,b);
}

int main(){
	int nCases; cin>>nCases;
	for(int iCase=1;iCase<=nCases;iCase++){
		cin>>p;
		rep(i,1<<p) cin>>m[i];
		rep(i,p) rep(j,1<<(p-i-1)) cin>>cost[i][j];
		
		rep(i,1<<p) re[i]=p-m[i];
		dp.clear();
		visited.clear();
		ll res=go(0,1<<p,0,p,0);
		cerr<<"Case #"<<iCase<<": ";
		cout<<"Case #"<<iCase<<": ";
		cout<<res<<endl;
	}
	
	
	
	return 0;
}
