#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main () {
	FILE* In;
	FILE* Out;

	fopen_s(&In, "B-large.in", "r");
	fopen_s(&Out, "B-large.out", "w");

	int nTestCases, iTestCase;
	fscanf_s(In, "%d", &nTestCases);
	for (iTestCase=0; iTestCase < nTestCases; iTestCase++) {
		//Read Test Case
		int n, k, b, t;
		fscanf_s(In, "%d %d %d %d\n", &n, &k, &b, &t);
		int i;
		int x[100], v[100], xf[100];
		for (i=0;i<n;i++)
			fscanf_s(In, "%d", x+i);
		for (i=0;i<n;i++)
			fscanf_s(In, "%d", v+i);
		//Solve Problem
		for (i=0;i<n;i++) {
			xf[i] = x[i] + t*v[i];
		}
		int kf = 0;
		int s = 0;
		for (i=n-1;i>=0;i--) {
			if (xf[i] >= b) {
				s += (n-1) - i - kf;
				kf++;
				if (kf>=k)
					break;
			}
		}
		//Write Out Results
		fprintf_s(Out, "Case #%d:", iTestCase+1);
		if (kf>=k) 
			fprintf_s(Out, " %d\n", s);
		else 
			fprintf_s(Out, " IMPOSSIBLE\n", s);
	}

	if (In) fclose(In);
	if (Out) fclose(Out);

	return 0;
}

