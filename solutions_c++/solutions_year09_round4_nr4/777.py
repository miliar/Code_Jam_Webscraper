#include <cstdio>
#include <cmath>
#include <algorithm>

double distance(int x1, int y1, int x2, int y2){
	x1 -= x2;
	y1 -= y2;
	return sqrt(x1 * x1 + y1 * y1);
}

double eval(int x[], int y[], int r[], int size){
	switch(size){
	case 1:	return r[0] * 2.0;
	case 2:	return std::max(r[0], r[1]) * 2.0;
	case 3:
		{
			double list[3] = {
				std::max(distance(x[1], y[1], x[2], y[2]) + r[1] + r[2], r[0] * 2.0),
				std::max(distance(x[2], y[2], x[0], y[0]) + r[2] + r[0], r[1] * 2.0),
				std::max(distance(x[0], y[0], x[1], y[1]) + r[0] + r[1], r[2] * 2.0),
			};
			return *std::min_element(list, list + 3);
		}
	default:	break;
	}
	return -2;
}

int main(){
	int C = 0;
	scanf("%d ", &C);
	for(int ccc = 1; ccc <= C; ccc++){
		int N = 0;
		scanf("%d ", &N);
		int x[40] = {0};
		int y[40] = {0};
		int r[40] = {0};
		for(int i = 0; i < N; i++) scanf("%d %d %d ", x + i, y + i, r + i);
		printf("Case #%d: %lf\n", ccc, eval(x, y, r, N) / 2.0);
	}
	return 0;
}
