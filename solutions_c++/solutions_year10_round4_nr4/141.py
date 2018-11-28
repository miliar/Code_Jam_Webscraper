#include <string>
#include <set>
#include <iostream>
#include <stdio.h>
#include <vector>
#include <math.h>

using namespace std;

const long double PI = 3.1415926535897932384626433;
int main ( ) {

	int cases;
	cin >> cases; 
	for ( int caseno = 1; caseno <= cases; caseno++) {
		int N, M;
		cin >> N >> M;
		vector < long double > nx;
		vector < long double > ny;
		vector < long double > qx;
		vector < long double > qy;
		for ( int i = 0; i < N; i ++ )  {
			int x,y;
			cin >> x >> y;
			nx.push_back ( x);
			ny.push_back ( y);

		}
		for ( int i = 0 ; i < M; i ++ ) {
			int x,y;
			cin >> x >> y;
			qx.push_back ( x);
			qy.push_back ( y);
		}
		long double minarea  = 99999999;;
		cout << "Case #" << caseno << ": "; 
		for ( int i = 0; i < qx.size(); i ++ ) {
			long double d1, d2;
			d1 = sqrt((long double)(nx[0] - qx[i])*(nx[0] - qx[i]) + (ny[0] -qy[i])*(ny[0] -qy[i]));
			d2 = sqrt((long double)(nx[1] - qx[i])*(nx[1] - qx[i]) + (ny[1] -qy[i])*(ny[1] -qy[i]));
			long double odl = sqrt((long double)(nx[1] - nx[0])*(nx[1] - nx[0]) + (ny[1] -ny[0])*(ny[1] -ny[0]));
			// jeden w srodku drugiego
			double res = 0;
			if ( d1 + odl <= d2 ) {
				res = d1*d1*PI;
			}
			else if ( d2 + odl <= d1 ) {
				res = d2*d2 * PI;
			}
			else {
				long double a1 = acos ( (d2*d2 - d1*d1 - odl*odl ) / ( -2 * d1 * odl ));
				long double a2 = acos ( (d1*d1 - d2*d2 - odl*odl ) / ( -2 * d2 * odl ));
				// first lens
				long double h1 = d1 * sin(a1);
				long double odl1 = d1 * cos (a1);
				long double h2 = d2 * sin ( a2);
				long double odl2 = d2 * cos ( a2);
				long double pom1 = d1*d1*PI;
				long double pom2 = d2*d2*PI;
				long double pom1a = d1*d1*PI*(a1/PI);
				long double pom2a = d2*d2*PI*(a2/PI);
				long double area1 = d1*d1*PI*(a1/PI) - h1* odl1;
				long double area2 = d2*d2*PI*(a2/PI) - h2* odl2;
				res = area1 + area2;

			}
			if ( res < minarea ) {
				minarea = res;
			}
			cout.precision(10);
			cout << res << " ";
				
		}
		cout << endl;
		
	}

	return 0;

}