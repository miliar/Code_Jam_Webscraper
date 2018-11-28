#include <iostream>
#include <cstdio>


using namespace std;

long long t, c, d, p[500], v[500];
long long min_i, max_i, sumv;
double wyn;
double wyn_max;

int main(int argc, char ** argv) {

	cin >> t;

	for (int i=0; i<t; ++i) {

		cin >> c;
		cin >> d;

		for (int j=0; j<c; ++j) {

			cin >> p[j];
			cin >> v[j];
		}

		wyn_max = 0.0;

		for (int l=c; l>=0; --l) {

			for (int k=0; k<l; ++k) {

				min_i = 2000000;
				max_i = -2000000;
				sumv = 0;

				for (int j=k; j<l; ++j) {
	
					sumv += v[j];
			
					if (p[j] > max_i) max_i = p[j];
					if (p[j] < min_i) min_i = p[j];
				}

				long long wyn_i;
				wyn_i = (sumv - 1) * d;
				wyn_i -= max_i - min_i;

				if (wyn_i > 0) {

					wyn = (long long)(wyn_i / 2);

					if (wyn_i % 2 == 1) wyn += 0.5;

					if (wyn > wyn_max) wyn_max = wyn;

				}
			}
		}

		printf("Case #%d: %.1lf\n", i + 1, wyn_max);
	}


	return 0;
}
