#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>

using namespace std;

long long gcd(long long a, long long b){
	return a == 0 ?b : gcd(b%a, a);
}
bool solve(){
	long long gc, p, d, i, t, m = 100;
	scanf ("%lld%lld%lld", &t, &d, &p);
	
	if(p== 100){
		return (d == 100)? true : false;
	}
	else if(p == 0)
	{
		return (d == 0)? true : false;
	}
	if(d == 0) return true;
	gc = gcd(m, d);
	m /= gc;
	d /= gc;
	
	if(m > t) return false;
	else return true;
	
}
int main(){
	int cas;
	int i;
	bool flag;
	freopen("d:\\A-large.in","r", stdin);
	freopen("d:\\A.out","w", stdout);
	scanf ("%d", &cas);
	for(i = 1;i <= cas; i ++){
		flag = solve();
		printf("Case #%d: %s\n", i, flag?"Possible":"Broken");
	}
	return 0;
}