#include <fstream>
#include <vector>
#include <math.h>

using namespace std;

int main() {

	int T, N;
	fstream f, g;
	
	char robot; 
	int button;
	
	int blueGain, blueCurrent;
	int orangeGain, orangeCurrent;
	int total; 

	f.open("robots.in", fstream::in);
	g.open("robots.out", fstream::out);
	
	f >> T;
	for (int t = 1; t <= T; t++) {
		f >> N;

		blueGain = orangeGain = 0;
		orangeCurrent = blueCurrent = 1;
		total = 0;
		for (int l = 0; l < N; l++) {
			f >> robot >> button;
			if (robot == 'O') {
				if (orangeGain > abs(button - orangeCurrent)) {
					total += 1;
					blueGain += 1;
				} else {
					total += abs(button - orangeCurrent) + 1 - orangeGain;
					blueGain += abs(button - orangeCurrent) + 1 - orangeGain;
				}
				orangeCurrent = button;
				orangeGain = 0;
			} else {
				if (blueGain > abs(button - blueCurrent)) {
					total += 1;
					orangeGain += 1;
				} else {
					total += abs(button - blueCurrent) + 1 - blueGain;
					orangeGain += abs(button - blueCurrent) + 1 - blueGain;
				}
				blueCurrent = button;
				blueGain = 0;
			}
		}
		g << "Case #" << t << ": " << total << endl; 
	}
		
	f.close();
	g.close();
	return 0;
}