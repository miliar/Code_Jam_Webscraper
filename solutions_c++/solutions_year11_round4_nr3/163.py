#include <cmath>
#include <ctime>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#define maxl 1000000000
#define maxn 50000
using namespace std;

typedef long long ll;

const double eps=1e-8;

int tot;
int zs[1010000],small[1010000];

void solve(){
	ll n,ans,now;
	int i;
	cin>>n;
	if(n==1)ans=0;else ans=1;
	for(i=1;i<=tot;++i){
		now=(ll)zs[i]*zs[i];
		if(now>n)break;
		while(now<=n){
			++ans;
			now*=zs[i];
		}
	}
	cout<<ans<<endl;
}
	

int main(){
	int t,i,j;
	scanf("%d",&t);
	tot=0;
	for(i=2;i<=1000000;++i)if(small[i]==0){
		zs[++tot]=i;
		if(i<=1000)for(j=i*i;j<=1000000;j+=i)if(small[j]==0)small[j]=i;
	}
	for(i=1;i<=t;++i){
		printf("Case #%d: ",i);
		solve();
	}
} 
