#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <vector>

using namespace std;

int matchWord(map<char, void*> *nowMap, const vector<char> *possibleChar, const int whichChar, const int wordLength) {
	int totalNum = 0;
	size_t pSize = possibleChar[whichChar].size();
	size_t pNum;
	map<char, void*>::iterator mapIt;

	for (pNum = 0; pNum < pSize; pNum++) {
		mapIt = nowMap->find(possibleChar[whichChar][pNum]);
		if (mapIt != nowMap->end()) {
			if (whichChar == wordLength - 1) {
				totalNum++;
			}
			else {
				totalNum += matchWord((map<char, void*>*)mapIt->second, possibleChar, whichChar+1, wordLength);
			}
		}
	}

	return totalNum;
}


int main()
{
	FILE* code_file;
	FILE* outFile;
	int wordLength, wordNum, testNum;
	int i, j;
	char theWord[500];
	map<char, void*> dicMap;
	map<char, void*>::iterator mapIt;
	map<char, void*> *nowTraceMap, *nextTraceMap;
	vector<char> *possibleChar;
	int charPos;
	int totalNum;

	code_file = fopen("A-large.in", "r");
	outFile = fopen("outResult", "w");

	if (!code_file)
		exit(1);

	fscanf(code_file, "%d %d %d", &wordLength, &wordNum, &testNum);

	for (i = 0; i < wordNum; i++) {
		fscanf(code_file, "%s", theWord);
		nowTraceMap = &dicMap;
		for (j = 0; j < wordLength; j++) {
			mapIt = nowTraceMap->find(theWord[j]);
			if (mapIt == nowTraceMap->end()) {
				if (j < wordLength - 1) {
					nextTraceMap = new map<char, void*>;
					nowTraceMap->insert(pair<char, void*>(theWord[j], (void*)nextTraceMap));
					nowTraceMap = nextTraceMap;
				}
				else {
					nowTraceMap->insert(pair<char, void*>(theWord[j], NULL));
				}
			}
			else {
				nowTraceMap = (map<char, void*>*)mapIt->second;
			}
		}
	}

	possibleChar = new vector<char> [wordLength];
	for (i = 0; i < testNum; i++) {
		fscanf(code_file, "%s", theWord);
		charPos = 0;
		for (j = 0; j < wordLength; j++) {
			possibleChar[j].clear();
			if (theWord[charPos] == '(') {
				charPos++;
				while(theWord[charPos] != ')') {
					possibleChar[j].push_back(theWord[charPos++]);
				}
			}
			else {
				possibleChar[j].push_back(theWord[charPos]);
			}
			charPos++;
		}
		totalNum = matchWord(&dicMap, possibleChar, 0, wordLength);

		//printf("Case #%d: %d\n", i+1, totalNum);
		fprintf(outFile, "Case #%d: %d\n", i+1, totalNum);
	}

	delete [] possibleChar;
	
	fclose(code_file);
	fclose(outFile);

	//system("pause");

	return 0;
}