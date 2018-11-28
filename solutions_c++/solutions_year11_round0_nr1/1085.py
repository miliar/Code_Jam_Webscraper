#include <iostream>
#include <cstdio>

using namespace std;

#define ABS(X) ((X) < 0 ? -(X) : X)
#define MIN(X,Y) ((X) < (Y) ? (X) : (Y))
#define MAX(X,Y) ((X) > (Y) ? (X) : (Y))

#define DEBUG 0

int main () {
	int nCases, iCase = 0;
	cin >> nCases;

	while (iCase < nCases) {
		int nMoves, iMove, tot = 0;
		int curPos[2]; // 0 for 'B', 1 for 'O'
		char robot;
		int button;
		
		curPos[0] = 1;
		curPos[1] = 1;

		cin >> nMoves >> robot >> button;

		int isRobotO = (robot == 'O');
		int prevMoves;

		tot += button;
		prevMoves = button;
		curPos[isRobotO] = button;
		
		for (iMove = 1; iMove < nMoves; iMove++) {
			cin >> robot >> button;
			
			int isNewO = (robot == 'O');

			int change = isNewO ^ isRobotO;

			int numMoves = ABS (button - curPos[isNewO]);

			if (change) {
				numMoves = MAX (0, numMoves - prevMoves);

				isRobotO = isNewO;
				prevMoves = 0;
			}
			numMoves++; // pressing button

			tot += numMoves;
			prevMoves += numMoves;
			curPos[isNewO] = button;
			
			if (DEBUG) printf ("numMoves %d prev %d tot %d\n", numMoves, prevMoves, tot);
		}

		printf ("Case #%d: %d\n", ++iCase, tot);
	}

	return 0;
}
