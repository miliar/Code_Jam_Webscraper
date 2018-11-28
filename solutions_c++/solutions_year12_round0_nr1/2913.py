#include <iostream>
#include<string>
using namespace std;

int main()
{
	string sAns = string("ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupzq");
	string sTestCase = string("ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvqz");
	int iCaseNum = 0;
	cin >> iCaseNum;
	string *sInput = new string[iCaseNum];
	cin.clear();
	cin.sync();
	for(int iCase = 0; iCase < iCaseNum; iCase++){
		getline(cin, sInput[iCase]);
	}
	for(int iCase = 0; iCase < iCaseNum; iCase++){
		string sOutput;
		for(unsigned int i = 0; i<sInput[iCase].length();i++){
			size_t iFind = sTestCase.find(sInput[iCase].at(i), 0);
			if(iFind == -1) sOutput.append(sInput[iCase], i, 1);
			else sOutput.append(sAns, iFind, 1);
		}
		cout << "Case #" << iCase + 1<< ": " << sOutput << endl;
	}
	system("pause");
	return 0;
}