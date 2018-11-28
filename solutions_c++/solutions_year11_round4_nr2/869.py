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
#include <memory.h>

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
typedef pair<int,int> pii;
typedef long long ll;

int main(){
	int T; cin>>T;
	for(int iCase=1;iCase<=T;iCase++){
		int R,C,D; cin>>R>>C>>D;
		int m[20][20];
		rep(i,R) rep(j,C){
			char c; cin>>c;
			m[i][j]=c-'0'+D;
		}
		
		int ans=0;
		rep(a,R) rep(b,C) REP(c,a,R-1) REP(d,b,C-1) if(c-a>=2 && d-b>=2 && (a-c)==(b-d)){
			double cx=b+(c-a)/2.0,cy=a+(c-a)/2.0;
			double vx=0,vy=0;
			REP(y,a,c) REP(x,b,d){
				if(y==a && x==b) continue;
				if(y==c && x==d) continue;
				if(y==a && x==d) continue;
				if(y==c && x==b) continue;
				
				vx+=(x-cx)*m[y][x];
				vy+=(y-cy)*m[y][x];
			}
			if(vx==0 && vy==0) ans=max(ans,c-a+1);
		}
		
		cout<<"Case #"<<iCase<<": ";
		if(ans==0) cout<<"IMPOSSIBLE"<<endl;
		else cout<<ans<<endl;
	}
	return 0;
}
