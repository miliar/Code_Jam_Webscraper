#include <stdio.h>
#include <limits.h>

int D,I,M,n;

int dt[103][256];
int a[103];

inline int min(int a,int b){
	if(a<b)return a;
	return b;
}

inline int abs(int a){
	if(a < 0)return -a;
	return a;
}

int main(){
	int T;
	int testcase = 0;
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&T);
	while(T-- > 0){
		++testcase;
		int i,j,k;
		scanf("%d%d%d%d",&D,&I,&M,&n);
		for(i=1;i<=n;i++){
			scanf("%d",&a[i]);
		}
		int ans = D * (n-1);
		n++;
		for(i=0;i<256;i++){
			dt[0][i] = 0;
		}
		for(i=1;i<n;i++){
			for(j=0;j<256;j++){ /* current color */
				dt[i][j] = INT_MAX;
				for(k=0;k<256;k++){ /* before color */
					if(M == 0){
						if(j == k){
							dt[i][j] = min(dt[i][j], dt[i-1][k]+D);
							dt[i][j] = min(dt[i][j], dt[i-1][k]+abs(a[i]-j));
						}
					}else{
						dt[i][j] = min(dt[i][j],
							dt[i-1][k]
							+ I*( (abs(a[i]-k)+(a[i] == k)-1) / M )
							+ I*( (abs(a[i]-j)+M-1) / M )
							);
						dt[i][j] = min(dt[i][j],
							dt[i-1][k] + D
							+ I*( (abs(j-k)+M-1) / M )
							);
						dt[i][j] = min(dt[i][j],
							dt[i-1][k] + abs(j-a[i])
							+ I*( (abs(j-k)+(j==k)-1) / M )
							);
					}
				}
			}
			for(j=0;j<256;j++){ /* current color */
				for(k=0;k<256;k++){ /* current color */
					if(M != 0){
						dt[i][j] = min(dt[i][j],
								dt[i][k] + I*( (abs(j-k)+M-1) / M ) );
					}
				}
			}
		}
		for(j=0;j<256;j++){
			if(ans > dt[n-1][j]){
				ans = dt[n-1][j];
			}
		}
		printf("Case #%d: %d\n",testcase,ans);
	}

	return 0;
}
