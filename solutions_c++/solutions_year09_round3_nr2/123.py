#include <stdio.h>
#include <math.h>
using namespace std;

double x, y, z, vx, vy, vz;
int N;
double MyX, Y, Z, velMyX, velY, velZ;

void solve(int C) {
	// Çóµ¼£¬¡£¡£¡£
	double t = -(velMyX * MyX + Y * velY + Z * velZ) / ((velMyX * velMyX + velY * velY + velZ * velZ));
	if (t > 0) {} else {
		t = 0;
	}
	double d = sqrt((MyX + velMyX * t) * (MyX + velMyX * t) + (Y + velY * t) * (Y + velY * t) + (Z + velZ * t) * (Z + velZ * t));
	d = d / N;
	printf("Case #%d: %.8lf %.8lf\n", C, d, t);
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	int C = 1;
	for (C = 1; C <= T; C ++) {
		scanf("%d", &N);
		MyX = Y = Z = velMyX = velY = velZ = 0;
		for (int i = 0;i < N;i++) {
			scanf("%lf %lf %lf %lf %lf %lf", &x, &y, &z, &vx, &vy, &vz);
			MyX += x;Y += y;Z += z;velMyX += vx;velY += vy;velZ += vz;
		}
		solve(C);
	}
	return 0;
}
