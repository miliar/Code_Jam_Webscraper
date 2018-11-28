#include <stdio.h>
#include <iostream>
#include <set>
#include <map>
#include <string>
#include <string.h>
#include <queue>
#include <algorithm>
#include <math.h>
#include <sstream>
using namespace std;
typedef pair<int, int> pi;
typedef long long int li;
typedef vector<int> vi;
void solve();
#define mp make_pair
#define pb push_back

int main(){
#ifdef DEBUG
    freopen("input", "r", stdin);
    freopen("output","w",stdout);
#endif
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;++i){
		printf("Case #%d: ",i);
		solve();
	}
    return 0;
}

void solve(){
	int n,sum=0,mn=1LL<<30,xr=0;
	scanf("%d",&n);
	for(int i=0;i<n;++i){
		int x;
		scanf("%d",&x);
		mn=min(mn,x);
		sum+=x;
		xr^=x;
	}
	if(xr)
		printf("NO\n");
	else
		printf("%d\n",sum-mn);
}