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
	int nCases; cin>>nCases;
	for(int iCase=1;iCase<=nCases;iCase++){
		int R,k,N; cin>>R>>k>>N;
		vi g(N);
		rep(i,N) cin>>g[i];
		vi nsum(N,0),next(N);
		rep(i,N){
			rep(j,N) if(nsum[i]+g[(i+j)%N]<=k){
				nsum[i]+=g[(i+j)%N];
				next[i]=(i+j)%N;
			}
			else break;
			next[i]=(next[i]+1)%N;
		}
		long long res=0;
		int p=0;
		rep(i,R){
			res+=nsum[p];
			p=next[p];
		}
		cout<<"Case #"<<iCase<<": ";
		cout<<res<<endl;
	}
	
	return 0;
}
