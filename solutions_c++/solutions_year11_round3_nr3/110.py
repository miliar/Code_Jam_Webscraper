#include<cstdio>
int b,t,n,l,h,a[10005],g,ok,ac;
int gcd(int x,int y){
	 if (x%y==0) return y;
	 else return (gcd(y,x%y));
}
int main(){
	scanf("%d",&t);
	for (int z=1; z<=t; z++){
		ok=0;
		scanf("%d%d%d",&n,&l,&h);
		for (long long i=1; i<=n; i++)
		    scanf("%d",&a[i]);
		for (ac=l; ac<=h; ac++){
			b=1;
		    for (int i=1; i<=n; i++)
		    	if ((a[i]%ac!=0)&&(ac%a[i]!=0)){
			   	   b=0; break;
			    }
			if (b){ok=1; break;}
		}
		printf("Case #%d: ",z);
		if (!ok) printf("NO\n");
		else printf("%d\n",ac);
	}
	return 0;
}
