#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

char buffer[32];

int
main(int argc, char **argv)
{
	int numCases;
	scanf("%d", &numCases);

	for (int c = 0; c < numCases; c++) {
		int len;
		scanf("%d", &len);
		int lastPos1 = 1;
		int lastPos2 = 1;
		int lastMoveTime1 = 0;
		int lastMoveTime2 = 0;

		int moves = 0;
		for (int i = 0 ; i < len; i++) {
			int tmp;
			scanf("%s", buffer);
			scanf("%d", &tmp);
			if (buffer[0] == 'O') {
				int movesNeeded = abs(lastPos1 - tmp);
				movesNeeded = max(0, movesNeeded - (moves - lastMoveTime1)) + 1;
				moves += movesNeeded;
				lastMoveTime1 = moves;
				lastPos1 = tmp;
			} else {
				int movesNeeded = abs(lastPos2 - tmp);
				movesNeeded = max(0, movesNeeded - (moves - lastMoveTime2)) + 1;
				moves += movesNeeded;
				lastMoveTime2 = moves;
				lastPos2 = tmp;
			}
		}

		printf("Case #%d: %d\n", c+1, moves);
	}

	return 0;
}
