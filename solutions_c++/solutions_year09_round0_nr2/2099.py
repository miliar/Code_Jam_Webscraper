#include <cstdio>
#include <cstdlib>
#include <cstring>

enum dirType {North, West, East, South};

struct theSpace {
	dirType toWhere;
	int altitude;
	bool isLabeled;
	char basinLabel;
};

char traceMap(const int i, const int j, int &nowLabelIndex, struct theSpace **inputMap, const int &mapHeight, const int &mapWidth) {
	char *labelStr = "abcdefghijklmnopqrstuvwxyz";
	int nAlt, wAlt, eAlt, sAlt;
	int next_i, next_j;

	if (!inputMap[i][j].isLabeled) {
		if (mapHeight > 1 || mapWidth > 1) {
			if (i > 0) 
				nAlt = inputMap[i-1][j].altitude;
			else
				nAlt = INT_MAX;
			if (i < mapHeight-1)
				sAlt = inputMap[i+1][j].altitude;
			else
				sAlt = INT_MAX;
			if (j > 0)
				wAlt = inputMap[i][j-1].altitude;
			else
				wAlt = INT_MAX;
			if (j < mapWidth-1)
				eAlt = inputMap[i][j+1].altitude;
			else
				eAlt = INT_MAX;

			if (nAlt <= wAlt && nAlt <= eAlt && nAlt <= sAlt) {
				next_i = i - 1;
				next_j = j;
			}
			else if (wAlt < nAlt && wAlt <= eAlt && wAlt <= sAlt) {
				next_i = i;
				next_j = j - 1;
			}
			else if (eAlt < nAlt && eAlt < wAlt && eAlt <= sAlt) {
				next_i = i;
				next_j = j + 1;			
			}
			else {
				next_i = i + 1;
				next_j = j;
			}
			
			if (inputMap[next_i][next_j].altitude < inputMap[i][j].altitude) {
				inputMap[i][j].basinLabel = traceMap(next_i, next_j, nowLabelIndex, inputMap, mapHeight, mapWidth);
				inputMap[i][j].isLabeled = true;
			}
			else {
				inputMap[i][j].basinLabel = labelStr[nowLabelIndex];
				inputMap[i][j].isLabeled = true;
				nowLabelIndex++;
			}
		}
		else {
			inputMap[i][j].basinLabel = 'a';
			inputMap[i][j].isLabeled = true;
			return 'a';
		}
	}

	return inputMap[i][j].basinLabel;
}


int main()
{
	FILE* code_file;
	FILE* outFile;
	int mapNum, mapHeight, mapWidth;
	struct theSpace **inputMap, **finalBasin;
	int i, j, rIndex, cIndex;
	int altitude;
	int nowLabelIndex = 0;

	code_file = fopen("B-large.in", "r");
	outFile = fopen("outResult", "w");

	if (!code_file)
		exit(1);

	fscanf(code_file, "%d", &mapNum);

	for (i = 0; i < mapNum; i++) {
		fscanf(code_file, "%d %d", &mapHeight, &mapWidth);
		inputMap = (struct theSpace**)malloc(mapHeight*sizeof(struct theSpace*));

		for (j = 0; j < mapHeight; j++) {
			inputMap[j] = (struct theSpace*)malloc(mapWidth*sizeof(struct theSpace));
		}
		for (rIndex = 0; rIndex < mapHeight; rIndex++) {
			for (cIndex = 0; cIndex < mapWidth; cIndex++) {
				fscanf(code_file, "%d", &altitude);
				inputMap[rIndex][cIndex].altitude = altitude;
				inputMap[rIndex][cIndex].isLabeled = false;
			}
		}
		for (rIndex = 0; rIndex < mapHeight; rIndex++) {
			for (cIndex = 0; cIndex < mapWidth; cIndex++) {
				traceMap(rIndex, cIndex, nowLabelIndex, inputMap, mapHeight, mapWidth);
			}
		}

		//printf("Case #%d:\n", i+1);
		fprintf(outFile, "Case #%d:\n", i+1);
		for (rIndex = 0; rIndex < mapHeight; rIndex++) {
			for (cIndex = 0; cIndex < mapWidth; cIndex++) {
				//printf("%c ", inputMap[rIndex][cIndex].basinLabel);
				fprintf(outFile, "%c ", inputMap[rIndex][cIndex].basinLabel);
			}
			//printf("\n");
			fprintf(outFile, "\n");
		}
	
		nowLabelIndex = 0;
		free(inputMap);
	}
	
	fclose(code_file);
	fclose(outFile);

	//system("pause");

	return 0;
}