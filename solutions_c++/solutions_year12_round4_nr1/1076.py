#include <cmath>
#include <ctime>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <set>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#define maxn 10100
using namespace std;

int d[maxn],l[maxn],f[maxn];

void solve(){
	int n,i,j,maxx,D;
	scanf("%d",&n);
	for(i=1;i<=n;++i){
		scanf("%d%d",&d[i],&l[i]);
		f[i]=-1;
	}
	scanf("%d",&D);
	f[1]=min(d[1],l[1]);
	for(i=1;i<=n;++i){
		maxx=d[i]+min(f[i],l[i]);
		if(maxx>=D){
			printf("YES\n");
			return;
		}
		for(j=i+1;j<=n;++j){
			if(maxx<d[j])break;
			f[j]=max(f[j],min(d[j],d[j]-d[i]));
		}
	}
	printf("NO\n");
}
	

int main(){
	int t,i;
	scanf("%d",&t);
	for(i=1;i<=t;++i){
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}