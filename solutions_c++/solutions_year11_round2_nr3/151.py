#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> room[8];
int roomCount;

void
split(int from, int to) {
	int oldCount = roomCount;
	for (int i = 0; i < oldCount; i++) {
		for (int j = 0; j < (signed) room[i].size(); j++) {
			int curNode = room[i][j];
			if (curNode == from) {
				vector<int> newRoom;
				int foundTo = -1;
				for (int k = j; k < (signed) room[i].size() * 2; k++) {
					int nextRoom = room[i][k % (signed) room[i].size()];
					newRoom.push_back(nextRoom);
					if (nextRoom == to) {
						foundTo = k;
						break;
					}
				}
				if (foundTo == -1 || newRoom.size() == room[i].size()) {
					break;
				}
				room[roomCount] = newRoom;
				roomCount++;

				newRoom.clear();
				for (int k = foundTo; k < (signed) room[i].size() * 3; k++) {
					int nextRoom = room[i][k % (signed) room[i].size()];
					newRoom.push_back(nextRoom);
					if (nextRoom == from) {
						break;
					}
				}
				room[i] = newRoom;
				break;
			}
		}
	}
}

vector<int> froms, tos;
int colors[8];
int numNodes, numWalls;
bool used[8];

bool
check(int numC)
{
	bool poss = true;
	for (int i = 0; poss && i < roomCount; i++) {
		for (int j = 0; j < numC; j++) {
			used[j] = false;
		}
		for (int j = 0; j < (signed) room[i].size(); j++) {
			used[colors[room[i][j]]] = true;
		}
		for (int j = 0; j < numC; j++) {
			if (!used[j]) {
				poss = false;
				break;
			}
		}

	}
	return poss;
}

bool
tryToColor(int numC)
{
	int max = numC;
	for (int i = 1; i < numNodes; i++) {
		max *= numC;
	}

	for (int i = 0; i < max; i++) {
		int foo = i;
		for (int j = 0; j < numNodes; j++) {
			colors[j] = foo % numC;
			foo /= numC;
		}
		if (check(numC)) {
			printf("%d\n%d", numC, 1 + colors[0]);
			for (int i = 1; i < numNodes; i++) {
				printf(" %d", 1 + colors[i]);
			}
			puts("");
			return true;
		}
	}

	return false;
}

int
main(int argc, char **argv)
{
	int numCases;
	scanf("%d", &numCases);

	for (int c = 1; c <= numCases; c++) {
		scanf("%d%d", &numNodes, &numWalls);

		roomCount = 1;
		for (int i = 0; i < numNodes; i++) {
			room[i].clear();
		}
		for (int i = 0; i < numNodes; i++) {
			room[0].push_back(i);
		}

		froms.clear();
		tos.clear();
		for (int i = 0; i < numWalls; i++) {
			int from;
			scanf("%d", &from);
			from--;
			froms.push_back(from);
		}
		for (int i = 0; i < numWalls; i++) {
			int from;
			scanf("%d", &from);
			from--;
			tos.push_back(from);
		}
		for (int i = 0; i < numWalls; i++) {
			split(froms[i],tos[i]);
		}

		int maxC = numNodes;
		for (int i = 0; i < roomCount; i++) {
			maxC = min(maxC, (signed) room[i].size());
		}

		printf("Case #%d: ", c);
		bool solved = false;
		while (maxC > 1) {
			if (tryToColor(maxC)) {
				solved = true;
				break;
			}
			maxC--;
		}
		if (!solved) {
			printf("1\n1");
			for (int i = 1; i < numNodes; i++) {
				printf(" 1");
			}
			puts("");
		}



	}

	return 0;
}
