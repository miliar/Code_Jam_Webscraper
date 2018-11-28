#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

#define MAX 100000
#define EPS 1e-7

int main () {
	FILE* In;
	FILE* Out;

	fopen_s(&In, "A-large.in", "r");
	fopen_s(&Out, "A-large.out", "w");

	int nTestCases, iTestCase;
	fscanf_s(In, "%d", &nTestCases);
	for (iTestCase=0; iTestCase < nTestCases; iTestCase++) {
		int i, sum = 0, n;
		int a[10010], d[10010], l[10010];
		fscanf_s(In, "%d", &n);
		int dprev = 0, maxl,len;
		for (i=0;i<n;i++) {
			fscanf_s(In, "%d %d", &d[i], &l[i]);
			a[i] = -1;
		}
		fscanf_s(In, "%d", &len);
		a[0] = d[0];
		for (i=0;i<n;i++) {
			//if (l[i] < d[i]-dprev)
			//	maxl = l[i];
			//else 
			//	maxl = d[i]-dprev;

			//if (maxl > a[i])
			//	a[i] = maxl;
			//else 
			//	continue;

			for (int j=i+1;j<n;j++) {
				if (a[i]+d[i] >= d[j]) {
					if (l[j] < d[j]-d[i])
						maxl = l[j];
					else 
						maxl = d[j]-d[i];
					if (maxl > a[j])
						a[j] = maxl;
				}
			}
		}
		//Write Out Results
		bool can = false;
		for (i=0; i<n; i++) {
			if (a[i] > 0 && a[i] + d[i] >= len) {
				fprintf_s(Out, "Case #%d: YES\n", iTestCase+1);
				can = true;
				break;
			}
		}
		if (!can)
			fprintf_s(Out, "Case #%d: NO\n", iTestCase+1);
		//Write Out Results

	}

	if (In) fclose(In);
	if (Out) fclose(Out);

	return 0;
}
