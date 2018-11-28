#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
#define LL long long
LL x[1000],y[1000],ans;

int main(){
	int ca; scanf("%d",&ca);
	for (int tt=1; tt<=ca; tt++){
		int n; scanf("%d",&n);
		for (int i=0; i<n; i++) scanf("%lld",x+i);
		for (int i=0; i<n; i++) scanf("%lld",y+i);
		sort(x,x+n); sort(y,y+n);
		ans=0;
		for (int i=0; i<n; i++){
			ans+=x[i]*y[n-i-1];
		}
		printf("Case #%d: %lld\n",tt,ans);
	}
	return 0;
}	
