#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cmath>
#include <iostream>
#define eps (1e-7)
#define N 505
#define LL long long int

double px[N][N],py[N][N],SX,SY,MASS,tx,ty;
LL d[N][N],s[N][N];
int w,AC,TC,n,m,D;
char ts[N];

using namespace std;

int main(){
	scanf("%d",&TC);
	for (int C=1;C<=TC;C++){
		
		scanf("%d%d%d",&n,&m,&D);
		AC=0;
		
		for (int i=0;i<=n+1;i++)
			for (int j=0;j<=m+1;j++){
				px[i][j]=py[i][j]=0.0;
				d[i][j]=0;
				s[i][j]=0;
			}
		
		for (int i=1;i<=n;i++){
			scanf("%s",ts);
			for (int j=1;j<=m;j++){
				d[i][j]=ts[j-1]-'0';
				d[i][j]+=D;
				
				s[i][j]=s[i][j-1]+s[i-1][j]-s[i-1][j-1]+d[i][j];
				
				tx = i-0.5;
				ty = j-0.5;
				
				px[i][j]=px[i][j-1]+px[i-1][j]-px[i-1][j-1]+tx*d[i][j];
				py[i][j]=py[i][j-1]+py[i-1][j]-py[i-1][j-1]+ty*d[i][j];
				
				
			}
		}
		
		for (int i=1;i<=n;i++)
			for (int j=1;j<=m;j++){
				w = min(i,j);
				for (int k=3;k<=w;k++){
					double rx = i-k*1.0/2,ry=j-k*1.0/2;
					MASS = s[i][j]-s[i][j-k]-s[i-k][j]+s[i-k][j-k]
						   -d[i][j]-d[i-k+1][j]-d[i][j-k+1]-d[i-k+1][j-k+1];
						   
					SX = px[i][j]-px[i-k][j]-px[i][j-k]+px[i-k][j-k]
						-(i-k+0.5)*(d[i-k+1][j]+d[i-k+1][j-k+1])
						-(i-0.5)*(d[i][j]+d[i][j-k+1]);
					
					SY = py[i][j]-py[i-k][j]-py[i][j-k]+py[i-k][j-k]
						-(j-k+0.5)*(d[i][j-k+1]+d[i-k+1][j-k+1])
						-(j-0.5)*(d[i][j]+d[i-k+1][j]);
						
					if (fabs(rx*MASS-SX)<eps && fabs(ry*MASS-SY)<eps){
						if (AC<k) AC=k;
					}
				}
			}
			
		printf("Case #%d: ",C);
		if (AC==0) printf("IMPOSSIBLE\n");
		else printf("%d\n",AC);
		
	}
	//scanf("\n");
	return 0;
}
