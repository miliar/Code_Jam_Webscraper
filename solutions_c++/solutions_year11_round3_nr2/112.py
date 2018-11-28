#include<cstdio>
#include<algorithm>
using namespace std;
long long T,t,l,n,c,a[1005],k,b[1000005],m;
long long ac;
bool cmp(long long u,long long v){
	 return (u>v);
}
int main(){
	scanf("%I64d",&T);
	for (long long z=1; z<=T; z++){
		scanf("%I64d%I64d%I64d%I64d",&l,&t,&n,&c);
		for (long long i=0; i<c; i++) scanf("%I64d",&a[i]),a[i]*=2;
		ac=0; k=0;
		while (ac+a[k%c]<=t&&k<n){
			  ac+=a[k%c];
			  ++k;
		}
		m=0;
		for (long long i=k; i<n; i++){
			if (i==k) b[++m]=a[i%c]-(t-ac);
			else b[++m]=a[i%c];
		}
		if (k<n)
		   ac=t;
		if (m>0){
		   sort(b+1,b+m+1,cmp);
		   for (long long i=1; i<=m; i++){
			   if (l>0){
				  ac+=(b[i]/2);
				  --l;
			   }
			   else ac+=b[i];
		   }
		}
		printf("Case #%I64d: %I64d\n",z,ac);
	}
	return 0;
}
