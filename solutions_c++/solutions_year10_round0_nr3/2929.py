#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int T, t, R, r, k, p, N, n;
	long long groups[1001][3];
	int loop, runs_left, loops_left;
	long long euro, loop_euro, total_passengers;

	ifstream myfile ("input.in");
	ofstream output ("output.txt", ios::trunc);
	myfile >> T;

	for (t=1;t<=T;t++) {
		myfile >> R >> k >> N;
		total_passengers = 0;
		for (n=1;n<=N;n++) {
			myfile >> groups[n][0];
			total_passengers=total_passengers+groups[n][0];
			groups[n][1] = 0;
			groups[n][2] = 0;
		}

		if (total_passengers>k) {
			euro = 0;
			r = 1;
			n = 1;
			do {
				groups[n][1] = r;
				groups[n][2] = euro;
				p=0;
				do {
					p=p+groups[n][0];
					n++;
					if (n>N) n=1;
				} while (p+groups[n][0] <= k);
				euro = euro + p;
				r++;
			} while ((groups[n][1]==0) && (r<=R));

			if (r<=R){
				loop = r - groups[n][1];
				loop_euro = euro - groups[n][2];
				runs_left = R - r + 1;
				loops_left = runs_left / loop;
				euro = euro + (loops_left * loop_euro);
				r = r + (loops_left * loop);
			}

			if (r<=R) {
				do {
					p=0;
					do {
						p=p+groups[n][0];
						n++;
						if (n>N) n=1;
					} while (p+groups[n][0] <= k);
					euro = euro + p;
					r++;
				} while (r<=R);
			}
		}
		else euro = R * total_passengers;
		cout << "Case #" << t << ": " << euro << "\n";
		output << "Case #" << t << ": " << euro << "\n";
	}
}


