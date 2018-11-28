#include <iostream>
#include <vector>
#include <set>
#include <fstream>
using namespace std;

void main () {
	ifstream f ("input.txt");
	FILE* of;
	of = fopen("output.txt", "w+");
	//ofstream of ("output.txt");
	int T = 0;
	f >> T;
	for (int tc = 0; tc < T; ++tc) {
		int L = 0, N = 0, C = 0;
		double t;
		f >> L >> t >> N >> C;

		
		vector<int> a (N,0.0);
		for (int i = 0; i < C; ++i) {
			f >> a[i];
		}
		for (int i = C; i < N; ++i) {
			a[i] = a[i%C];
		}
		
		double res_time = 0.0;
		set<int> builded;
		vector<double> res (N, 0.0);
		if (L == 0) {
			for (int i = 0; i < N; ++i)
				res_time += a[i]*2.0;
		} else {
			builded.clear();
			for (int ll = 1; ll <= L; ++ll) {
				for (int i = 0; i < N; ++i)
					res[i] = 0.0;
				//i - position for new booster
				for (int i = 0; i < N; ++i) {
					if (builded.find(i) != builded.end()) continue;

					double time = 0.0;
					for (int j = 0; j < N; ++j) {
						if (j != i && builded.find(j) == builded.end()) {
							time += a[j]*2.0;
						} else {
							if (time + a[j]*2.0 < t) {
								time += a[j]*2.0;
							} else {
								if (time >= t) {
									time += a[j];
								} else {
									double remtime = t - time;
									time += remtime + (a[j]*2.0 - remtime)/2.0;
								}
							}
						}
					}
					res[i] = time;
				}
					
				double mintime = res[0];
				int minind = 0;
				for (int i = 1; i < N; ++i) {
					if (mintime == 0.0 || (mintime > res[i] && res[i] != 0.0)) {
						minind = i;
						mintime = res[i];
					}
				}
				builded.insert(minind);
				if (ll == L)
					res_time = mintime;
			}
		}

		printf ("Case #%u: %.0f\n", tc+1, res_time);
		fprintf (of, "Case #%u: %.0f\n", tc+1, res_time);
	}
	f.close();
	fclose(of);
	cin.get();
}