#include <fstream>
#include <queue>
using namespace std;
int main()
{
	int iCalcCount = 0;
	int iRunTimePerDay = 0;
	int iMaxPassenger = 0;
	int iGroupNum = 0;
	int iEarn = 0;
	int iTemp,iTemp2;
	ifstream filein("C.in");
	ofstream fileout("C.out");
	if (filein) 
	{
		filein >> iCalcCount;
		for (int i = 0; i < iCalcCount; i++) 
		{
			queue<int> qGroups;
			iEarn = 0;
			filein >> iRunTimePerDay >> iMaxPassenger >> iGroupNum;
			for (int j = 0; j < iGroupNum; j++) 
			{
				filein >> iTemp;
				qGroups.push(iTemp);
			}
			for (int j = 0; j < iRunTimePerDay; j++) 
			{
				iTemp = 0;
				iTemp2 = 0;
				while (iTemp +qGroups.front() <= iMaxPassenger) 
				{
					iTemp += qGroups.front();
					qGroups.push(qGroups.front());
					qGroups.pop();
					iTemp2++;
					if (iTemp2 >= iGroupNum) 
					{
						break;
					}
				}
				iEarn += iTemp;
			}
			fileout << "Case #" << (i+1) <<": " << iEarn <<endl;
		}
	}
	return 0;
}
