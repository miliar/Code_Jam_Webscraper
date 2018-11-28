#include <vector>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <list>
#include <ctime>
#include <string>
#include <cassert>

using namespace std;

//----------------------zjut_DD for Topcoder-------------------------------
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
#define PB push_back
#define MP make_pair
#define ff first
#define ss second
#define two(w) (1<<(w))
#define test(x,w) (x&two(w))
#define sz(v) (int)v.size()
#define all(c) c.begin(),c.end() 
#define clr(buf,val) memset(buf,val,sizeof(buf))
#define rep(i,l,r) for(int i=(l);i<(r);i++)
#define repv(i,v)  for(int i=0;i<(int)v.size();i++)
#define repi(it,c) for(typeof(c.begin()) it=c.begin();it!=c.end();++it)
//------------------------------------------------------------------------

#define maxn 11000


int toInt(string s){
	int ret=0;
	repv(i, s) ret=ret*10+s[i]-'0';
	return ret;
}

int main(){
	freopen("D:\\Ñ¸À×ÏÂÔØ\\B-small-attempt0.in", "r", stdin);
	freopen("D:\\Ñ¸À×ÏÂÔØ\\B-small-attempt0.out", "w", stdout);
	
	int surpMax[33];
	int normMax[33];
	clr(surpMax, -1);
	clr(normMax, -1);
	rep(p, 0, 31){
		rep(i, 0, 11) rep(j, i, i+3) rep(k, i, i+3){
			if( i>10 || j>10 || k>10 || (i+j+k != p) ) 
				continue;
			if( j==i+2 || k==i+2 ){
				surpMax[p]=max(surpMax[p], max(j, k) );
			}else {
				normMax[p]=max(normMax[p], max(j, k) );
			}
		}
		//printf("norm[%d]=%d\n", p, normMax[p]);
	}
	
	int cas, Te=1; cin>>cas;
	while( cas-- ){
		int N, S, P;
		VI t; 
		cin>>N>>S>>P;
		rep(i, 0, N) {
			int val; cin>>val;
			t.PB(val);
		}
		int dp[110][110]={0};
		rep(i, 0, N){
			rep(s, 0, N){
				//if( normMax[ t[i] ]>=P ){
					dp[i+1][s]=max(dp[i+1][s], dp[i][s]+ (normMax[ t[i] ]>=P) );
				//}
				if( surpMax[ t[i] ]>=P ){
					dp[i+1][s+1]=max(dp[i+1][s+1], dp[i][s]+1);
				}
			}
		}
		printf("Case #%d: %d\n", Te++, dp[N][S]);
	}
}


























