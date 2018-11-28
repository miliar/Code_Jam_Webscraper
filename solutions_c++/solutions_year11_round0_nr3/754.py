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
#define present(c,x) ((c).find(x) != string::npos)
typedef long long ll;
template<class T>inline int sz(T& x){return (int)x.size();}
int stoi(string a){int len=sz(a);if(len==1)return a[0]-'0';return a[len-1]-'0'+10*stoi(a.substr(0,len-1));}
template<class T>inline string tostring(T& i){ostringstream oss; oss << i; return oss.str();}
template <class T> void make_unique(T& v){sort(ALL(v)); v.resize(unique(ALL(v)) - v.begin());}
inline void eraseV(vector<int>& vec,int val) {vector<int>::iterator it = find(ALL(vec),val);if(it!=vec.end()) vec.erase(it,it+1);}

int data[1000001];
int dp[2097153];
int dpPrev[2097153];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tests; cin>>tests;
	for(int test=1;test<=tests;++test){
		int n; cin>>n;
		int xorsum = 0;
		int ans = -1;
		memset(dp,0xff,sizeof(dp));
		memset(dpPrev,0xff,sizeof(dpPrev));
		for(int i=0;i<n;++i){
			scanf("%d",&data[i]);
			xorsum ^= data[i];
		}
		dpPrev[0] = 0;
		for(int i=0;i<n;++i){
			for(int j=0;j<2097153;++j){
				if(dpPrev[j] != -1) dp[j^data[i]] = dpPrev[j] + data[i];
			}
			for(int j=0;j<2097153;++j){
				if(dpPrev[j] != -1){
					if(dp[j] != -1){
						dp[j] = max(dp[j],dpPrev[j]);
					}else{
						dp[j] = dpPrev[j];
					}
				}
				if(j!=0 && dp[j] != -1){
					if(j == (j^xorsum)){
						ans = max(ans,dp[j]);
					}
				}
			}

			memcpy(dpPrev,dp,sizeof(dp));
			memset(dp,0xff,sizeof(dp));
		}
		if(ans == -1){
			printf("Case #%d: NO\n",test);
		}else{
			printf("Case #%d: %d\n",test,ans);
		}
	}
	return 0;
} 
