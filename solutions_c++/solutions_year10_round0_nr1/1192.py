#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main () {
	FILE* In;
	FILE* Out;

	fopen_s(&In, "A-large.in", "r");
	fopen_s(&Out, "A-large.out", "w");

	int nTestCases, iTestCase;
	fscanf_s(In, "%d", &nTestCases);
	for (iTestCase=0; iTestCase < nTestCases; iTestCase++) {
		//Read Test Case
		int n, k;
		fscanf_s(In, "%d %d", &n, &k);
		//Solve Problem
		int i, iPower = 1, iSw = 0;
		for (i=0;i<n;i++) 
			iPower *= 2;
		if (((k+1) % iPower)) iSw = 0;
		else iSw = 1;
		//Write Out Results
		fprintf_s(Out, "Case #%d:", iTestCase+1);
		if (iSw) fprintf_s(Out, " ON\n");
		else fprintf_s(Out, " OFF\n");
	}

	if (In) fclose(In);
	if (Out) fclose(Out);

	return 0;
}
