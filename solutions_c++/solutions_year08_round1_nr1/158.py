#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define MAXN 2000

int n;
long long x[MAXN],y[MAXN];

int main(){
	
	int t,lp;
	int i;
	long long ret;
	
	scanf("%d",&t);
	
	for(lp=1;lp<=t;lp++){
		scanf("%d",&n);
		for(i=0;i<n;i++) scanf("%lld",&x[i]);
		for(i=0;i<n;i++) scanf("%lld",&y[i]);
		sort(&x[0],&x[n]);
		sort(&y[0],&y[n]);
		reverse(&y[0],&y[n]);
		ret = 0;
		for(i=0;i<n;i++) ret += x[i]*y[i];
		printf("Case #%d: %lld\n",lp,ret);
	}
	
	return 0;
	
}
