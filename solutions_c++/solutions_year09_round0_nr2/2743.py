#include <windows.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

struct sSquare
{
	int Alt;
	int Drain;
	char Value;
	bool parsed;
};

//Drain:
//None:		0
//North:	1
//West:		2
//South:	3
//East:		4

void SelectDrain(sSquare** pArea, int h, int w, int iH, int iW)
{
	int iMin = pArea[h][w].Alt;
	pArea[h][w].Drain = 0;
	pArea[h][w].parsed = false;

	if(h>0 && pArea[h-1][w].Alt < iMin) {
		iMin = pArea[h-1][w].Alt;
		pArea[h][w].Drain = 1;
	}
	if(w>0 && pArea[h][w-1].Alt < iMin) {
		iMin = pArea[h][w-1].Alt;
		pArea[h][w].Drain = 2;
	}
	if(w<(iW-1) && pArea[h][w+1].Alt < iMin) {
		iMin = pArea[h][w+1].Alt;
		pArea[h][w].Drain = 4;
	}
	if(h<(iH-1) && pArea[h+1][w].Alt < iMin) {
		iMin = pArea[h+1][w].Alt;
		pArea[h][w].Drain = 3;
	}

}

void Fill(sSquare** pArea, int h, int w, int iH, int iW, char Value)
{
	pArea[h][w].Value = Value;
	pArea[h][w].parsed = true;

	if(h>0 && !pArea[h-1][w].parsed && pArea[h-1][w].Drain == 3)
		Fill(pArea, h-1, w, iH, iW, Value);
	if(w>0 && !pArea[h][w-1].parsed && pArea[h][w-1].Drain == 4)
		Fill(pArea, h, w-1, iH, iW, Value);
	if(h<(iH-1) && !pArea[h+1][w].parsed && pArea[h+1][w].Drain == 1)
		Fill(pArea, h+1, w, iH, iW, Value);
	if(w<(iW-1) && !pArea[h][w+1].parsed && pArea[h][w+1].Drain == 2)
		Fill(pArea, h, w+1, iH, iW, Value);
	
	switch(pArea[h][w].Drain)
	{
	case 1:
		if(!pArea[h-1][w].parsed)
			Fill(pArea, h-1, w, iH, iW, Value);
		break;
	case 2:
		if(!pArea[h][w-1].parsed)
			Fill(pArea, h, w-1, iH, iW, Value);
		break;
	case 3:
		if(!pArea[h+1][w].parsed)
			Fill(pArea, h+1, w, iH, iW, Value);
		break;
	case 4:
		if(!pArea[h][w+1].parsed)
			Fill(pArea, h, w+1, iH, iW, Value);
		break;
	}
}

void main(int argc, char* argv[])
{
	int iT, iH, iW;
	sSquare** pArea;
	char value;
	char* input, *sInput;
	char* output, *sOutput;
	DWORD dwLength;
	char tmp[3];
	tmp[0] = ' ';
	tmp[1] = '\n';
	tmp[2] = '\0';

	//Open files
	HANDLE hFile=CreateFile(argv[1], GENERIC_READ, FILE_SHARE_READ, NULL, 
		OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
	if(hFile != INVALID_HANDLE_VALUE) {
		sInput = (char*) malloc(GetFileSize(hFile, NULL));
		sOutput = (char*) malloc(GetFileSize(hFile, NULL));
		ReadFile(hFile, sInput, GetFileSize(hFile, NULL), &dwLength, NULL);
		CloseHandle(hFile);
	}


	
	input = sInput;
	output = sOutput;

	//Read variables
	sscanf(input, "%d\n", &iT);
	input=strchr(input, '\n')+1; 
	for(int t=0;t<iT;t++) {
		sscanf(input, "%d %d\n", &iH, &iW);
		input=strchr(input, '\n')+1; 
		pArea = (sSquare**) malloc(sizeof(sSquare*)*iH);
		for(int s=0;s<iH;s++)
			pArea[s] = (sSquare*) malloc(sizeof(sSquare)*iW);

		for(int h=0;h<iH;h++)
			for(int w=0;w<iW;w++) {
				sscanf(input, "%d", &pArea[h][w].Alt);
				input+=strcspn(input, tmp)+1;
			}

		for(int h=0;h<iH;h++)
			for(int w=0;w<iW;w++)
				SelectDrain(pArea, h, w, iH, iW);
		
		value = 96; 
		for(int h=0;h<iH;h++)
			for(int w=0;w<iW;w++)
				if(!pArea[h][w].parsed)
					Fill(pArea, h, w, iH, iW, ++value);

		sprintf(output, "Case #%d:\n", t+1);
		output = strchr(output, '\n')+1;
		for(int h=0;h<iH;h++) {
			for(int w=0;w<iW;w++) {
				sprintf(output, "%c ", pArea[h][w].Value);
				output+=2;
			}
			sprintf(output, "\n");
			output++;
		}

		//for(int s=0;s<iH;s++)
		//	free(pArea[s]);
		//free(pArea);
	}

	free(sInput);

	hFile=CreateFile(argv[2], GENERIC_WRITE, FILE_SHARE_WRITE, NULL, 
		OPEN_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
	if(hFile != INVALID_HANDLE_VALUE) {
		WriteFile(hFile, sOutput, (DWORD) strlen(sOutput), &dwLength, NULL) ? true : false;
		CloseHandle(hFile);
	}
}