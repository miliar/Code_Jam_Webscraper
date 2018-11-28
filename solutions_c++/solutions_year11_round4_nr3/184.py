#include <map>        
#include <set>        
#include <queue> 
#include <cmath>       
#include <cstdio>      
#include <vector>        
#include <string>        
#include <sstream>       
#include <iostream>       
#include <algorithm>        
using namespace std;        
#define FOR(i,a,b) for(int i=(a); i<(b); ++i)        
#define FORE(it,x) for(typeof(x.begin()) it=x.begin(); it!=x.end(); ++it)        
#define SET(x, v) memset(x, v, sizeof (x))        
#define sz size()        
#define cs c_str()        
#define pb push_back        
#define mp make_pair       
    
typedef long long ll;        
int np;
ll prime[1048576];
void init() {
	np= 0;
	prime[np++] = 2;
	FOR(i,3,1048576) {
		FOR(j,0,np) {
			if(prime[j]*prime[j] > i) {
				prime[np++] = i;
				break;
			}
			else if(i%prime[j]==0) break;
		}
		i++;
	}
}
int main() {
	int e= 0, T;
	scanf("%d",&T);
	int ans = 0;
	init();
	while(T--) {
		ll n;
		scanf("%I64d",&n);
		int maxi = 0 , mini = 1;
		FOR(i,0,np) {
			if(prime[i] > n) break;
			ll x = 1;
			int cnt = 0;
			while(x <= n) {
				x*= prime[i];
				cnt++;
			}
			cnt--;
			if(cnt != 0) {
				mini += cnt;
				maxi++;
				//printf("\t %I64d with %d\n", prime[i], cnt);
			}
		}
		//printf("[%d vs %d]\n", maxi, mini);
		ans = mini - maxi;
		if(n == 1) ans = 0;
		printf("Case #%d: %d\n", ++e, ans);
	}
	return 0;
}