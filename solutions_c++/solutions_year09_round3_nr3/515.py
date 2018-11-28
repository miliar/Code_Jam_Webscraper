#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <algorithm>
#include <iterator>
#include <functional>
#include <utility>
#include <numeric>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cassert>

using namespace std;

#define allof(c) ((c).begin()),((c).end())
#define debug(c) cout<<"> "<<#c<<" = "<<c<<endl;
#define iter(c) __typeof((c).begin())
#define tr(i,c) for(iter(c) i=(c).begin();i!=(c).end();i++)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define repd(i,n) for(int i=(int)(n-1);i>=0;i--)
#define repi(i,a,b) for(int i=(int)(a);i<=(int)(b);i++)
#define mp make_pair
#define fst first
#define snd second
#define pb push_back

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef pair<double,double> pdd;

#define INFTY 1000000000

int c(int pos,vi &p){
	int res=0;
	for(int i=pos+1;i<p.size();i++){
		if(p[i]){
			break;
		}
		res++;
	}
	for(int i=pos-1;i<p.size();i--){
		if(p[i]){
			break;
		}
		res++;
	}
	return res;
}

int main(){
	int T; cin>>T;
	rep(iCase,T){
		int P,Q; cin>>P>>Q;
		vi v(Q);
		rep(i,Q){
			cin>>v[i];
		}
		int ans=INFTY;
		do{
			int tans=0;
			vi p(P,0);
			rep(i,Q){
				p[v[i]-1]=1;
				tans+=c(v[i]-1,p);
			}
			ans=min(ans,tans);
		}while(next_permutation(allof(v)));
		
		printf("Case #%d: %d\n",iCase+1,ans);
	}
	
	return 0;
}
