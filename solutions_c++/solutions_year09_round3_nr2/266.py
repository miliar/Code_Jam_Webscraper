#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;
int main () {
	int T;
	cin >> T;
	long long X, Y, Z, VX, VY, VZ;
	long long N;
	for (int xxx = 1; xxx <= T; ++xxx) {
		long long x, y, z, vx, vy, vz;
		cin >> N;
		X = Y = Z = VX = VY = VZ = 0;
		for (int i = 0; i < N; ++i) {
			cin >> x >> y >> z >> vx >> vy >> vz;
			X += x;
			Y += y;
			Z += z;
			VX += vx;
			VY += vy;
			VZ += vz;
		}
		long double t;
		if (VX == 0 && VY == 0 && VZ == 0) {
			t = 0;
			
		} else {
			t = 0 - (X * VX + Y * VY + Z * VZ) * 1.0 / (VX * VX + VY * VY + VZ * VZ);
		}
		if (t < 0) t = 0;
		long double d;
		d = sqrt((X + t * VX) * (X + t * VX) + (Y + t * VY) * (Y + t * VY) + (Z + t * VZ) * (Z + t * VZ));
		d = d / N;
		cout << "Case #" << xxx << ": " << fixed << setprecision(8) << d << " " << fixed << setprecision(8) << t << endl;
	}
}
