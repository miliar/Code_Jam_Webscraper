#include<stdio.h>
#include<set>

using namespace std;

#define SIZE 100009

int x[SIZE],y[SIZE];
//int ctx[3][SIZE],cty[3][SIZE],
int ct[SIZE][3][3];

int main(){
	int N,n,a,b,c,d,x0,y0,mod,t,res,tx,ty,tmx,tmy,i,j,k;
	long long A,B,C,D;
	
	freopen("as.in","r",stdin);
	freopen("as.out","w",stdout);
	
	scanf("%d",&N);
	for(t = 1; t<=N; ++t){
		scanf("%d%d%d%d%d%d%d%d",&n,&a,&b,&c,&d,&x[0],&y[0],&mod);
		
	//	memset(ctx,0,sizeof(ctx));
		//memset(cty,0,sizeof(cty));
		memset(ct,0,sizeof(ct));
		
		A = a, B = b,C = c, D = d;
//		ctx[ x[0]%3 ][1] = 1;
//		cty[ y[0]%3 ][1] = 1;
		ct[1][x[0]%3][y[0]%3] = 1;
		for(i = 1; i<n; ++i){
			tx = x[i] = ( (A * x[i-1])%mod + B ) % mod;
			ty = y[i] = ( (C * y[i-1])%mod + D ) % mod;
			for(j=0; j<3; ++j){
				//ctx[j][i+1] = ctx[j][i];
				//cty[j][i+1] = cty[j][i];
				for(k = 0; k<3; ++k){
					ct[i+1][j][k] = ct[i][j][k];
				}
			}
			
//			ctx[tx%3][i+1]++;
//			cty[ty%3][i+1]++;
			ct[i+1][tx%3][ty%3]++;
		}
		
		res = 0;
		for(i=0; i<n; ++i){
			for(j = i+1; j<n-1; ++j){
				tmx = (x[i]%3 + x[j]%3) %3;
				tmy = (y[i]%3 + y[j]%3) %3;
				
				tmx = (3 - tmx)%3;
				tmy = (3 - tmy)%3;				
				
				res += ct[n][tmx][tmy] - ct[j+1][tmx][tmy];
			}
		}
		
		//for(i=0; i<n; ++i){ printf("%d %d\n",x[i],y[i]);}
		printf("Case #%d: %d\n",t,res);
	}
	
//	scanf(" ");
	return 0;
}
