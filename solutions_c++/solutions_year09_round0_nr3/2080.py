#include <cstdio>
#include <cstdlib>
#include <cstring>


unsigned long GetNum(int charIndex, int pos, char* strBuf, char* ansStr) {
	bool findTheChar = false;
	unsigned long totalNum = 0;
	int lengthOfStr = strlen(strBuf);

	if (charIndex != 18) {
		while (19-charIndex <= lengthOfStr-pos) {
			findTheChar = false;
			while (!findTheChar && (19-charIndex <= lengthOfStr-pos)) {
				if (ansStr[charIndex] == strBuf[pos++])
					findTheChar = true;
			}
			if (findTheChar) {
				totalNum += GetNum(charIndex+1, pos, strBuf, ansStr);
			}
		}
	}
	else {
		while (pos < lengthOfStr) {
			if (ansStr[charIndex] == strBuf[pos++])
				totalNum++;
		}
	}

	return totalNum;
}



int main()
{
	FILE* code_file;
	FILE* outFile;
	char lineNumBuf[10];
	char strBuf[50];
	char *ansStr = "welcome to code jam";
	int lineNum;
	unsigned long totalNum = 0;

	code_file = fopen("C-small-attempt2.in", "r");
	outFile = fopen("outResult", "w");

	if (!code_file)
		exit(1);

	fgets(lineNumBuf, 10, code_file);
	lineNum = atoi(lineNumBuf);
	

	for (int i = 0; i < lineNum; i++) {
		fgets(strBuf, 500, code_file);
		totalNum = GetNum(0, 0, strBuf, ansStr);
		totalNum %= 10000;
		printf("Case #%d: %04lu\n", i+1, totalNum);
		fprintf(outFile, "Case #%d: %04lu\n", i+1, totalNum);
	}
	
	fclose(code_file);
	fclose(outFile);

	return 0;
}