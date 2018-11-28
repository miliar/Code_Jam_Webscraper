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


ll mypow(int a,int b){
	ll res=1;
	rep(i,b){
		res*=(ll)a;
	}
	return res;
}

int main(){
	int T; cin>>T;
	for(int iCase=0;iCase<T;iCase++){
		string s; cin>>s;
		int sp[256];
		memset(sp,-1,sizeof(sp));
		vector<int> ss(s.size());
		int c_p=0;
		rep(i,s.size()){
			if(sp[s[i]]==-1){
				sp[s[i]]=(c_p==0?1:(c_p==1?0:c_p));
				c_p++;
			}
			ss[i]=sp[s[i]];
		}
		ll ans=0;
		reverse(allof(ss));
		if(c_p==1){
			c_p++;
		}
		rep(i,ss.size()){
			ans+=ss[i]*mypow(c_p,i);
		}
		printf("Case #%d: ",iCase+1);
		cout<<ans<<endl;
	}
	
	return 0;
}
