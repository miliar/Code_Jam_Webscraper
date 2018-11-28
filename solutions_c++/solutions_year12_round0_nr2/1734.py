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
#define maxn 101000
using namespace std;

int p;

bool can(int x){
	if(x<p)return false;
	if(max(p-1,0)*2+p>x)return false;
	return true;
}

bool can2(int x){
	if(x<p)return false;
	if(max(p-2,0)*2+p>x)return false;
	return true;
}

void solve(){
	int n,ans,i,s,x;
	scanf("%d%d%d",&n,&s,&p);
	ans=0;
	for(i=1;i<=n;++i){
		scanf("%d",&x);
		if(can(x))++ans;else if(s>0 && can2(x)){
			++ans;
			--s;
		}
	}
	printf("%d\n",ans);
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