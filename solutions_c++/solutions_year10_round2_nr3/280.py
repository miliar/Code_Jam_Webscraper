#include<stdio.h>
#include<memory.h>
#include<algorithm>
#include<math.h>
#include<stdlib.h>
#define M 100003

int T;
int c[555][555],f[555][555],n;


int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d\n",&T);


	c[0][0]=1;
	for(int i=1;i<=500;i++){
		c[i][0]=1;
		for(int j=1;j<=i;j++) c[i][j]=(c[i-1][j]+c[i-1][j-1])%M;
	}

	for(int _=1;_<=T;_++){
		scanf("%d",&n);
		memset(f,0,sizeof(f));
		for(int i=2;i<=n;i++){
			f[i][1]=1;
			for(int j=2;j<i;j++) 
				for(int k=1;k<j;k++)
					f[i][j]=(f[i][j]+((long long)f[j][k]*c[i-j-1][j-k-1])%M)%M;
		}
		int ans=0;
		for(int i=1;i<=n;i++) ans=(ans+f[n][i])%M;
		
		printf("Case #%d: %d\n",_,ans);
	}
	return 0;
}
