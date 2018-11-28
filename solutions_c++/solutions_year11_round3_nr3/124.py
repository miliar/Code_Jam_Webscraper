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


int main(){
	int T; cin>>T;
	for(int iCase=1;iCase<=T;iCase++){
		int N,L,H; cin>>N>>L>>H;
		vi a(N);
		rep(i,N) cin>>a[i];
		int ans=0;
		REP(i,L,H){
			int cnt=0;
			rep(j,N){
				if(i%a[j]==0 || a[j]%i==0) cnt++;
			}
			if(cnt==N){
				ans=i;
				break;
			}
		}
		
		cout<<"Case #"<<iCase<<": ";
		if(ans==0) cout<<"NO"<<endl;
		else cout<<ans<<endl;
	}
	
	return 0;
}
