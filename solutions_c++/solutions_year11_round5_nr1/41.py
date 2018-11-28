#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

#define EPS 1e-8

double L[105][2];
double U[105][2];
int G, l, u, W, T;

double calc_square(){
	double ret = 0;
	for (int i=0; i<u-1; i++){
		ret += (U[i][1] + U[i+1][1])/2.0 * (U[i+1][0] - U[i][0]);
	}
	for (int i=0; i<l-1; i++){
		ret -= (L[i][1] + L[i+1][1])/2.0 * (L[i+1][0] - L[i][0]);
	}
	return ret;
}

double calc_square(double mx){
	double ret = 0;
	for (int i=0; i<u-1; i++){
		if (U[i+1][0] > mx){
			double uf = U[i][1] + (U[i+1][1] - U[i][1])/(U[i+1][0] - U[i][0]) * (mx - U[i][0]);
			ret += (U[i][1] + uf)/2.0 * (mx - U[i][0]);
			break;	
		} else {
			ret += (U[i][1] + U[i+1][1])/2.0 * (U[i+1][0] - U[i][0]);
		}
	}
	for (int i=0; i<l-1; i++){
		if (L[i+1][0] > mx){
			double lf = L[i][1] + (L[i+1][1] - L[i][1])/(L[i+1][0] - L[i][0]) * (mx - L[i][0]);
			ret -= (L[i][1] + lf)/2.0 * (mx - L[i][0]);
			break;	
		} else {
			ret -= (L[i][1] + L[i+1][1])/2.0 * (L[i+1][0] - L[i][0]);
		}
	}
	return ret;
}

int main(){
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	cin >> T;
	for (int I=0; I<T; I++){
		cout << "Case #" << I+1 << ":\n";
		cin >> W >> l >> u >> G;
		for (int i=0; i<l; i++){
			cin >> L[i][0] >> L[i][1];
		}
		for (int i=0; i<u; i++){
			cin >> U[i][0] >> U[i][1];
		}
		double S = calc_square();
		S /= G;
		for (int i=1; i<G; i++){
			double lb = 0, ub = U[u-1][0], ns = S*i;
			for (int j=0; j<80; j++){
				double mb = (ub + lb)/2;
				if (calc_square(mb) > ns){
					ub = mb;
				} else {
					lb = mb;
				}
			}
			cout << fixed << setprecision(10) << lb << endl;
		}
	}
	return 0;
}