#include<cstdio>
typedef long long LL;

int main(){
	int nnn;
	scanf("%d", &nnn);
	for(int nn=1;nn<=nnn;nn++){
		int n, k;
		long long x=1;
		scanf("%d%d", &n, &k);
		for(int i=1;i<n;i++)x*=2;
		printf("Case #%d: %s\n", nn, (k+1)%(x*2)==0?"ON":"OFF");
	}
	return 0;
}
