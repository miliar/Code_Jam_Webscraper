#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>


int main () {
	FILE* In;
	FILE* Out;

	fopen_s(&In, "C-large.in", "r");
	fopen_s(&Out, "C-large.out", "w");

	int nTestCases, iTestCase;
	int n;
	fscanf_s(In, "%d", &nTestCases);
	for (iTestCase=0; iTestCase < nTestCases; iTestCase++) {
		fscanf_s(In, "%d", &n);
		int min = 1000000000, c, sum = 0, x = 0;
		for (int i = 0; i < n; i++) {
			fscanf_s(In, "%d", &c);
			if (c<min) min = c;
			x ^= c;
			sum += c;
		}
		//Write Out Results
		if (x == 0) fprintf_s(Out, "Case #%d: %d\n", iTestCase+1, sum-min);
		else fprintf_s(Out, "Case #%d: NO\n", iTestCase+1);

	}

	if (In) fclose(In);
	if (Out) fclose(Out);

	return 0;
}
