#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main () {
	FILE* In;
	FILE* Out;

	fopen_s(&In, "C-small-attempt0.in", "r");
	fopen_s(&Out, "C-small-attempt0.out", "w");

	int nTestCases, iTestCase;
	fscanf_s(In, "%d", &nTestCases);
	for (iTestCase=0; iTestCase < nTestCases; iTestCase++) {
		//Read Test Case
		int r, n, k;
		fscanf_s(In, "%d %d %d", &r, &k, &n);
		int i, iAllSum = 0, iLapNum = 0;
		int xiGroups[1010];

		for (i=0; i < n; i++) {
			fscanf_s(In, "%d", xiGroups+i);
			iAllSum += xiGroups[i];
		}
		//Solve Problem
		int xiStartGroups[1010];
		int xiEuroStartGroups[1010];
		int j, iPrevStart, iCurrentWeight, iEuroSum, iCycleInd;

		memset(xiStartGroups, 0, sizeof(xiStartGroups));
		memset(xiEuroStartGroups, 0, sizeof(xiEuroStartGroups));
		i = 1; j = 0; iPrevStart = 0; iCurrentWeight = 0; iEuroSum = 0; iCycleInd = 1;

		if (iAllSum <= k) {
			iEuroSum = r * iAllSum;
			iCycleInd = 0;
		}

		while (iCycleInd) {
			if (iCurrentWeight + xiGroups[j] > k) {
				iEuroSum += iCurrentWeight;
				iCurrentWeight = 0;
				xiStartGroups[iPrevStart] = i;
				xiEuroStartGroups[iPrevStart] = iEuroSum;
				iPrevStart = j;
				i++;
				if (i > r) {
					iCycleInd = 0;
					break;
				}
				if (xiStartGroups[j]) {
					int iCycleLength = i - xiStartGroups[j];
					iEuroSum = (r / iCycleLength) * iAllSum * iLapNum;
					j = r % iCycleLength;
					for (i=0; i < n; i++)
						if (j == xiStartGroups[i]) {
							iEuroSum += xiEuroStartGroups[i]; 
							break;
						}
					iCycleInd = 0;
					break;
				}
			}
			iCurrentWeight += xiGroups[j];
			j++;
			if (j>=n) {
				j %= n;
				iLapNum++;
			}
		}

		//Write Out Results
		fprintf_s(Out, "Case #%d: %d\n", iTestCase+1, iEuroSum);

	}

	if (In) fclose(In);
	if (Out) fclose(Out);

	return 0;
}
