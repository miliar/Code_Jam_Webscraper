#include <stdio.h>
#include <iostream>
#include<string>
using namespace std;

int main()
{
	int iCaseNum = 0;
	cin >> iCaseNum;
	string *sInput = new string[iCaseNum];
	int *googlerNum = new int[iCaseNum];
	int *suprisingNum = new int[iCaseNum];
	int *maxNum = new int[iCaseNum];
	int **googlerPoint = (int **)malloc(sizeof(int *) * iCaseNum);
	cin.clear();
	cin.sync();
	for(int iCase = 0; iCase < iCaseNum; iCase++){
		cin >> googlerNum[iCase] >> suprisingNum[iCase] >> maxNum[iCase];
		googlerPoint[iCase] = (int *)malloc(sizeof(int) * googlerNum[iCase]);
		for(int i = 0 ;i < googlerNum[iCase]; i++){
			cin >> googlerPoint[iCase][i];
		}
	}
	
	for(int iCase = 0; iCase < iCaseNum; iCase++){
		string sOutput;
		int nShouldSuprising = 0;
		int nCanOverEqualMaxNum = 0;
		for(int i = 0 ;i < googlerNum[iCase]; i++){
			int iMinus = (googlerPoint[iCase][i] - maxNum[iCase]);
			if(iMinus < 0) continue;
			int iTest = maxNum[iCase] - (iMinus / 2);
			if(iTest == 2) nShouldSuprising++;
			else if(iTest < 2) nCanOverEqualMaxNum++;
		}
		if(nShouldSuprising > suprisingNum[iCase]) nCanOverEqualMaxNum += suprisingNum[iCase];
		else nCanOverEqualMaxNum += nShouldSuprising;
		cout << "Case #" << iCase + 1<< ": " << nCanOverEqualMaxNum << endl;
	}
	system("pause");
	return 0;
}