#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include<algorithm>

using namespace std;

const int N  = 520;
const double eps = 1e-6;

double mass[N][N],smass[N][N];
string ma[N];
double p[N][N][3],sp[N][N][3];
int ii,jj,n,m,d,kk,Test;
double xx,yy,totsp0,totsp1,totmass;


void work(){
	cin >> n >> m >> d;
	for (int i = 0;i<n;++i){
	cin >> ma[i];
	}
	
	for (int i = 0;i<n;++i)
	for (int j = 0;j<m;++j){
	   mass[i+1][j+1] = (double)(ma[i][j]-'0'+d);
	}
	for (int i = 1;i<=n;++i)
	for (int j = 1;j<=m;++j)
	   smass[i][j] = smass[i-1][j]+smass[i][j-1]-smass[i-1][j-1]+mass[i][j];

	for (int i = 1;i<=n;++i)
	for (int j = 1;j<=m;++j){ 
	   p[i][j][0] = (double)(i-0.5)*mass[i][j];
	   p[i][j][1] = (double)(j-0.5)*mass[i][j];
	}
	for (int i = 1;i<=n;++i)
	for (int j = 1;j<=m;++j){
		sp[i][j][0] = sp[i-1][j][0]+sp[i][j-1][0]-sp[i-1][j-1][0]+p[i][j][0];
		sp[i][j][1] = sp[i-1][j][1]+sp[i][j-1][1]-sp[i-1][j-1][1]+p[i][j][1];
	}

	kk = min(n,m);
	for (int k = kk;k>=3;--k){
	for (int i = 1;i<=n-k+1;++i)
	for (int j = 1;j<=m-k+1;++j){
			ii = i+k-1;
			jj = j+k-1;
		
			totmass = smass[ii][jj]-smass[i-1][jj]-smass[ii][j-1]+smass[i-1][j-1]
					-mass[ii][jj]-mass[ii][j]-mass[i][jj]-mass[i][j];
			totsp0 = sp[ii][jj][0]+sp[i-1][j-1][0]-sp[ii][j-1][0]-sp[i-1][jj][0]-
					p[ii][jj][0]-p[ii][j][0]-p[i][jj][0]-p[i][j][0];
					
			totsp1 = sp[ii][jj][1]+sp[i-1][j-1][1]-sp[ii][j-1][1]-sp[i-1][jj][1]-
					p[ii][jj][1]-p[ii][j][1]-p[i][jj][1]-p[i][j][1];
					
			xx = ( (double)(i+ii)/2-0.5) * totmass;
			yy = ( (double)(j+jj)/2-0.5) * totmass;

			if ( fabs(xx-totsp0)<eps && fabs(yy-totsp1)<eps ) {
				printf("%d\n",k);
				return;
			}
		}
	
	}
	printf("IMPOSSIBLE\n");
}
int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	cin >> Test;
	for (int ii = 1;ii<=Test;++ii){
		printf("Case #%d: ",ii);
		work();
	}
	return 0;
}
