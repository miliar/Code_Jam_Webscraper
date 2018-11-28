#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <cstdlib>
using namespace std;

int main() {
	
	int Nx;
	cin >> Nx;
	for(int nx = 1; nx <= Nx; ++nx) {
		cout << "Case #" << nx << ": ";

		int N;
		cin >> N;
		vector<int> x(N), y(N), z(N), p(N);
		for(int i = 0; i != N; ++i) {
			cin >> x[i] >> y[i] >> z[i] >> p[i];
		}
		double x0 = 0.0, y0 = 0.0, z0 = 0.0;
		double mp0 = 0.0;
		for(double st = 10000.0; st > 1e-20; st *= 0.995) {
			for(int j = 0; j != 20; ++j) {
				double x1 = x0, y1 = y0, z1 = z0;
				if(j == 0);
				else {
					x1 += st*(1.0*rand()/RAND_MAX-0.5);
					y1 += st*(1.0*rand()/RAND_MAX-0.5);
					z1 += st*(1.0*rand()/RAND_MAX-0.5);
				}
				
				double mp = 0.0;
				for(int i = 0; i != N; ++i) {
					mp = max(mp, (fabs(x1-x[i])+fabs(y1-y[i])+fabs(z1-z[i]))/p[i]);
				}
				if(j == 0) mp0 = mp;
				else if(mp < mp0) {
					mp0 = mp;
					x0 = x1;
					y0 = y1;
					z0 = z1;
				}
			}
		}
		
		cout << setprecision(10) << mp0;
		
		cout << endl;
	}
	
}
