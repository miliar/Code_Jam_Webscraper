#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int main () {
	FILE* In;
	FILE* Out;

	fopen_s(&In, "D-large.in", "r");
	fopen_s(&Out, "D-large.out", "w");

	int nTestCases, iTestCase;
	int xdNumber[1000];
	int xdNumberFirst[1000];
	fscanf_s(In, "%d", &nTestCases);
	for (iTestCase=0; iTestCase < nTestCases; iTestCase++) {
		int nNumbers, iNumbers;
		fscanf_s(In, "%d", &nNumbers);
		for (iNumbers=0; iNumbers < nNumbers; iNumbers++) {
			fscanf_s(In, "%d", xdNumber+iNumbers);
			xdNumberFirst[iNumbers] = xdNumber[iNumbers];
		}
		int sorted = 0;
		qsort(xdNumber, nNumbers, sizeof(int),compare);
		for (int i = 0; i < nNumbers; i++) {
			if (xdNumber[i] == xdNumberFirst[i]) {
				sorted++;
			}
		}
		double ans = (double)(nNumbers-sorted);
		//Write Out Results
		fprintf_s(Out, "Case #%d: %lf\n", iTestCase+1, ans);

	}

	if (In) fclose(In);
	if (Out) fclose(Out);

	return 0;
}
