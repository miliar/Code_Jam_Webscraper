#include <stdio.h>
#include <vector>

using namespace std;

vector<int> adjList[105][105];

int height, width;
int grid[105][105];
bool sink[105][105];

int dfsnum[105][105];
int dfsCount;

char curChar;
char dfsCountToChar[105];

void
dfs(int j, int k)
{
	if (dfsnum[j][k] >= 0) {
		return;
	}
	dfsnum[j][k] = dfsCount;
	for (unsigned int i = 0; i < adjList[j][k].size(); i++) {
		dfs(adjList[j][k][i] / (width + 1), adjList[j][k][i] % (width + 1));
	}
}

int
main(int argc, char **argv)
{
	int numCases;
	scanf("%d", &numCases);

	for (int i = 0; i < numCases; i++) {
		printf("Case #%d:\n", i + 1);
		scanf("%d%d", &height, &width);

		for (int j = 1; j <= height; j++) {
			grid[j][0] = 10005;
			grid[j][width + 1] = 10005;

			for (int k = 1; k <= width; k++) {
				dfsnum[j][k] = -1;
				grid[0][k] = 10005;
				grid[height + 1][k] = 10005;
				adjList[j][k].clear();
				sink[j][k] = false;
				scanf("%d", &grid[j][k]);
			}
		}

		for (int j = 1; j <= height; j++) {
			for (int k = 1; k <= width; k++) {
				int lowest = grid[j][k];
				int bestGridPoint = j * width + k;

				if (grid[j - 1][k] < lowest) {
					lowest = grid[j - 1][k];
					bestGridPoint = (j - 1) * (width + 1) + k;
				}
				if (grid[j][k - 1] < lowest) {
					lowest = grid[j][k - 1];
					bestGridPoint = (j) * (width + 1) + k - 1;
				}
				if (grid[j][k + 1] < lowest) {
					lowest = grid[j][k + 1];
					bestGridPoint = (j) * (width + 1) + k + 1;
				}
				if (grid[j + 1][k] < lowest) {
					lowest = grid[j + 1][k];
					bestGridPoint = (j + 1) * (width + 1) + k;
				}

				if (lowest == grid[j][k]) {
					sink[j][k] = true;
				} else {
					adjList[bestGridPoint / (width + 1)][bestGridPoint % (width + 1)].push_back(j * (width + 1) + k);
				}
			}
		}
		dfsCount = 0;
		for (int j = 1; j <= height; j++) {
			for (int k = 1; k <= width; k++) {
				if (sink[j][k]) {
					dfs(j, k);
					dfsCount++;
				}
			}
		}
		for (int i = 0; i < dfsCount; i++) {
			dfsCountToChar[i] = 0;
		}
		curChar = 'a';

		for (int j = 1; j <= height; j++) {
			for (int k = 1; k <= width; k++) {
				if (k != 1) {
					putchar(' ');
				}
				if (dfsCountToChar[dfsnum[j][k]] <= 0) {
					dfsCountToChar[dfsnum[j][k]] = curChar;
					curChar++;
				}
				putchar(dfsCountToChar[dfsnum[j][k]]);
			}
			puts("");
		}



	}

	return 0;
}
