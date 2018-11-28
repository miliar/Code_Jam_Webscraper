#include <iostream>
#include <fstream>
#define WON '1'
#define LOST '0'
#define NOT_PLAYED '.'
using namespace std;

int main (int argc, char * const argv[]) {
	ifstream input(argv[1]);
	ofstream output("output.txt");
	int T, N;
	input >> T;
	for (int i = 0; i < T; i++) {
		input >> N;
		char schedule[N][N];
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < N; k++) {
				input >> schedule[j][k];
			}
		}
		
		
		double WIP[N], OWP[N], OOWP[N], RPI[N];
		
		
		for (int j = 0; j < N; j++) {
			int wins = 0, loses = 0;
			for (int k = 0; k < N; k++) {
				if (j == k) {
					continue;
				}
				if (schedule[j][k] == WON) {
					wins++;
				} else if (schedule[j][k] == LOST) {
					loses++;
				}
			}
			WIP[j] = wins/(double)(wins+loses);
		}
		
		for (int j = 0; j < N; j++) {
			int counter = 0;
			double WPT[N];
			for (int k = 0; k < N; k++) {
				int wins = 0, loses = 0;
				if (j == k) {
					continue;
				}
				if (schedule[k][j] == NOT_PLAYED) {
					continue;
				}
				for (int s = 0; s < N; s++) {
					if (s == j) {
						continue;
					}
					if (schedule[k][s] == WON) {
						wins++;
					} else if (schedule[k][s] == LOST) {
						loses++;
					}
				}
				WPT[counter++] = wins/(double)(wins+loses);
			}
			double sum = 0;
			for (int k = 0; k < counter; k++) {
				sum+=WPT[k];
			}
			sum/=(double)counter;
			OWP[j] = sum;
		}
		
		for (int j = 0; j < N; j++) {
			double sum = 0;
			int c = 0;
			for (int k = 0; k < N; k++) {
				if (j == k) {
					continue;
				}
				if (schedule[j][k] != NOT_PLAYED) {
					sum+=OWP[k];
					c++;
				}
			}
			OOWP[j] = sum/(double)c;
		}
		output << "Case #" << i+1 << ":" << endl;
		output << showpoint;
		output.precision(12);
		for (int j = 0; j < N; j++) {
			RPI[j] = .25f*WIP[j]+.50f*OWP[j]+.25f*OOWP[j];
			output << RPI[j] << endl;
		}
	}
	return 0;
}