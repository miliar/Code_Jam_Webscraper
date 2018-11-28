#include <cstdio>
#include <cmath>

double Px, Py, Pz, Vx, Vy, Vz;

double calc(double t){
	return (Px+t*Vx)*(Px+t*Vx) + (Py+t*Vy)*(Py+t*Vy) + (Pz+t*Vz)*(Pz+t*Vz);
}

int main(){
	int T;
	scanf("%d", &T);

	for (int tt = 1; tt <= T; ++tt){
		int N;
		scanf("%d", &N);
		Px = Py = Pz = Vx = Vy = Vz = 0;

		for (int i = 0; i < N; ++i){
			int x, y, z, vx, vy, vz;
			scanf("%d%d%d%d%d%d", &x, &y, &z, &vx, &vy, &vz);
			Px += x; Py += y; Pz += z;
			Vx += vx; Vy += vy; Vz += vz;
		}
		Px /= N; Py /= N; Pz /= N;
		Vx /= N; Vy /= N; Vz /= N;

		double left = 0, right = 15000;

		for (int i = 0; i < 10000; ++i){
			double pl = left+(right-left)/3, pr = left+2*(right-left)/3;
			//printf("%lf (%lf, %lf) (%lf, %lf) %lf\n", left, pl, sqrt(calc(pl)), pr, sqrt(calc(pr)), right);

			if (calc(pl) > calc(pr)) left = pl;
			else right = pr;
		}

		printf("Case #%d: %lf %lf\n", tt, sqrt(calc(left)), left);

	}
	

	return 0;
}
