//Google Code Jam - Problem C
//Author: Sushant Bhatia
#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<cmath>
#include<cstring>
#define FOR(i,j,k) for(i = j;i < k;i++)
#define RFOR(i,j,k) for(i = k-1;i >= j;i--)
#define LL long long
#define GET(x) scanf("%d",&x)
#define OUT(x) printf("%d\n",x)
#define SET(x) memset(x,0,sizeof(x))
#define S(x) x.size()
bool comp(int i,int j){ return i > j; }
using namespace std;
int main(){
	int t;
	int n,nm,xr,mn;
	GET(t);
	int cs,i,tot;
	FOR(cs,1,t+1){
		GET(n);
		xr = tot = 0;
		mn = 100000000;
		FOR(i,0,n){
			GET(nm);
			tot += nm;
			xr ^= nm;
			mn = min(mn,nm);
		}
		if(xr) printf("Case #%d: NO\n",cs);
		else printf("Case #%d: %d\n",cs,tot-mn);
	}
	return 0;
}
