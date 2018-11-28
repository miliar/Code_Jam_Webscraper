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

typedef vector<int> vi;
typedef long long ll;
typedef vector<ll> vll;

int main(){
	int T; cin>>T;
	for(int iCase=1;iCase<=T;iCase++){
		ll L,t,N,C; cin>>L>>t>>N>>C;
		vll a(C);
		rep(i,C) cin>>a[i];
		vll d(N+1);
		d[0]=0;
		rep(i,N) d[i+1]=a[i%C];
		vll nreacht(N+1);
		nreacht[0]=0;
		REP(i,1,N) nreacht[i]=d[i]*2+nreacht[i-1];
		
//		cout<<"nreacht"<<endl;
//		rep(i,N+1) cout<<nreacht[i]<<' ';
//		cout<<endl;
//		cerr<<"#"<<endl;
		
		vll canuse;
		rep(i,N+1){
			if(nreacht[i]==t){
				REP(j,i+1,N) canuse.pb(d[j]);
				break;
			}
			else if(nreacht[i]>t){
				canuse.pb((nreacht[i]-t)/2);
				REP(j,i+1,N) canuse.pb(d[j]);
				break;
			}
		}
		
		
//		cerr<<"#2"<<endl;
//		debug(canuse.size());
//		cout<<"canuse"<<endl;
//		rep(i,canuse.size()) cout<<canuse[i]<<' ';
//		cout<<endl;
		
		sort(allof(canuse));
		reverse(allof(canuse));
		
		ll ans=t;
		
		if(canuse.size()!=0){
			rep(i,L) ans+=canuse[i];
			REP(i,L,canuse.size()-1) ans+=canuse[i]*2;
		}
		else{
			ans=nreacht.back();
		}
		
//		cerr<<"Case #"<<iCase<<": ";
		cout<<"Case #"<<iCase<<": ";
		cout<<ans<<endl;
	}
	
	return 0;
}
