#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int test,t,n,k,x,y,i,s;

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for (test=1; test<=t; ++test) {
		scanf("%d%d",&n,&k);
		s=1;
		for (i=1; i<=n; ++i) s*=2;
		--s;
		//printf("s=%d    k=%d\n",s,k);
		if (k==0 || (k-s)%(s+1)!=0) printf("Case #%d: OFF\n",test);
		else printf("Case #%d: ON\n",test);
	}
    return 0;
}