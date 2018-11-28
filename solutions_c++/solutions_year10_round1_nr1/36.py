#include <stdio.h>
#include <string.h>

char a[100][100];
int b[100][100];

int main(void)
{
	int T, cs=0, n, k, i, j;
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++){
		scanf("%d%d",&n,&k);
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		for(i=0;i<n;i++){
			scanf("%s",a[i]);
		}
		for(i=0;i<n;i++){
			int r=0;
			for(j=n-1;j>=0;j--){
				if(a[i][j] =='R'){
					b[i][r++] = 1;
				}else if(a[i][j]=='B'){
					b[i][r++] = 2;
				}
			}
		}
		int Rflag=0, Bflag=0, u;
		for(i=0;i<n;i++)
			for(j=0;j<=n-k;j++){
				if(b[i][j] == 0) continue;
				for(u=0;u<k;u++){
					if(b[i][j+u] != b[i][j])
						break;
				}
				if(u==k){
					if(b[i][j]==1) Rflag = 1;
					else if(b[i][j]==2) Bflag = 1;
				}
			}
		for(i=0;i<=n-k;i++)
			for(j=0;j<n;j++){
				if(b[i][j]==0) continue;
				for(u=0;u<k;u++){
					if(b[i+u][j] != b[i][j])
						break;
				}
				if(u==k){
					if(b[i][j] == 1) Rflag = 1;
					else if(b[i][j]==2) Bflag = 1;
				}
			}
		for(i=0;i<=n-k;i++)
			for(j=0;j<=n-k;j++){
				if(b[i][j]==0) continue;
				for(u=0;u<k;u++)
					if(b[i+u][j+u] != b[i][j])
						break;
				if(u==k){
					if(b[i][j] == 1) Rflag = 1;
					else if(b[i][j]==2) Bflag = 1;
				}
			}
		for(i=0;i<=n-k;i++)
			for(j=k-1;j<n;j++){
				if(b[i][j]==0) continue;
				for(u=0;u<k;u++)
					if(b[i+u][j-u] != b[i][j])
						break;
				if(u==k){
					if(b[i][j] == 1) Rflag = 1;
					else if(b[i][j]==2) Bflag = 1;
				}
			}
		/*printf("%d %d\n",n,k);
		for(j=n-1;j>=0;j--){
			for(i=n-1;i>=0;i--){
				printf("%c",b[i][j]==0?'.':b[i][j]==1?'R':'o');
			}
			printf("\n");
		}*/
		printf("Case #%d: ", cs);
		if(Rflag && Bflag){
			printf("Both\n");
		}else if(Rflag){
			printf("Red\n");
		}else if(Bflag){
			printf("Blue\n");
		}else
			printf("Neither\n");
	}
	return 0;
}
