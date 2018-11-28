// codeJam_Magicka.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <math.h>
#include <iostream>
using namespace std;

int numCombine, numOpposed, numChar;
char combine[40][5];
char opposed[30][5];
char invoke[105];
char result[105];

void inputRules();
void printResult(int, int);
int calculate();
char checkCombine(char, int);
int checkOpposed(char, int);

int _tmain(int argc, _TCHAR* argv[])
{
	int numTestCase;
	
	cin >> numTestCase;
	for (int i = 1; i <= numTestCase; ++i){
		inputRules();
		
		int num = calculate();

		printResult(i, num);
	}

	return 0;
}

char checkCombine(char curChar, int ptrResult){
	if (ptrResult == 0) return '0';
	for (int i = 0; i < numCombine; i++){
		if(combine[i][0] == curChar){
			if (result[ptrResult-1] == combine[i][1]) 
				return combine[i][2];
		}
		if(combine[i][1] == curChar){
			if (result[ptrResult-1] == combine[i][0]) 
				return combine[i][2];
		}
	}
	return '0';
}

int checkOpposed(char curChar, int ptrResult){
	if(ptrResult == 1) return ptrResult;
	for (int i = 0; i < numOpposed; i++){
		if(opposed[i][0] == curChar){
			for(int j = 0; j < ptrResult; j++){
				if (result[j] == opposed[i][1]) 
					return 0;
			}
		}
		if(opposed[i][1] == curChar){
			for(int j = 0; j < ptrResult; j++){
				if (result[j] == opposed[i][0]) 
					return 0;
			}
		}
	}
	return ptrResult;
}

int calculate(){
	int ptrResult = 0;

	for(int i = 0; i < numChar; i++){
		char cc = checkCombine(invoke[i], ptrResult);
		if (cc != '0'){
			result[ptrResult-1] = cc;
		}else{
			result[ptrResult] = invoke[i];
			ptrResult++;
			ptrResult = checkOpposed(invoke[i], ptrResult);
		}
	}
	return ptrResult;
}

void printResult(int i, int charNum){
	cout << "Case #" << i << ": [";
	for (int i = 0; i < charNum; i++){
		cout << result[i];
		if (i != charNum - 1) cout << ", ";
	}
	cout << "]" << endl;
}

void inputRules(){
	cin >> numCombine;
	for (int j = 0; j < numCombine; j++){
		cin >> combine[j];
	}
	cin >> numOpposed;
	for (int j = 0; j < numOpposed; j++){
		cin >> opposed[j];
	}
	cin >> numChar;
	for (int j = 0; j < numChar; j++){
		cin >> invoke[j];
	}
}
