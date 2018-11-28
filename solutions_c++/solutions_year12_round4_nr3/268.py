/* Let's rock'n'roll! :) */

#include <fstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <climits>

using namespace std;

#define MAX(x, y) ((x) >= (y) ? (x) : (y))
#define MIN(x, y) ((x) <= (y) ? (x) : (y))
#define ABS(x)		((x) >=  0  ? (x) :-(x))

fstream in("in.txt", fstream::in);
fstream out("out.txt", fstream::out);

void line(int n1, double alt1, int n2, double alt2, double &a0, double &a1){
	a1 = (alt1 - alt2) / (n1 - n2);
	a0 = alt1 - n1 * a1;
}

double altn(int n, double a0, double a1){
	return n * a1 + a0;
}

void solve(){
	bool possible = true;
	int N; in >> N;
	int *x = new int [N - 1];
	double a0, a1;
	double *alt = new double [N];
	for(int n = 0; n < N - 1; n++){
		in >> x[n];
		x[n]--;
	}
	alt[N - 1] = 1.0;
	alt[N - 2] = 1.0;
	for(int n = N - 3; n >= 0; n--){
		double altmin = -DBL_MAX, altmax = DBL_MAX;
		for(int i = x[n] + 1; i < N; i++){
			line(x[n], alt[x[n]], i, alt[i], a0, a1);
			double test = altn(n, a0, a1);
			altmax = MIN(altmax, test);
		}
		for(int i = n + 1; i < x[n]; i++){
			line(x[n], alt[x[n]], i, alt[i], a0, a1);
			double test = altn(n, a0, a1);
			altmin = MAX(altmin, test);
		}
		if(altmin > altmax){
			possible = false;
			n = -1;
		}
		else{
			if((altmin > -DBL_MAX) && (altmax < DBL_MAX))
				alt[n] = 0.5 * (altmin + altmax);
			else if((altmin == -DBL_MAX) && (altmax == DBL_MAX))
				alt[n] = 1.0;
			else if(altmin == -DBL_MAX)
				alt[n] = altmax - 1;
			else
				alt[n] = altmin + 1;
			// cout << n << ' ' << altmin << ' ' << altmax << ' ' << alt[n] << endl;
		}
	}
	if(possible){
		double min = DBL_MAX, max = -DBL_MAX;
		for(int n = 0; n < N; n++){
			min = MIN(min, alt[n]);
			max = MAX(max, alt[n]);
		}
		for(int n = 0; n < N; n++){
			if(max > min) out << long int (0.9e9 * (alt[n] - min) / (max - min)) << ' ';
			else out << 10 << ' ';
			// cout << long int(1e9 * alt[n]) << ' ';
			// out << alt[n] << ' ';
		}
		out << endl;
	}
	else{
		out << "Impossible" << endl;
	}
	delete[] alt;
	delete[] x;
}

int main(){
	int T; in >> T;
	for(int t = 1; t <= T; t++){
		cout << "Solving case #" << t << endl;
		out << "Case #" << t << ": ";
		solve();
	}
	return 0;
}
