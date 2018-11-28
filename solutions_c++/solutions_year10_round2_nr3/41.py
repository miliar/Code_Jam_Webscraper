#include <stdio.h>

#define P 100003

typedef long long ll;

ll binom[1000][1000];

ll a[1000][1000];

ll ans[1000];

main(){
	for(int i=0;i<1000;i++){
		for(int j=0;j<=i;j++){
			if(j==0 || j==i)binom[i][j]=1;
			else binom[i][j]=(binom[i-1][j-1]+binom[i-1][j])%P;
		}
	}
	
	for(int n=2;n<=500;n++){
		for(int m=1;m<=n;m++){
			a[n][m]=0;
			if(m==1)a[n][m]=1;
			else{
				for(int i=1;i<=m-1;i++){
					if(n-m>=m-i)a[n][m]=(a[n][m]+a[m][i]*binom[n-m-1][m-i-1])%P;
				}
			}
		}
		ans[n]=0;
		for(int m=1;m<=n;m++)ans[n]=(ans[n]+a[n][m])%P;
	}
	
	int tests;
	scanf("%d",&tests);
	for(int t=1;t<=tests;t++){
		int n;
		scanf("%d",&n);
		printf("Case #%d: %lld\n",t,ans[n]);
	}
}