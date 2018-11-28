#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <string.h>
#include <bitset>
#include <math.h>
#include <time.h>
#include <list>
#include <stack>

using namespace std;

//typedef long long LL;
typedef __int64 LL;
#define move(i) (1<<i)
#define take(a,b) (((a)>>(b))&1)
#define mp make_pair
#define pb push_back
#define VI vector<int>
#define MX vector<vector<int> >
#define PII pair<int,int>
#define SZ(X) ((int)(X.size()))
#define LEN(X) ((int)(X.length()))
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
//template<class T> inline T max(T a,T b){return a > b ? a : b;}
//template<class T> inline T min(T a,T b){return a < b ? a : b;}

// template by tracyzhu
VI p;
int n;
int main(){
	int i,j;
	int t,cas = 0;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&t);
	while(t--){
		p.clear();
		scanf("%d",&n);
		int pre = 0;
		for(i = 1;i <= n;i++){
			int x;scanf("%d",&x);
			p.pb(x);
			pre = pre ^ x;
		}
		if(pre != 0){
			printf("Case #%d: NO\n",++cas);
			continue;
		}
		sort(p.begin(),p.end());
		int ans = 0;
		for(i = 1;i < SZ(p);i++){
			ans += p[i];
		}
		printf("Case #%d: %d\n",++cas,ans);
	}
	return 0;
}
