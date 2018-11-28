#include<iostream>
#include<algorithm>
using namespace std;
int a[100000];
long long anz;
main(){
	int tt,t,i,p,k,l,x;
	scanf("%d",&t);
	for(tt=1;tt<=t;tt++){
		scanf("%d",&p);
		scanf("%d",&k);
		scanf("%d",&l);
		for(i=0;i<l;i++){
			scanf("%d",&a[i]);
		}
		sort(a,a+l);
		x = 0;
		anz = 0;
		for(i=l-1;i>=0;i--){
			anz += (long long)a[i]*(x/k+1);
			x++;
		}
		printf("Case #%d: %lld\n",tt,anz);
	}
	return 0;
}
