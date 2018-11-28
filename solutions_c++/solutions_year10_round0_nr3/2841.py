#include<iostream>
#include<cstdio>
using namespace std;

int main(){
	freopen("D:\\C-small-attempt0.in","r",stdin);
	freopen("D:\\C-small-attempt0.out","w",stdout);
	int t,r,k,n,a[1010],sum,head;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		scanf("%d%d%d",&r,&k,&n);
		sum=0;
		for(int j=0;j<n;j++){
			scanf("%d",&a[j]);
			sum+=a[j];
		}
		if(sum<=k){
			printf("Case #%d: %d\n",i,sum*r);
			continue;
		}
		sum=0,head=0;
		for(int j=0;j<r;j++){
			int tt=0;
			while(tt+a[head]<=k){
				tt+=a[head++];
				head%=n;
			}
			sum+=tt;
		}
		printf("Case #%d: %d\n",i,sum);
	}
	return 0;
}