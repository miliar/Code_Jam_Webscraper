//============================================================================
// Name        : Qualification.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <math.h>

using namespace std;

bool IsLightOn(int nChainLen, int nToggles)
{
	bool isLightOn = false;
	isLightOn = (((1 << nChainLen) - 1) & nToggles) == ((1 << nChainLen) - 1);

	return isLightOn;
}

int main()
{
	FILE *pSourceFile = NULL;
	FILE *pTargetFile = NULL;

	pSourceFile = fopen("A-large.in", "r");
	pTargetFile = fopen("output.txt", "w");

	int n;
	int k;
	int nTotalCases = 0;

	fscanf(pSourceFile, "%i", &nTotalCases);
	for(int i = 0; i < nTotalCases; i++)
	{
		fscanf(pSourceFile, "%i %i\n", &n, &k);

		fprintf(pTargetFile, "Case #%i: %s\n", i + 1, IsLightOn(n, k) ? "ON" : "OFF");
	}

	fclose(pSourceFile);
	fclose(pTargetFile);

	return 0;
}
