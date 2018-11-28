#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int ncases;
	cin >> ncases;

	for (int caseno = 1; caseno <= ncases; caseno++) {
		int nrnds;
		cin >> nrnds;
		int mins[2000];
		int nteams = 1 << nrnds;
		for (int i = 0; i < nteams; i++)
			cin >> mins[i];
		int costs[2000];
		for (int i = 0; i < nteams - 1; i++)
			cin >> costs[i];

		int opt[12][2000];
		fill(opt[0], opt[12], 0);
		for (int k = 0; k < nteams / 2; k++) {
			int n = min(mins[2 * k], mins[2 * k + 1]);
			for (int o = n; o < 12; o++)
				opt[o][k] = 1000000000;
			opt[n][k] = costs[k];
		}

		for (int r = 1; r < nrnds; r++) {
			int ngames = nteams >> (r + 1);
			int st = 0;
			for (int i = 0; i < r; i++)
				st += nteams >> (i + 1);
			int pst = st - (nteams >> r);
			for (int k = 0; k < ngames; k++) {
				for (int m = 0; m < 12; m++) {
					opt[m][st + k] = opt[m + 1][pst + 2 * k] + opt[m + 1][pst + 2 * k + 1];
					opt[m][st + k] = min(opt[m][st + k],
							costs[st + k] + opt[m][pst + 2 * k] + opt[m][pst + 2 * k + 1]);
					opt[m][st + k] = min(opt[m][st + k], 1000000000);

				}
			}
		}

		cout << "Case #" << caseno << ": " << opt[0][nteams - 2] << endl;
	}
	return 0;
}
