// GoogleTest.cpp : Defines the entry point for the console application.
//

#include <SDKDDKVer.h>
#include <stdio.h>
#include <tchar.h>
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	//////////////////////////////////////////////////////////////////////////
	// Check input
	if (argc <= 1) { return 1; }

	// Get input file path
	string sPath = argv[1];

	// Variable to store number of cases
	int nCases = 0;
	int nLinesPerTest = 4;

	// Read file
	string sLine;
	ifstream fInput(sPath);

	// Validate file
	if (!fInput.is_open()) { return 1; }

	// Read number of cases
	if (fInput.good()) {
		getline(fInput, sLine);
		stringstream(sLine) >> nCases;
	}

	// Validate input before dynamic allocation
	if (nCases < 1) { return 1; }

	// Declare array for input and output
	string* pstrInput = new string [nCases*nLinesPerTest];
	string* pstrOutput = new string [nCases];

	// Read input
	int nLine = 0;
	string sTmp;
	for (int nCase = 1; nCase <= nCases; nCase++) {
		nLine = 0;
		while ((fInput.good()) && nLine < nLinesPerTest) {
			getline(fInput, pstrInput[((nCase-1)*nLinesPerTest)+nLine]);
			nLine++;
		}
		// empty line
		getline(fInput, sTmp);
	}
	//////////////////////////////////////////////////////////////////////////

	// Solve problem
	string sStatus;
	for (int nCase = 1; nCase <= nCases; nCase++) {
		sStatus = "";
		// X won
		if (sStatus == "") {
			for (int nLine = 0; nLine < nLinesPerTest; nLine++) {
				if (
					(pstrInput[((nCase-1)*nLinesPerTest)+nLine][0] == 'X' || pstrInput[((nCase-1)*nLinesPerTest)+nLine][0] == 'T') &&
					(pstrInput[((nCase-1)*nLinesPerTest)+nLine][1] == 'X' || pstrInput[((nCase-1)*nLinesPerTest)+nLine][1] == 'T') &&
					(pstrInput[((nCase-1)*nLinesPerTest)+nLine][2] == 'X' || pstrInput[((nCase-1)*nLinesPerTest)+nLine][2] == 'T') &&
					(pstrInput[((nCase-1)*nLinesPerTest)+nLine][3] == 'X' || pstrInput[((nCase-1)*nLinesPerTest)+nLine][3] == 'T')
					)
				{
					sStatus = "X won";
					break;
				}
				if (
					(pstrInput[((nCase-1)*nLinesPerTest)+0][nLine] == 'X' || pstrInput[((nCase-1)*nLinesPerTest)+0][nLine] == 'T') &&
					(pstrInput[((nCase-1)*nLinesPerTest)+1][nLine] == 'X' || pstrInput[((nCase-1)*nLinesPerTest)+1][nLine] == 'T') &&
					(pstrInput[((nCase-1)*nLinesPerTest)+2][nLine] == 'X' || pstrInput[((nCase-1)*nLinesPerTest)+2][nLine] == 'T') &&
					(pstrInput[((nCase-1)*nLinesPerTest)+3][nLine] == 'X' || pstrInput[((nCase-1)*nLinesPerTest)+3][nLine] == 'T')
					)
				{
					sStatus = "X won";
					break;
				}
				if (
					(pstrInput[((nCase-1)*nLinesPerTest)+nLine][0] == 'O' || pstrInput[((nCase-1)*nLinesPerTest)+nLine][0] == 'T') &&
					(pstrInput[((nCase-1)*nLinesPerTest)+nLine][1] == 'O' || pstrInput[((nCase-1)*nLinesPerTest)+nLine][1] == 'T') &&
					(pstrInput[((nCase-1)*nLinesPerTest)+nLine][2] == 'O' || pstrInput[((nCase-1)*nLinesPerTest)+nLine][2] == 'T') &&
					(pstrInput[((nCase-1)*nLinesPerTest)+nLine][3] == 'O' || pstrInput[((nCase-1)*nLinesPerTest)+nLine][3] == 'T')
					)
				{
					sStatus = "O won";
					break;
				}
				if (
					(pstrInput[((nCase-1)*nLinesPerTest)+0][nLine] == 'O' || pstrInput[((nCase-1)*nLinesPerTest)+0][nLine] == 'T') &&
					(pstrInput[((nCase-1)*nLinesPerTest)+1][nLine] == 'O' || pstrInput[((nCase-1)*nLinesPerTest)+1][nLine] == 'T') &&
					(pstrInput[((nCase-1)*nLinesPerTest)+2][nLine] == 'O' || pstrInput[((nCase-1)*nLinesPerTest)+2][nLine] == 'T') &&
					(pstrInput[((nCase-1)*nLinesPerTest)+3][nLine] == 'O' || pstrInput[((nCase-1)*nLinesPerTest)+3][nLine] == 'T')
					)
				{
					sStatus = "O won";
					break;
				}
			}
			if (sStatus == "") {
				if (
					(pstrInput[((nCase-1)*nLinesPerTest)+0][0] == 'X' || pstrInput[((nCase-1)*nLinesPerTest)+0][0] == 'T') &&
					(pstrInput[((nCase-1)*nLinesPerTest)+1][1] == 'X' || pstrInput[((nCase-1)*nLinesPerTest)+1][1] == 'T') &&
					(pstrInput[((nCase-1)*nLinesPerTest)+2][2] == 'X' || pstrInput[((nCase-1)*nLinesPerTest)+2][2] == 'T') &&
					(pstrInput[((nCase-1)*nLinesPerTest)+3][3] == 'X' || pstrInput[((nCase-1)*nLinesPerTest)+3][3] == 'T')
					)
				{
					sStatus = "X won";
				}
			}
			if (sStatus == "") {
				if (
					(pstrInput[((nCase-1)*nLinesPerTest)+0][3] == 'X' || pstrInput[((nCase-1)*nLinesPerTest)+0][3] == 'T') &&
					(pstrInput[((nCase-1)*nLinesPerTest)+1][2] == 'X' || pstrInput[((nCase-1)*nLinesPerTest)+1][2] == 'T') &&
					(pstrInput[((nCase-1)*nLinesPerTest)+2][1] == 'X' || pstrInput[((nCase-1)*nLinesPerTest)+2][1] == 'T') &&
					(pstrInput[((nCase-1)*nLinesPerTest)+3][0] == 'X' || pstrInput[((nCase-1)*nLinesPerTest)+3][0] == 'T')
					)
				{
					sStatus = "X won";
				}
			}
			if (sStatus == "") {
				if (
					(pstrInput[((nCase-1)*nLinesPerTest)+0][0] == 'O' || pstrInput[((nCase-1)*nLinesPerTest)+0][0] == 'T') &&
					(pstrInput[((nCase-1)*nLinesPerTest)+1][1] == 'O' || pstrInput[((nCase-1)*nLinesPerTest)+1][1] == 'T') &&
					(pstrInput[((nCase-1)*nLinesPerTest)+2][2] == 'O' || pstrInput[((nCase-1)*nLinesPerTest)+2][2] == 'T') &&
					(pstrInput[((nCase-1)*nLinesPerTest)+3][3] == 'O' || pstrInput[((nCase-1)*nLinesPerTest)+3][3] == 'T')
					)
				{
					sStatus = "O won";
				}
			}
			if (sStatus == "") {
				if (
					(pstrInput[((nCase-1)*nLinesPerTest)+0][3] == 'O' || pstrInput[((nCase-1)*nLinesPerTest)+0][3] == 'T') &&
					(pstrInput[((nCase-1)*nLinesPerTest)+1][2] == 'O' || pstrInput[((nCase-1)*nLinesPerTest)+1][2] == 'T') &&
					(pstrInput[((nCase-1)*nLinesPerTest)+2][1] == 'O' || pstrInput[((nCase-1)*nLinesPerTest)+2][1] == 'T') &&
					(pstrInput[((nCase-1)*nLinesPerTest)+3][0] == 'O' || pstrInput[((nCase-1)*nLinesPerTest)+3][0] == 'T')
					)
				{
					sStatus = "O won";
				}
			}
		}
		// Game has not completed
		if (sStatus == "") {
			for (int nLine = 0; nLine < nLinesPerTest; nLine++) {
				if (
					(pstrInput[((nCase-1)*nLinesPerTest)+nLine][0] == '.') ||
					(pstrInput[((nCase-1)*nLinesPerTest)+nLine][1] == '.') ||
					(pstrInput[((nCase-1)*nLinesPerTest)+nLine][2] == '.') ||
					(pstrInput[((nCase-1)*nLinesPerTest)+nLine][3] == '.')
					)
				{
					sStatus = "Game has not completed";
					break;
				}
			}
		}
		// Draw
		if (sStatus == "") {
			sStatus = "Draw";
		}
		// Set status
		pstrOutput[nCase-1] = sStatus;
	}

	//////////////////////////////////////////////////////////////////////////
	// File output
	ofstream fOutput;
	fOutput.open(sPath+".out", ios::out|ios::trunc);
	for (int nCase = 1; nCase <= nCases; nCase++) {
		fOutput << "Case #" << nCase << ": " << pstrOutput[nCase-1] << "\n";
	}
	fOutput.close();

	// Release memory
	delete [] pstrInput;
	delete [] pstrOutput;
	//////////////////////////////////////////////////////////////////////////

	return 0;
}