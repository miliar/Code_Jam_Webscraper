// TikTakToeTomek.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "conio.h"
#include "malloc.h"

char ComChar = 'T';
void ReadInput(FILE* fileInput, char* input)
{
	for (int i=0; i<4;i++){
		fscanf_s(fileInput, "\n%c%c%c%c", &input[(4*i)+0],1,&input[(4*i)+1],1,&input[(4*i)+2],1, &input[(4*i)+3],1);
	}
}

typedef enum{
	NOT_WON = 0,
	WON = 1,
}ResultType;

int FindNoOfChaal(char* input, char c){
	int count = 0;
	for (int i=0; i<16;i++){
		if (c == input[i])
			count++;
	}
	return count;
}

int FindNoOfPlacesFilled(char* input){
	int count = 0;
	for (int i=0; i<16;i++){
		if ('.' != input[i])
			count++;
	}
	return count;
}

ResultType CheckRows(char* input, char checkChar){
	for (int i=0; i<4;i++){
		ResultType resultRow = WON;
		for (int j=0;j<4;j++){
			if ((input[i*4+j] != checkChar) && (input[i*4+j] != ComChar)){
				resultRow = NOT_WON;
				break;		
			}
		}
		if (resultRow == WON)
			return WON;
	}
	return NOT_WON;
}
ResultType CheckColumns(char* input, char checkChar){
	for (int j=0; j<4;j++){
		ResultType resultCol = WON;
		for (int i=0;i<4;i++){
			if ((input[i*4+j] != checkChar) && (input[i*4+j] != ComChar)){
				resultCol = NOT_WON;
				break;		
			}
		}
		if (resultCol == WON)
			return WON;
	}
	return NOT_WON;
}
ResultType CheckDiagonals(char* input, char checkChar){
	ResultType resultDiag = WON;
		
	for (int i=0;i<4;i++){
		if ((input[i*4+i] != checkChar) && (input[i*4+i] != ComChar)){
			resultDiag = NOT_WON;
			break;		
		}
	}
	if (resultDiag == WON)
		return WON;

	resultDiag = WON;
	for (int i=0;i<4;i++){
		if ((input[i*4+(4-i-1)] != checkChar) && (input[i*4+(4-i-1)] != ComChar)){
			resultDiag = NOT_WON;
			break;		
		}
	}
	if (resultDiag == WON)
		return WON;

	return NOT_WON;
}


int _tmain(int argc, _TCHAR* argv[])
{
	char* input=NULL;
	int NoOfTests = 0;

	FILE* fileInput = NULL;
	FILE* fileOutput = NULL;
	char fileName[300] = {0};

	sprintf_s(fileName, 300, "%S", argv[1]);
	fopen_s(&fileInput, fileName, "r");
	if (fileInput == NULL){
		fprintf(stderr, "%s FILE INPUT OPEN FAILED", fileName );
		return 0;
	}
	sprintf_s(fileName, 300, "%S", argv[2]);
	fopen_s(&fileOutput, fileName, "w");
	if (fileOutput == NULL){
		fprintf(stderr, "%s FILE OUTPUT OPEN FAILED", fileName);
		fclose(fileInput);
		return 0;
	}
	fscanf_s(fileInput, "\n%d", &NoOfTests);

	input = (char*)malloc(NoOfTests*16*sizeof(char));
	for (int i=0;i<NoOfTests;i++){
		ReadInput(fileInput, input + (16*i));
	}

	//fprintf(stderr,"NoOfTests=%d\n",NoOfTests);

	//for (int i=0;i<NoOfTests;i++){
	//	for (int j=0;j<4;j++){
	//		fprintf(stderr, "readinput = %c  %c  %c  %c \n", input[(16*i)+(4*j)+0], input[(16*i)+(4*j)+1], input[(16*i)+(4*j)+2], input[(16*i)+(4*j)+3]);
	//	}	
	//}	

	for (int i=0;i<NoOfTests;i++){
		int XCount = FindNoOfChaal(&input[16*i], 'X');
		int OCount = FindNoOfChaal(&input[16*i],'O');
		int NoOfPlacesFilled = FindNoOfPlacesFilled(&input[16*i]);
		//char FirstCheckChar = 0;
		//char SecondCheckChar = 0;

		//if (XCount>OCount)
		//{
		//	FirstCheckChar = 'O';
		//	SecondCheckChar = 'X';
		//}else{
		//	FirstCheckChar = 'X';
		//	SecondCheckChar = 'O';
		//}
		ResultType resultX_Rows;
		ResultType resultX_Cols;
		ResultType resultX_Diag;
		ResultType resultO_Rows;
		ResultType resultO_Cols;
		ResultType resultO_Diag;

		resultX_Rows = CheckRows(&input[16*i], 'X');
		resultX_Cols = CheckColumns(&input[16*i] , 'X');
		resultX_Diag = CheckDiagonals(&input[16*i], 'X');
		
		if ((resultX_Rows == WON) || (resultX_Cols == WON) || (resultX_Diag == WON) )
		{
			fprintf(fileOutput,"Case #%d: X won\n",i+1);
			continue;
		}
		resultO_Rows = CheckRows(&input[16*i], 'O');
		resultO_Cols = CheckColumns(&input[16*i], 'O');
		resultO_Diag = CheckDiagonals(&input[16*i], 'O');
		
		if ((resultO_Rows == WON) || (resultO_Cols == WON) || (resultO_Diag == WON) )
		{
			fprintf(fileOutput,"Case #%d: O won\n",i+1);
			continue;
		}

		if (NoOfPlacesFilled == 16){
			//game drawn
			fprintf(fileOutput,"Case #%d: Draw\n",i+1);
		}else{
			//game has not completed
			fprintf(fileOutput,"Case #%d: Game has not completed\n",i+1);
		}
	}

	fclose(fileInput);
	fclose(fileOutput);
	return 0;
}

