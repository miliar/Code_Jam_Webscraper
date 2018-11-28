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
	rep(iCase,T){
		int N; cin>>N;
		int mi=10000000;
		int xsum=0;
		int sum=0;
		rep(i,N){
			int c; cin>>c;
			xsum^=c;
			sum+=c;
			mi=min(mi,c);
		}
		cout<<"Case #"<<iCase+1<<": ";
		if(xsum!=0) cout<<"NO"<<endl;
		else cout<<sum-mi<<endl;
	}
	
	
	return 0;
}
