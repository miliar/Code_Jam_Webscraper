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
int b[1000+5],e[1000+5],w[1000+5];
int main(){
	int i,j,k,t,cas = 0;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	while(t--){
		int x,s,r,n;
		double t;
		scanf("%d %d %d %lf %d",&x,&s,&r,&t,&n);
		vector<pair<double,double> >P;
		int sum = 0;
		for(i = 1;i <= n;i++){
			int b,e,w;
			scanf("%d %d %d",&b,&e,&w);
			P.pb(mp((double)(w),double(e - b)));
			sum = sum + e - b;
		}
		P.pb(mp(0,x - sum));
		sort(P.begin(),P.end());
		double ans = 0;
		for(i = 0;i < P.size();i++){
			double cur = P[i].second;
			double t1 = cur / (double)(P[i].first + r);
			if(t1 <= t){
				t = t - t1;
				ans = ans + t1;
			}else{
				ans += t + (cur - (P[i].first + r)*t)/(P[i].first + s);
				t = 0;
			}
		}
		printf("Case #%d: %.6lf\n",++cas,ans);	
	}
	return 0;
}