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

	//Open files
	FILE* fpInput = fopen(argv[1], "rb");
	FILE* fpOutput = fopen(argv[2], "wb");
	
	//Read variables
	fscanf(fpInput, "%d\n", &iT);
	for(int t=0;t<iT;t++) {
		fscanf(fpInput, "%d %d\n", &iH, &iW);
		pArea = (sSquare**) malloc(sizeof(sSquare*)*iH);
		for(int s=0;s<iH;s++)
			pArea[s] = (sSquare*) malloc(sizeof(sSquare)*iW);
				
		for(int h=0;h<iH;h++)
			for(int w=0;w<iW;w++) {
				pArea[h][w].Alt = getc(fpInput)-48;
				getc(fpInput);
			}

		for(int h=0;h<iH;h++)
			for(int w=0;w<iW;w++)
				SelectDrain(pArea, h, w, iH, iW);
		
		value = 96; 
		for(int h=0;h<iH;h++)
			for(int w=0;w<iW;w++)
				if(!pArea[h][w].parsed)
					Fill(pArea, h, w, iH, iW, ++value);

		fprintf(fpOutput, "Case #%d:\n", t+1);
		for(int h=0;h<iH;h++) {
			for(int w=0;w<iW;w++)
				fprintf(fpOutput, "%c ", pArea[h][w].Value);
			fprintf(fpOutput, "\n");
		}

		for(int s=0;s<iH;s++)
			free(pArea[s]);
		free(pArea);
	}
}