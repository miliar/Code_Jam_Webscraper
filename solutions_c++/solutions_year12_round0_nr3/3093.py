#include <stdio.h>
#include <iostream>
#include<string>
using namespace std;

//return the pair num
bool checkIsRecycledPair(int a, int b)
{
	char cA[10];
	char cB[10];
	sprintf_s(cA, "%d", a);
	sprintf_s(cB, "%d", b);
	int iALen = strlen(cA);
	int iBLen = strlen(cB);
	if(iALen != iBLen) return false;
	for(int i = 0;i<iALen;i++){
		string sNewA;
		sNewA.append(cA, iALen - i, i);
		sNewA.append(cA, 0, iALen - i);
		if(sNewA.find(cB) != -1) return true;
	}
	return false;
}

int main()
{
	int iCaseNum = 0;
	cin >> iCaseNum;
	int **iInput = (int**)malloc(sizeof(int*) * iCaseNum);
	for(int i = 0; i < iCaseNum; i++){
		iInput[i] = (int*)malloc(sizeof(int) * 2);
	}
	cin.clear();
	cin.sync();
	for(int iCase = 0; iCase < iCaseNum; iCase++){
		cin >> iInput[iCase][0] >> iInput[iCase][1];
	}
	for(int iCase = 0; iCase < iCaseNum; iCase++){
		int nRecycledPairs = 0;
		bool **bIsChecked = (bool**)malloc(sizeof(bool*) * (iInput[iCase][1] + 1));
		for(int i = 0; i <= iInput[iCase][1]; i++){
			bIsChecked[i] = (bool*)malloc(sizeof(bool) * (iInput[iCase][1] + 1));
			memset(bIsChecked[i], false, (iInput[iCase][1] + 1));
		}
		for(int i = iInput[iCase][0]; i<= iInput[iCase][1]; i++){
			for(int j = i + 1; j <= iInput[iCase][1]; j++){
				if(bIsChecked[i][j] || bIsChecked[j][i]) continue;
				if(checkIsRecycledPair(i,j)) nRecycledPairs++;
				bIsChecked[i][j] = true;
				bIsChecked[j][i] = true;
			}
		}
		cout << "Case #" << iCase + 1<< ": " << nRecycledPairs << endl;
	}
	system("pause");
	return 0;
}