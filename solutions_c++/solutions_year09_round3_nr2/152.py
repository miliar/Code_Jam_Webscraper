#include <cstdio>
#include <cmath>
using namespace std;
#define eps 1e-10
double X, Y, Z, VX, VY, VZ;
int N;
int sgn(double x){
	return (int)((x > eps) - (x <-eps));
}
void init(){
	double x, y, z, vx, vy, vz;
	scanf("%d", &N);
	X = Y = Z = 0.0;
	VX = VY = VZ = 0.0;
	for (int i = 0; i < N; i++) {
		scanf("%lf%lf%lf%lf%lf%lf", &x, &y ,&z, &vx, &vy, &vz);
		X += x;
		Y += y;
		Z += z;
		VX += vx;
		VY += vy;
		VZ += vz;
	}
	X /= N;
	Y /= N;
	Z /= N;
	VX /= N;
	VY /= N;
	VZ /= N;
}
void solve(){
	double A, B, C, ans, x0;
	A = VX*VX + VY*VY + VZ*VZ;
	B = 2*(X*VX + Y*VY + Z*VZ);
	C = X*X + Y*Y + Z*Z;
	
	if ( sgn(A)== 0 ) {
		x0 = 0;
		ans = sqrt(fabs(X*X + Y*Y + Z*Z));
	}
	else {
	    x0 = -B/A*0.5;
	    if (sgn(x0) < 0) x0 = 0.0;
		ans = sqrt(fabs(A*x0*x0 + B*x0 + C));
	}
	
	if ( sgn(ans) == 0) ans = 0.0;
	if ( sgn(x0) == 0) x0 = 0.0;
	printf("%.8lf %.8lf\n", ans, x0);
}
int main(){
//	freopen("test.in", "r", stdin);
//	freopen("test.out", "w", stdout);
	int Case;
	scanf("%d", &Case);
	for (int t = 1; t <= Case; t++){
		printf("Case #%d: ", t);
		init();
		solve();
	}
	return 0;
}
