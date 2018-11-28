#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <math.h>

double c[100][3];
int n;
double g[100][100][3];
int cov[50][50][50];
int used[50];

	bool isZero(double x){
		if(x>-1e-8 && x<-1e-8)
			return true;
		return false;
	}

bool p1(int x,int y,double R, int flag, double dir, double dir2){
	double A, B, C, D, U, V, W, X, Y;
	U = (R-c[y][2])*(R-c[y][2]) - c[y][0]*c[y][0] - c[y][1]*c[y][1]
		-(R-c[x][2])*(R-c[x][2]) + c[x][0]*c[x][0] + c[x][1]*c[x][1];
	V = 2.0*(c[x][0] - c[y][0]);
	W = 2.0*(c[x][1] - c[y][1]);
	if(V==0.0){
		Y = U/W;
	}else{ //Ay^2 - 2By+C=0;
		A = V*V+W*W;
		B = (W*(U-V)+ c[x][1]*V*V);
		C = (U-c[x][0]*V)*(U-c[x][0]*V)+V*V*c[x][1]*c[x][1]-V*V*(R-c[x][2])*(R-c[x][2]);
		Y = (B + dir*sqrt(B*B-A*C))/A;
	}
	X = sqrt((R-c[y][2])*(R-c[y][2]) - (Y-c[y][1])*(Y-c[y][1]));
	X += dir2*c[y][0];
	printf("X=%lf Y=%lf R=%lf\n",X,Y,R);
	if(isZero((X-c[y][0])*(X-c[y][0])+(Y-c[y][1])*(Y-c[y][1])-(R-c[y][2])*(R-c[y][2])) && isZero((X-c[x][0])*(X-c[x][0])+(Y-c[x][1])*(Y-c[x][1])-(R-c[x][2])*(R-c[x][2])))
	{
		for(int i=0;i<n;i++){
			if(!used[i] && (X-c[i][0])*(X-c[i][0])+(Y-c[i][1])*(Y-c[i][1])-1e-15<=(R-c[i][2])*(R-c[i][2]))
				used[i] = flag;
		}
		return true;
	}
	return false;

}

void d(int id){
	for(int i=0;i<n;i++)
		if(used[i]==id) used[i]=0;
}
bool pass3(void){
	for(int i=0;i<n;i++)
		if(!used[i])
			return false;
	return true;
}
bool pass2(double R){
	int x,y,flag=0;
	for(x=0;x<n;x++)
		for(y=x+1;y<n;y++)
			if(!used[x] && !used[y]){
				flag=1;
				if(p1(x, y, R, 2, 1.0, 1.0)){
					if(pass3())
						return true;
					d(2);
				}
				if(p1(x, y, R, 2, -1.0, 1.0)){
					if(pass3())
						return true;
					d(2);

				}
				if(p1(x, y, R, 2, 1.0, -1.0)){
					if(pass3())
						return true;
					d(2);

				}
				if(p1(x, y, R, 2, -1.0, -1.0)){
					if(pass3())
						return true;
					d(2);
				}
			}
	if(!flag) return true;
	return false;
}

bool test(double R){
	int x,y;
	x=0;
	for(y=1;y<n;y++){
		if(p1(x, y, R, 1, 1.0, 1.0)){
			if(pass2(R))
				return true;
			d(1);
		}
		if(p1(x, y, R, 1, -1.0, 1.0)){
			if(pass2(R))
				return true;
			d(1);

		}
		if(p1(x, y, R, 1, 1.0, -1.0)){
			if(pass2(R))
				return true;
			d(1);

		}
		if(p1(x, y, R, 1, -1.0, -1.0)){
			if(pass2(R))
				return true;
			d(1);
		}
	}
	return false;
}

double sqr(double x){
	return x*x;
}
double dist(int x,int y){
	return sqrt(sqr(c[x][0]-c[y][0])+sqr(c[x][1]-c[y][1]));
}
int main(void)
{
	int T, cs=0;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		double L=0.0, R=2000.0, M, ans=100000.0;
		for(int i=0;i<n;i++){
			scanf("%lf%lf%lf",&c[i][0],&c[i][1],&c[i][2]);
			if(L<c[i][2]) L = c[i][2];
		}
		if(n==2){
			ans = L;
		}else{
			int i, j;
			double t;
			for(i=0;i<3;i++)
				for(j=i+1;j<3;j++){
					if(dist(i,j)+c[i][2]+c[j][2] < 2.0*c[3-i-j][2]){
						t = c[3-i-j][2]*2.0;
					}else
						t = dist(i,j)+c[i][2]+c[j][2];
					if(ans>t) ans=t;
				}
			ans/=2.0;
		}

		printf("Case #%d: %.7lf\n",++cs,ans);
	}
	return 0;
}

