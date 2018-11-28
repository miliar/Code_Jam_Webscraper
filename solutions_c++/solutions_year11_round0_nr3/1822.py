#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;

int main(){
	int t, time=0, ans, m, n, k, sum;
	scanf("%d", &t);
	while(t--){
		scanf("%d%d", &n, &ans);
		sum=m=ans;
		while(--n){
			scanf("%d", &k);
			sum+=k;
			ans^=k;
			m=min(k, m);
		}
		printf("Case #%d: ", ++time);
		if(ans) puts("NO");
		else printf("%d\n", sum-m);

	}
    return 0;
}
