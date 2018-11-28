#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <limits>
#include <map>
#include <cmath>
#include <numeric>
#include <memory.h>
#include <stdio.h>
using namespace std;
 
#define pb push_back
#define REP(i,n) for(int i=0; i<(n); ++i)   
#define ALL(X) (X).begin(),(X).end()
#define present(c,x) ((c).find(x) != (c).end())
typedef long long ll;
template<class T>inline int sz(T& x){return (int)x.size();}
int stoi(string a){int len=sz(a);if(len==1)return a[0]-'0';return a[len-1]-'0'+10*stoi(a.substr(0,len-1));}
template<class T>inline string tostring(T& i){ostringstream oss; oss << i; return oss.str();}
template <class T> void make_unique(T& v){sort(ALL(v)); v.resize(unique(ALL(v)) - v.begin());}
inline void eraseV(vector<int>& vec,int val) {vector<int>::iterator it = find(ALL(vec),val);if(it!=vec.end()) vec.erase(it,it+1);}


int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tests; cin>>tests;
	for(int test=1;test<=tests;++test){
		ll dis[10001];
		ll val[10001]; memset(val,0,sizeof(val));
		ll l,t,n,c; cin>>l>>t>>n>>c;
		for(int i=0;i<c;++i) cin>>dis[i];

		val[0] = 0;
		for(int i=0;i<n;++i){
			val[i+1] = val[i] + dis[i%c] * 2;
		}

		ll ans = 0;

		if(l >= 0){
			ans = val[n];
		}

		if(l >= 1){
			for(int i=0;i<n;++i){
				if(val[i+1] >= t){
					ll minus = max(t - val[i], ll(0));
					ans = min(ans, val[n] - (val[i+1] - val[i]) + (minus+(dis[i%c] - minus/2)));
				}
			}
		}

		if(l >= 2){
			for(int i=0;i<n;++i){
				if(val[i+1] >= t){
					ll minus1 = max(t - val[i], ll(0));
					ll elaps = (val[i+1] - val[i]) - (minus1+(dis[i%c] - minus1/2));
					ll sub = val[n] - (val[i+1] - val[i]) + (minus1+(dis[i%c] - minus1/2));

					for(int j=i+1;j<n;++j){
						ll left = val[j] - elaps;
						ll right = val[j+1] - elaps;
						ll minus2 = max(t - left,ll(0));

						if(right >= t){
							ans = min(ans, sub - (right - left) + minus2+(dis[j%c] - minus2/2));
						}
					}
				}
			}
		}
		printf("Case #%d: %lld\n",test,ans);
	}
	return 0;
} 
