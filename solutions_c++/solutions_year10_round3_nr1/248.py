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
		int n, i, j;
		fscanf_s(In, "%d\n", &n);
		int a[2000], b[2000];
		for (i=0;i<n;i++) {
			fscanf_s(In, "%d %d\n", a+i, b+i);
		}
		//Solve Problem
		int glob_min = 0;

		for (i=0;i<n;i++) {
			for (j=0;j<i;j++) {
				if ((a[i]-a[j])*(b[i]-b[j]) < 0)
					glob_min++;
			}
		}
		//Write Out Results
		fprintf_s(Out, "Case #%d:", iTestCase+1);
		fprintf_s(Out, " %d\n", glob_min);
	}

	if (In) fclose(In);
	if (Out) fclose(Out);

	return 0;
}

