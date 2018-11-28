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
#define mod 1000000007
using namespace std;

typedef long long ll;

void solve(){
	int p[2],t[2],n,now,x,xx,i,delta;
	char s[10];
	p[0]=1;p[1]=1;
	t[0]=0;t[1]=0;
	scanf("%d",&n);
	now=0;
	for(i=1;i<=n;++i){
		scanf("%s%d",s,&x);
		if(s[0]=='O')xx=0;else xx=1;
		delta=abs(p[xx]-x)-(now-t[xx]);
		if(delta>0)now+=delta;
		++now;
		p[xx]=x;
		t[xx]=now;
	}
	printf("%d\n",now);
}
		
		

int main(){
	int t,i;
	scanf("%d",&t);
	for(i=1;i<=t;++i){
		printf("Case #%d: ",i);
		solve();
	}	
}
