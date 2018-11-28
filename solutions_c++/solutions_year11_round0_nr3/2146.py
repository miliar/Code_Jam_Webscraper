#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <set>
#include <queue>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <iostream>

using namespace std;

int main() {
	int t,n,x,mini,a,sum,tes=1;
	scanf("%d",&t);
	while (t--) {
		mini=2000000000;
		a=0;
		sum=0;
		scanf("%d",&n);
		for (int i=0;i<n;i++) {
			scanf("%d",&x);
			mini=min(mini,x);
			a=a^x;
			sum+=x;
		}
		printf("Case #%d: ",tes++);
		if (a==0) printf("%d\n",sum-mini); else printf("NO\n");
			
	}
	return 0;
}
