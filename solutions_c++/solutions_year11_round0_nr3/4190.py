#include<stdio.h>
int main(){
	freopen("lic.in", "r", stdin);
	freopen("lic.txt", "w", stdout);
	int t,m,a,s,n,i,T=0;
	scanf("%d",&t);
	while(T<t){
		scanf("%d",&n);i=10000000;s=m=0;
		while(n--){
			scanf("%d",&a);s+=a;m^=a;if(i>a)i=a;
		}printf("Case #%d: ",++T);if(m){printf("NO\n");}else{printf("%d\n",s-i);}
	}
}  