#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int main () {
	FILE* In;
	FILE* Out;

	fopen_s(&In, "B-large.in", "r");
	fopen_s(&Out, "B-large.out", "w");

	int c,d,i,j,x[300],n[300];
	int nTestCases, iTestCase;
	long long tek_x, newstep, maxstep;
	fscanf_s(In, "%d", &nTestCases);
	for (iTestCase=0; iTestCase < nTestCases; iTestCase++) {
		fscanf_s(In, "%d %d", &c,&d);
		for (i=0;i<c;i++) {
			fscanf_s(In, "%d %d", &x[i],&n[i]);
		}

		//for (i=0;i<c;i++) {
		//	int tek = 1000000000;
		//	for (j=i;j<c;j++) {
		//		if (x[j]<tek) {
		//		}
		//	}
		//}
		tek_x = x[0]-d;
		maxstep = 0;
		for (i=0;i<c;i++) {
			for (j=0;j<n[i];j++) {
				newstep = tek_x + d - x[i];
				if (newstep > maxstep)
					maxstep = newstep;
				if (tek_x + d < x[i])
					tek_x = x[i];
				else
					tek_x += d;
			}
		}
		//Write Out Results
		fprintf_s(Out, "Case #%d: %lf\n", iTestCase+1, ((double)maxstep)/2.);
	}

	if (In) fclose(In);
	if (Out) fclose(Out);

	return 0;
}
