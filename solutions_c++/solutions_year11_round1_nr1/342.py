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
#include <functional>
using namespace std;

typedef long long LL;
//typedef __int64 LL;
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
int gcd(int a,int b){
	if(b == 0) return a;
	else return gcd(b,a%b);
}
int main(){
	int i,j,k,t,cas = 0;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	while(t--){
		int pd,pg;
		LL n;
		scanf("%I64d %d %d",&n,&pd,&pg);
		if(pg == 100 && pd < 100){
			printf("Case #%d: Broken\n",++cas);
			continue;
		}
		if(pg == 0 && pd > 0){
			printf("Case #%d: Broken\n",++cas);
			continue;
		}
		int k = gcd(pd,100);
		int a1,b1;
		a1 = pd/k;b1 = 100/k;
		int f = 0;
		if(n >= b1){f = 1;}
		if(f == 1){
			printf("Case #%d: Possible\n",++cas);
		}else{
			printf("Case #%d: Broken\n",++cas);
		}
	}
	return 0;
}