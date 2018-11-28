#include <cmath>
#include <ctime>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#define maxn 1010
using namespace std;

typedef long long ll;

void solve(){
	int n,now,minn,sum,x,i;
	scanf("%d",&n);
	now=0;minn=1100000;sum=0;
	for(i=1;i<=n;++i){
		scanf("%d",&x);
		minn=min(minn,x);
		now^=x;
		sum+=x;
	}
	if(now!=0)printf("NO\n");else printf("%d\n",sum-minn);
}
		
		

int main(){
	int t,i;
	scanf("%d",&t);
	for(i=1;i<=t;++i){
		printf("Case #%d: ",i);
		solve();
	}	
}
