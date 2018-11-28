#include<stdio.h>
long T,TT,l,h,n,i,j;
long f[101];
inline bool check(){
	for(j=0;j<n;++j)
		if(i%f[j]&&f[j]%i)
			return 0;
	return 1;
}
int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	for(scanf("%ld",&T),TT=0;TT<T;){
		scanf("%ld%ld%ld",&n,&l,&h);
		for(i=0;i<n;++i)
			scanf("%ld",f+i);
		for(i=l;i<=h;++i)
			if(check())
				break;
		printf("Case #%ld: ",++TT);
		if(i==h+1) puts("NO");
		else printf("%ld\n",i);
		}
	scanf("%ld",&T);
	return 0;
}
