#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int main () {
	FILE* In;
	FILE* Out;

	fopen_s(&In, "B-large.in", "r");
	fopen_s(&Out, "B-large.out", "w");

	int nTestCases, iTestCase;
	fscanf_s(In, "%d", &nTestCases);
	for (iTestCase=0; iTestCase < nTestCases; iTestCase++) {
		//Read Test Case
		int l,p,c;
		fscanf_s(In, "%d %d %d\n", &l, &p, &c);
		//Solve Problem
		long long l1 = l;
		int pow = 0;
		while (l1<p) {
			l1 *= c;
			pow++;
		}
		l1 = 1;
		int pow_a = 0;
		while (l1<pow) {
			l1 *= 2;
			pow_a++;
		}
		//Write Out Results
		fprintf_s(Out, "Case #%d:", iTestCase+1);
		fprintf_s(Out, " %d\n", pow_a);
	}

	if (In) fclose(In);
	if (Out) fclose(Out);

	return 0;
}

