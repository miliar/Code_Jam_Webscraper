#include<cstdio>
typedef long long LL;

LL gcd(LL a, LL b){
	if(a==0)return b;
	return gcd(b%a, a);
}
int main(){
	int nnn;
	scanf("%d", &nnn);
	for(int nn=1;nn<=nnn;nn++){
		int n, k;
		long long a,b,c,g=0;
		scanf("%d", &n);
		scanf("%I64d", &a);
		
		for(int i=1;i<n;i++){
			scanf("%I64d", &b);
			c=a-b;
			if(c<0)c=-c;
			g = gcd(g, c);
		}
		printf("Case #%d: %I64d\n",nn, g==0?0:((-a)%g+g)%g);
	}
	return 0;
}
