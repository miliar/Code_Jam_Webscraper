#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

inline int issimple(long long k) {
	int k1=2;
	while (k1*k1<=k) {
		if (k % k1 == 0) return 0;
		k1++;
	}
	return 1;
}

int main () {
	FILE* In;
	FILE* Out;

	fopen_s(&In, "C-small-attempt0.in", "r");
	fopen_s(&Out, "C-small-attempt0.out", "w");

	int nTestCases, iTestCase;
	fscanf_s(In, "%d", &nTestCases);
	for (iTestCase=0; iTestCase < nTestCases; iTestCase++) {
		long long n,i,j,ans;
		double nf;
		fscanf_s(In, "%lf", &nf);
		n = (long long)(nf);
		if (n==1) ans = 0;
		else if (n==2) ans = 1;
		else {
			i=2;
			ans = 1;
			while (i*i<=n) {
				if (issimple(i)) {
					j=i;
					while (j<=n) {
						j*=i;
						ans++;
					}
					ans--;
				}
				i++;
			}
		}

		//Write Out Results
		fprintf_s(Out, "Case #%d: %ld\n", iTestCase+1, ans);
	}

	if (In) fclose(In);
	if (Out) fclose(Out);

	return 0;
}
