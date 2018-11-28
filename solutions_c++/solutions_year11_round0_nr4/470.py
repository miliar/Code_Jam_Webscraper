#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <map>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
#define maxn 60
using namespace std;

typedef long long ll;

int a[1010];
bool visit[1010];

void solve(){
	int i,temp,now,n;
	scanf("%d",&n);
	for(i=1;i<=n;++i){
		scanf("%d",&a[i]);
		visit[i]=false;
	}
	double ans=0;
	for(i=1;i<=n;++i)if(!visit[i]){
		visit[i]=true;
		temp=a[i];
		now=1;
		while(temp!=i){
			visit[temp]=true;
			++now;
			temp=a[temp];
		}
		if(now>1)ans+=now;
	}
	printf("%.6f\n",ans);
}

int main(){
	int t,i;
	scanf("%d",&t);
	for(i=1;i<=t;++i){
		printf("Case #%d: ",i);
		solve();
	}
}

