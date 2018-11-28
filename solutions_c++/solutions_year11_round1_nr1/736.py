#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
typedef long long lint;
int pd,pg;
lint n;
bool check(){
	if (pg==100){
		if (pd!=100) return false;
		return true;
	}
	if (pg==0){
		if (pd!=0) return false;
		return true;
	}
	if (n>=100) return true;
	int i;
	for (i=1;i<=n;i++){
		if (pd*i%100==0){
			return true;
		}
	}
	return false;
}
void init(){
	scanf("%lld%d%d",&n,&pd,&pg);
}
void solve(){
	if (check()){
		printf("Possible\n");
	}else{
		printf("Broken\n");
	}
}
int main()
{
//	freopen("A-small-attempt1.in","r",stdin);
//	freopen("A-small-attempt1.out","w",stdout);
	int i,t;
	scanf("%d",&t);
	for (i=1;i<=t;i++){
		printf("Case #%d: ",i);
		init();
		solve();
	}
	return 0;
}