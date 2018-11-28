#include <cstdio>
#include <cmath>
#include <algorithm>

int main(){
	int T = 0;
	scanf("%d ", &T);
	for(int ttt = 1; ttt <= T; ttt++){
		int N = 0;
		scanf("%d ", &N);
		double sum_x = 0, sum_y = 0, sum_z = 0, sum_vx = 0, sum_vy = 0, sum_vz = 0;
		for(int i = 0; i < N; i++){
			int x = 0, y = 0, z = 0, vx = 0, vy = 0, vz = 0;
			scanf("%d %d %d %d %d %d ", &x, &y, &z, &vx, &vy, &vz);
			sum_x  +=  x;	sum_y  +=  y;	sum_z  +=  z;
			sum_vx += vx;	sum_vy += vy;	sum_vz += vz;
		}
		sum_x  /= N;	sum_y  /= N;	sum_z  /= N;
		sum_vx /= N;	sum_vy /= N;	sum_vz /= N;
		double t2 = sum_vx * sum_vx + sum_vy * sum_vy + sum_vz * sum_vz;
		double t1 = sum_x  * sum_vx + sum_y  * sum_vy + sum_z  * sum_vz;
		double t  = (t2 != 0.0) ? -t1 / t2 : 0.0;
		if(t <= 0) t = 0;
		sum_x += sum_vx * t;
		sum_y += sum_vy * t;
		sum_z += sum_vz * t;
		printf("Case #%d: %.8lf %.8lf\n", ttt, sqrt(sum_x * sum_x + sum_y * sum_y + sum_z * sum_z), t);
	}
	return 0;
}
