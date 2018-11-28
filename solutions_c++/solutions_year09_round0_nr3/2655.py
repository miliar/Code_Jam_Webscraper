#include <windows.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>


long int SearchForString(char* input, char* pattern)
{
	long int result = 0;
	char* pos = input;
	if(pattern[0] == '\0') return 1;
	while((pos = strchr(pos, pattern[0])) != NULL) {
		result += SearchForString(++pos, pattern+1);
	}
	return result;
}

void main(int argc, char* argv[])
{
	int iN;
	char* input, *sInput;
	char* output, *sOutput;
	char* sLine, *s;
	DWORD dwLength;
	long int dNum = 0;;
	char pattern[21] = "welcome to code jam\0";

	//Open files
	HANDLE hFile=CreateFile(argv[1], GENERIC_READ, FILE_SHARE_READ, NULL, 
		OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
	if(hFile != INVALID_HANDLE_VALUE) {
		sInput = (char*) malloc(GetFileSize(hFile, NULL));
		ReadFile(hFile, sInput, GetFileSize(hFile, NULL), &dwLength, NULL);
		CloseHandle(hFile);
	}

	sOutput = (char*) malloc(2048*sizeof(char));
	input = sInput;
	output = sOutput;

	//Read variables
	sscanf(input, "%d\n", &iN);
	input=strchr(input, '\n')+1; 

	sLine = (char*) malloc(510*sizeof(char));
	for(int n = 0;n<iN;n++)
	{
		sscanf(input, "%[^\n]", sLine); 
		input=strchr(input, '\n')+1;
		if((s = strrchr(sLine, 'm'))!=NULL) {
			s[1] = '\0';
			dNum = SearchForString(sLine, pattern);
		}
		else
			dNum = 0;

		sprintf(output, "Case #%d: %04d\n", n+1, (dNum%10000));
		output=strchr(output, '\n')+1;
	}
	
	free(sInput);

	hFile=CreateFile(argv[2], GENERIC_WRITE, FILE_SHARE_WRITE, NULL, 
		OPEN_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
	if(hFile != INVALID_HANDLE_VALUE) {
		WriteFile(hFile, sOutput, (DWORD) strlen(sOutput), &dwLength, NULL) ? true : false;
		CloseHandle(hFile);
	}
}
