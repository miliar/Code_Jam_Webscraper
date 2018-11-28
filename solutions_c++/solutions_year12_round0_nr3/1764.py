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

int a,b;

bool pre(int x){
	int pre=11,y;
	while(x>0){
		y=x%10;
		if(y>pre)return false;
		pre=y;
		x/=10;
	}
	return true;
}

int ten[10];

int getlen(int x){
	int len=0;
	while(x>0){
		++len;
		x/=10;
	}
	return len;
}
	

int did(int x){
	int len=getlen(x),i,now,y;
	now=x;
	vector<int> v;
	for(i=1;i<len;++i){
		y=now%10;
		now=now/10+y*ten[len-1];
		if(now>x && now<=b)v.push_back(now);
	}
	/*cout<<x<<endl;
	for(i=0;i<v.size();++i)cout<<" "<<v[i];
	cout<<endl;*/
	sort(v.begin(),v.end());
	return unique(v.begin(),v.end())-v.begin();
}

void solve(){
	scanf("%d%d",&a,&b);
	long long ans=0;
	int i;
	for(i=a;i<b;++i){
		ans+=did(i);
	}
	cout<<ans<<endl;
}

int main(){
	int t,i;
	ten[0]=1;
	for(i=1;i<=8;++i)ten[i]=ten[i-1]*10;
	scanf("%d",&t);
	for(i=1;i<=t;++i){
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}