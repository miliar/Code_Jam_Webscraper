#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <vector>

using namespace std;

int  N = -1;
char *R_i;
int  *P_i;
bool *done_i;

int compute2() {
	vector<pair<char, char> > table;

	int  curPos_orangeRobot  = 1;
	int  curPos_blueRobot    = 1;

	char robotAllowedToPress = ' ';

	for (int i = 0; i < N; ) {
		if (robotAllowedToPress == ' ') {
			robotAllowedToPress = R_i[i];
		}

		int nextI = -1;
		if ((i + 1) < N) {
			int _nextI = i + 1;
			while (R_i[_nextI] == R_i[i] && _nextI < N)
				++_nextI;

			if (R_i[_nextI] != R_i[i]) {
				nextI = _nextI;
			}
		}

		char orange = 2;
		char blue   = 2;

		if (R_i[i] == 'O') {
			if (curPos_orangeRobot == P_i[i]) {
				if (robotAllowedToPress == 'O') {
					// press the damned button!
					robotAllowedToPress = ' ';
					orange = 3;
					++i;

					if (nextI != -1) {
						if (curPos_blueRobot < P_i[nextI]) {
							++curPos_blueRobot;
							blue = 0;
						} else if (curPos_blueRobot > P_i[nextI]) {
							--curPos_blueRobot;
							blue = 1;
						}
					}
				}
			} else if (curPos_orangeRobot < P_i[i]) {
				++curPos_orangeRobot;
				orange = 0;

				if (nextI != -1) {
					if (curPos_blueRobot < P_i[nextI]) {
						++curPos_blueRobot;
						blue = 0;
					} else if (curPos_blueRobot > P_i[nextI]) {
						--curPos_blueRobot;
						blue = 1;
					}
				}
			} else if (curPos_orangeRobot > P_i[i]) {
				--curPos_orangeRobot;
				orange = 1;

				if (nextI != -1) {
					if (curPos_blueRobot > P_i[nextI]) {
						--curPos_blueRobot;
						blue = 1;
					} else if (curPos_blueRobot < P_i[nextI]) {
						++curPos_blueRobot;
						blue = 0;
					}
				}
			}
		} else if (R_i[i] == 'B') {
			if (curPos_blueRobot == P_i[i]) {
				if (robotAllowedToPress == 'B') {
					// press the damned button!
					robotAllowedToPress = ' ';
					blue = 3;
					++i;

					if (nextI != -1) {
						if (curPos_orangeRobot < P_i[nextI]) {
							++curPos_orangeRobot;
							orange = 0;
						} else if (curPos_orangeRobot > P_i[nextI]) {
							--curPos_orangeRobot;
							orange = 1;
						}
					}
				}
			} else if (curPos_blueRobot < P_i[i]) {
				++curPos_blueRobot;
				blue = 0;

				if (nextI != -1) {
					if (curPos_orangeRobot < P_i[nextI]) {
						++curPos_orangeRobot;
						orange = 0;
					} else if (curPos_orangeRobot > P_i[nextI]) {
						--curPos_orangeRobot;
						orange = 1;
					}
				}
			} else if (curPos_blueRobot > P_i[i]) {
				--curPos_blueRobot;
				blue = 1;

				if (nextI != -1) {
					if (curPos_orangeRobot > P_i[nextI]) {
						--curPos_orangeRobot;
						orange = 1;
					} else if (curPos_orangeRobot < P_i[nextI]) {
						++curPos_orangeRobot;
						orange = 0;
					}
				}
			}
		}
		
		table.push_back(pair<char, char>(orange, blue));
	}

	/*
	for (int i = 0; i < table.size(); ++i) {
		char orange = table[i].first + 48;
		char blue   = table[i].second + 48;
		printf("%c %c\n", orange, blue);
	}
	printf("\n\n");*/

	int tableSize = table.size();
	table.erase(table.begin(), table.end());
	return tableSize;
}

int compute1() {
	int  time = 0;
	

	int  curPos_orangeRobot  = 1;
	int  curPos_blueRobot    = 1;

	char robotAllowedToPress = ' ';

	//for (int i = 0; i < N; ++i)
	//	done_i[i] = false;

	for (int i = 0; i < N; ) {
		if (robotAllowedToPress == ' ') {
			robotAllowedToPress = R_i[i];
		}

		if (R_i[i] == 'O') {
			if (curPos_orangeRobot == P_i[i]) {
				if (robotAllowedToPress == 'O') {
					// press the damned button!
					robotAllowedToPress = ' ';
					time += 1;
					++i;
				}
			} else if (curPos_orangeRobot < P_i[i]) {
				int steps = P_i[i] - curPos_orangeRobot;

				curPos_orangeRobot += steps;
				time               += steps;
			} else if (curPos_orangeRobot > P_i[i]) {
				int steps = curPos_orangeRobot - P_i[i];

				curPos_orangeRobot -= steps;
				time               += steps;
			}
		} else if (R_i[i] == 'B') {
			if (curPos_blueRobot == P_i[i]) {
				if (robotAllowedToPress == 'B') {
					// press the damned button!
					robotAllowedToPress = ' ';
					time += 1;
					++i;
				}
			} else if (curPos_blueRobot < P_i[i]) {
				int steps = P_i[i] - curPos_blueRobot;

				curPos_blueRobot += steps;
				time             += steps;
			} else if (curPos_blueRobot > P_i[i]) {
				int steps = curPos_blueRobot - P_i[i];

				curPos_blueRobot -= steps;
				time             += steps;
			}
		}
	}

	return time;
}

int main() {
	//FILE *fp = fopen("C:\\gcj\\Bot_Trust\\test", "r");
	//FILE *fp = fopen("C:\\gcj\\Bot_Trust\\small", "r");
	FILE *fp = fopen("C:\\gcj\\Bot_Trust\\big", "r");

	FILE *fp2 = fopen("C:\\gcj\\Bot_Trust\\output", "w");

	int T;
	fscanf(fp, "%d", &T);

	assert(T >= 1);
	assert(T <= 100);

	R_i    = (char *) malloc(100 * sizeof(char));
	P_i    = (int *)  malloc(100 * sizeof(int));
	done_i = (bool *) malloc(100 * sizeof(bool));

	for (int i = 0; i < T; ++i) {
		fscanf(fp, "%d", &N);

		assert(N >= 1);
		assert(N <= 100);

		for (int j = 0; j < N; ++j) {
			fscanf(fp, " %c ", &R_i[j]);
			fscanf(fp, "%d", &P_i[j]);

			//printf(" {%c %d} ", R_i[j], P_i[j]);

			assert(R_i[j] == 'O' || R_i[j] == 'B');

			assert(P_i[j] >= 1);
			assert(P_i[j] <= 100);
		}

		fprintf(fp2, "Case #%d: ", i + 1);

		//int ret = compute1();
		int ret = compute2();
		//printf("\n");
		fprintf(fp2, "%d", ret);

		fprintf(fp2, "\n");
	}

	free(R_i);
	free(P_i);
	free(done_i);

	fclose(fp);
	fclose(fp2);

	return 0;
}