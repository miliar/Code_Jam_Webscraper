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
		fscanf_s(In, "%d %d\n", &n, &k);
		int i, j, l = 0;
		char Buf[100];
		int iBingo1 = 0;
		int iBingo2 = 0;
		int a[100][100];
		for (i=0;i<100;i++) 
			for (j=0;j<100;j++) 
				a[i][j]=0;
		for (i=0;i<n;i++) {
			l = 0;
			fgets(Buf, 100, In);
			for (j=n-1;j>=0;j--) {
				if (Buf[j]=='B') {
					a[i][l] = 1;
					l++;
				}
				else if (Buf[j]=='R') {
					a[i][l] = 2;
					l++;
				}
			}
		}
		//Solve Problem
		//horizontal
		for (i=0;i<n;i++) {
			int iSum1 = 0;
			int iSum2 = 0;
			for (j=0;j<n;j++) {
				if (a[i][j] == 1) {
					iSum1++;
					iSum2 = 0;
				}
				if (a[i][j] == 2) {
					iSum2++;
					iSum1 = 0;
				}
				if (a[i][j] == 0) {
					iSum2 = 0;
					iSum1 = 0;
				}
				if (iSum1 >= k) iBingo1 = 1;
				if (iSum2 >= k) iBingo2 = 1;
			}
		}
		//vertical
		for (i=0;i<n;i++) {
			int iSum1 = 0;
			int iSum2 = 0;
			for (j=0;j<n;j++) {
				if (a[j][i] == 1) {
					iSum1++;
					iSum2 = 0;
				}
				if (a[j][i] == 2) {
					iSum2++;
					iSum1 = 0;
				}
				if (a[j][i] == 0) {
					iSum2 = 0;
					iSum1 = 0;
				}
				if (iSum1 >= k) iBingo1 = 1;
				if (iSum2 >= k) iBingo2 = 1;
			}
		}
		//diagonal /
		for (l=0;l<2*n-1;l++) {
			int iSum1 = 0;
			int iSum2 = 0;
			if (l<n) { 
				i=0;
				j=l;
			}
			else {
				i=l-n+1;
				j=n-1;
			}
			while (i<n && j>=0) {
				if (a[j][i] == 1) {
					iSum1++;
					iSum2 = 0;
				}
				if (a[j][i] == 2) {
					iSum2++;
					iSum1 = 0;
				}
				if (a[j][i] == 0) {
					iSum2 = 0;
					iSum1 = 0;
				}
				if (iSum1 >= k) iBingo1 = 1;
				if (iSum2 >= k) iBingo2 = 1;
				i++;
				j--;
			}
		}
		//diagonal |
		for (l=0;l<2*n-1;l++) {
			int iSum1 = 0;
			int iSum2 = 0;
			if (l<n) { 
				i=0;
				j=l;
			}
			else {
				i=l-n+1;
				j=0;
			}
			while (i<n && j<n) {
				if (a[j][i] == 1) {
					iSum1++;
					iSum2 = 0;
				}
				if (a[j][i] == 2) {
					iSum2++;
					iSum1 = 0;
				}
				if (a[j][i] == 0) {
					iSum2 = 0;
					iSum1 = 0;
				}
				if (iSum1 >= k) iBingo1 = 1;
				if (iSum2 >= k) iBingo2 = 1;
				i++;
				j++;
			}
		}
		//Write Out Results
		fprintf_s(Out, "Case #%d:", iTestCase+1);
		if (iBingo1 && iBingo2) fprintf_s(Out, " Both\n");
		else if (iBingo1) fprintf_s(Out, " Blue\n");
		else if (iBingo2) fprintf_s(Out, " Red\n");
		else fprintf_s(Out, " Neither\n");
	}

	if (In) fclose(In);
	if (Out) fclose(Out);

	return 0;
}

