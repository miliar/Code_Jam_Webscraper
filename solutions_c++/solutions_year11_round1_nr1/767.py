#include <iostream>
#include <fstream>
using namespace std;

int main (int argc, char * const argv[]) {
	ifstream input(argv[1]);
	ofstream output("output.txt");
	int T, PD, PG;
	long long N;
	input >> T;
	for (int i = 0; i < T; i++) {
		input >> N >> PD >> PG;
		long long gamesWonToday = -1, gamesPlayedToday = -1;
		bool found = false;
		for (long long j = 1; j <= N && !found; j++) {
			for (long long k = 0; k <= j; k++) {
				if ((k*100/(float)j) == (float)PD) {
					gamesWonToday = k;
					gamesPlayedToday = j;
					found = true;
					break;
				}
			}
		}
		if ((gamesWonToday == -1 || gamesPlayedToday == -1)) {
			output << "Case #" << i+1 << ": Broken" << endl;
			continue;
		}
		if ((PG == 100 || PG == 0) && PG != PD) {
			output << "Case #" << i+1 << ": Broken" << endl;
			continue;
		}
		long long gamesPlayed = -1, gamesWon = -1;
		found = false;
		for (long long j = gamesPlayedToday; !found; j++) {
			for (long long k = 0; k <= j-gamesPlayedToday; k++) {
				if (((k+gamesWonToday)*100/(float)j) == (float)PG) {
					gamesWon = k;
					gamesPlayed = j;
					found = true;
					break;
				}
			}
		}
		if (gamesWon == -1 || gamesPlayed == -1) {
			output << "Case #" << i+1 << ": Broken" << endl;
			continue;
		}
		output << "Case #" << i+1 << ": Possible" << endl;
	}
	return 0;
}