#include <iostream>
#include <cmath>
using namespace std;

const double Thresh = 1.0E-6;

struct fly {
	int x, y, z, vx, vy, vz;
};

struct c {
	double x, y, z, vx, vy, vz;
};

int K;
c center;

void init() {
	memset(&center, 0, sizeof(c));
	cin >> K;
	fly temp;
	for (int i = 0; i < K; ++i) {
		memset(&temp, 0, sizeof(fly));
		cin >> temp.x >> temp.y >> temp.z >> temp.vx >> temp.vy >> temp.vz;
		center.x += temp.x;
		center.y += temp.y;
		center.z += temp.z;
		center.vx += temp.vx;
		center.vy += temp.vy;
		center.vz += temp.vz;
	}
	center.x /= K;
	center.y /= K;
	center.z /= K;
	center.vx /= K;
	center.vy /= K;
	center.vz /= K;
}

void calc(int N) {
	double t = 0.0;
	double a = pow(center.vx, 2.0) + pow(center.vy, 2.0) + pow(center.vz, 2.0);
	if (abs(a) >= Thresh) {
		double b = center.vx * center.x + center.vy * center.y + center.vz
				* center.z;
		t = -1.0 * b / a;
	}
	if (t < 0.0)
		t = 0.0;
	double d = pow(center.vx * t + center.x, 2.0) + pow(center.vy * t
			+ center.y, 2.0) + pow(center.vz * t + center.z, 2.0);
	d = pow(d, 0.5);
	printf("Case #%d: %.8f %.8f\n", N, d, t);
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("b-large.out", "w", stdout);

	int N;
	cin >> N;
	for (int i = 0; i < N; ++i) {
		init();
		calc(i + 1);
	}
	return 0;
}
