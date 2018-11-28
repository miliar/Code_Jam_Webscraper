#include <fstream>
#include <vector>
#include <math.h>
#include <stdlib.h>
#include <string>

using namespace std;

int main() {

	int T;
	int C, D, N;
	fstream f, g;

	f.open("magicka.in", fstream::in);
	g.open("magicka.out", fstream::out);

	f >> T;
	for (int t = 1; t <= T; t++) {
		int invoke[64][3];
		int reset[32][2];
		
		memset(invoke, 0, sizeof(invoke));
		memset(reset, 0, sizeof(reset));
		
		f >> C;
		for (int i = 0; i < C; i++) {
			string s;
			f >> s;
			invoke[i][0] = (int )(s[0] - 'A');
			invoke[i][1] = (int )(s[1] - 'A');
			invoke[i][2] = (int )(s[2] - 'A');
		}

		f >> D;
		for (int i = 0; i < D; i++) {
			string s;
			f >> s;
			reset[i][0] = (int )(s[0] - 'A');
			reset[i][1] = (int )(s[1] - 'A');
		}
		
		int list[1000];
		int index = -1;
		f >> N;
		char ch;
		int c, bit[30];
		memset(bit, 0, sizeof( bit));

		for (int i = 0; i < N; i++) {
			f >> ch;
			c = (int )(ch - 'A');
			bool usedInvocation = false;
			bool usedReset = false;

			if (index >= 0) {
				// Try to apply invocation
				for (int j = 0; j < C; j++) {
					if ((invoke[j][0] == c && invoke[j][1] == list[index]) || 
						(invoke[j][0] == list[index] && invoke[j][1] == c)) {
							usedInvocation = true;
							bit[list[index]]--;
							list[index] = invoke[j][2];
							bit[invoke[j][2]]++;
							break;
					}
				}

				if (usedInvocation == false) {
					// Try to apply reset
					for (int j = 0; j < D; j++) {
						if ((reset[j][0] == c && bit[reset[j][1]] > 0) ||
							(reset[j][1] == c && bit[reset[j][0]] > 0)) {
							memset(list, 0, sizeof(list));
							memset(bit, 0, sizeof(bit));
							index = -1;
							usedReset = true;
							break;
						}
					}
				}
			}
			if (usedReset == false && usedInvocation == false) {
				list[++index] = c;
				bit[c]++;
			}
		}

		g << "Case #" << t << ": [";
		if (index == -1) {
			g << "]" << endl;
		} else {
			g << (char ) (list[0] + 'A');
			for (int i = 1; i <= index; i++) {
				g << ", " << (char ) (list[i] + 'A');
			}
			g << "]" << endl;
		}
	}

	f.close();
	g.close();

	return 0;
}