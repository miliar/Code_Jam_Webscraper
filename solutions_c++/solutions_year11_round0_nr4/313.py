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
VI P;
int main(){
	int i,j,t,cas = 0;
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	scanf("%d",&t);
	while(t--){
		P.clear();
		int n;
		scanf("%d",&n);
		for(i = 1;i <= n;i++){
			int x;
			scanf("%d",&x);
			P.pb(x);
		}
		VI temp = P;
		sort(temp.begin(),temp.end());
		int ans = 0;
		for(i = 0;i < SZ(P);i++){
			if(temp[i] != P[i])ans++;
		}	
		printf("Case #%d: %d.000000\n",++cas,ans);
	}
	return 0;
}
