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
const int maxn=329;
const int oo = 1000*1000*100;
int myabs(int a){
	if(a<0) a=-a;
	return a;
}
int D,I,M,N;
int a[maxn];
int dp[maxn][maxn];

priority_queue< pair< int, pair<int,int> > > pq;
int main(){
	assert(freopen("B.in","rt",stdin)==stdin);
	assert(freopen("B.out","wt",stdout)==stdout);
	int T,Case,i,j;
	scanf("%d",&T);
	for(Case=1;Case<=T;Case++){
		scanf("%d %d %d %d",&D,&I,&M,&N);	
		for(i=1;i<=N;i++) scanf("%d",&a[i]);
		//memset(dp,-1,sizeof dp);
		for(i=0;i<329;i++)
			for(j=0;j<329;j++) dp[i][j]=oo;
		dp[0][300]=0;
		pq.push(mp(0,mp(0,300)));
		int w,c,p;
		pair<int,pair<int,int> > f;
		while(!pq.empty()){
			f=pq.top();
			pq.pop();
			p=f.Y.X;
			w=-f.X;
			c=f.Y.Y;
			//DBG(p);
			//DBG(c);
			//DBG(w);
			if(p>N) continue;
			if(p==N){
				if(dp[p+1][c]>w){
					dp[p+1][c]=w;
					pq.push(mp(-dp[p+1][c],mp(p+1,c)));
				}
			}
			if(c!=300){
				for(i=0;i<256;i++){
					if(myabs(c-i)<=M){
						if(dp[p][i]>w+I){
							dp[p][i]=w+I;
							pq.push(mp(-dp[p][i],mp(p,i)));
						}
					}	
				}
			}
			if(dp[p+1][c]>w+D){
				dp[p+1][c]=w+D;
				pq.push(mp(-dp[p+1][c],mp(p+1,c)));	
			}
			for(i=0;i<256;i++){
				if(p+1<=N&&(myabs(c-i)<=M||c==300)){
					if(dp[p+1][i]>w+myabs(a[p+1]-i)){
						dp[p+1][i]=w+myabs(a[p+1]-i);
						pq.push(mp(-dp[p+1][i],mp(p+1,i)));
					}
				}
			}
		}
		int r=oo;
		for(i=0;i<256;i++){
			r=min(r,dp[N+1][i]);
		}
		r=min(r,dp[N+1][300]);
		printf("Case #%d: %d\n",Case,r);
	}
	
	return 0;
}
