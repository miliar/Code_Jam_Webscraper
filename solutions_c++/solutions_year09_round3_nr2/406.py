#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main(){
	int T;
	int N;
	int x, y, z, vx, vy, vz;
	int sumx, sumy, sumz, sumvx, sumvy, sumvz;
   	
	cin >> T; 

	// TODO: check overflow
	for (int cnt = 1; cnt <=T; ++cnt){
		sumx = 0;
		sumy = 0;
		sumz = 0;
		sumvx = 0;
		sumvy = 0;
		sumvz = 0;

		cin >> N;
		for (int i=0; i<N; ++i){
			cin >> x >> y >> z >> vx >> vy >> vz;
			sumx += x;
			sumy += y;
			sumz += z;
			sumvx += vx;
			sumvy += vy;
			sumvz += vz;
		}

		long long a, b, c; // quadratic consts

		a = sumvx*sumvx + sumvy*sumvy + sumvz*sumvz ; // must be positive
		b = 2 * (sumvx * sumx + sumvy * sumy + sumvz * sumz);
		c = sumx*sumx + sumy*sumy + sumz*sumz;

		//cout << a << " " << b << " " << c << endl;

		double time = 0;
		if (-b*1.0/a/2 >= 1e-6){
			time = -b*1.0/a/2;
		} else {
			time = 0;
		}
		double dist;
		double dist2 = (a*time*time+b*time+c)/N/N;
		if (fabs(dist2)<=1e-6)
			dist = 0;
		else 
			dist = sqrt(dist2);

		cout.setf(ios::fixed);

		cout << "Case #" << cnt << ": ";
		cout << setprecision(8) <<  dist << " " << time << endl;
	}
	
	cerr << "Program Terminated Property." << endl;

	return 0;
}
