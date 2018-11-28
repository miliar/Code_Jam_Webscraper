#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<queue>
#include<utility>
#include<cmath>
#include<string>
using namespace std;

#define llong long long 
const double pi = acos(-1.0);
const int maxInt = 0x7fffffff;
const int minInt = ~maxInt;


llong L,P,C,ans;

bool yes(int x){
	int t = 1<<x,i;
	llong res = 1;
	for(i = 0;i<t;i++){
		res *= C;
	}
	if(res*L>=P)return true;
	return false;
}
int main(){
	freopen("B-large.in","r",stdin);freopen("out.txt","w",stdout);
    int i,j,k,t,nc = 0;
	scanf("%d",&t);
	while(t--){
		scanf("%lld%lld%lld",&L,&P,&C);
		for(i = 0;;i++){
			if(yes(i))break;
		}
		printf("Case #%d: %d\n",++nc,i);
	}
    return 0;
}