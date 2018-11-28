#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int main(int argc, char* argv[]) {

	FILE* f = fopen("in.txt", "r");
	FILE* out = fopen("out.txt", "w");

	int testCases;
	fscanf(f, "%d", &testCases);

	for (int z = 0; z < testCases; z++) {
		int lineCount = 0;
		int lineStart[1000];
		int lineEnd[1000];

		fscanf(f, "%d", &lineCount);

		for (int i = 0; i < lineCount; i++) {
			fscanf(f, "%d", &lineStart[i]);
			fscanf(f, "%d", &lineEnd[i]);
			}

		int iCount = 0;
		for (int i = 0; i < lineCount; i++) {
	
			if (lineStart[i] == lineEnd[i]) continue;

			for (int j = 0; j < lineCount; j++) {
				if (i == j) continue;
				if (i > j) break;

				if (	(lineStart[i] > lineStart[j] && lineEnd[i] < lineEnd[j]) ||
						(lineStart[j] > lineStart[i] && lineEnd[j] < lineEnd[i]) 
					) {
					iCount ++;
					}
				}
			}

		cout << "Case #" << z+1 << ": " << iCount << endl;
		fprintf(out, "Case #%d: %d\n", z+1, iCount);
		}

	fclose(f);

	return 0;
	}
