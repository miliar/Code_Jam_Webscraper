#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int main () {
	FILE* In;
	FILE* Out;

	fopen_s(&In, "A-large.in", "r");
	fopen_s(&Out, "A-large.out", "w");

	char res[200][200];
	double owp[200][200];
	double wp[200], games[200];
	int i,k, iTestCase,nTestCases;
	fscanf_s(In, "%d", &nTestCases);
	for (iTestCase=0; iTestCase < nTestCases; iTestCase++) {
		int nNumbers, iNumbers;
		fscanf_s(In, "%d", &nNumbers);
		for (iNumbers=0; iNumbers < nNumbers; iNumbers++) {
				fscanf(In, "%s", &res[iNumbers]);
		}
		for (iNumbers=0; iNumbers < nNumbers; iNumbers++) {
			wp[iNumbers] = 0.;
			games[iNumbers] = 0.;
			for (i=0;i<nNumbers;i++) {
				if (res[iNumbers][i] == '1') wp[iNumbers]+=1.;
				if (res[iNumbers][i] == '1' ||
					res[iNumbers][i] == '0') games[iNumbers]+=1.;
			}
			for (i=0;i<nNumbers;i++) {
				if (res[iNumbers][i] == '1') {
					owp[iNumbers][i]= (wp[iNumbers]-1.)/(games[iNumbers]-1.);
				} else if (res[iNumbers][i] == '0') {
					owp[iNumbers][i]= (wp[iNumbers])/(games[iNumbers]-1.);
				} else {
					owp[iNumbers][i]= (wp[iNumbers])/(games[iNumbers]);
				}
			}
			wp[iNumbers] /= games[iNumbers];
		}

		//Write Out Results
		fprintf_s(Out, "Case #%d:\n", iTestCase+1);
		for (iNumbers=0; iNumbers < nNumbers; iNumbers++) {
			double IRP = 0.25*wp[iNumbers];
			double IRP1 =0.;
			double IRP3 = 0.;
			for (i=0;i<nNumbers;i++) {
				if (res[iNumbers][i] == '1' ||
					res[iNumbers][i] == '0') {
					double IRP2 = 0.;
					for (k=0;k<nNumbers;k++) {
						if (res[k][i] == '1' ||
							res[k][i] == '0') 
							IRP2 += owp[k][i];
					}
					IRP3 += IRP2 / games[i];
					IRP1 += owp[i][iNumbers];
				}
			}
			IRP += 0.5*(IRP1 / games[iNumbers]);
			IRP += 0.25*(IRP3 / games[iNumbers]);
			fprintf_s(Out, "%lf\n", IRP);
		}
	}

	if (In) fclose(In);
	if (Out) fclose(Out);

	return 0;
}
