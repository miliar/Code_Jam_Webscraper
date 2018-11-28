#include <fstream>
#include <sstream>

using namespace std;

int main()
{
	ifstream ifs("A-large.in");
	ofstream ofs("output.txt");
	string sLine = "";
	bool bFirstLineRead = false;
	int iTestCaseCount = 0;
	int iTestCaseNo = 0;
	
	while(getline(ifs, sLine))
	{
		istringstream ss(sLine);

		if(!bFirstLineRead)
		{
			ss >> iTestCaseCount;
			bFirstLineRead = true;
		}
		else
		{
			++iTestCaseNo;
			int iStepsCount = 0;
			ss >> iStepsCount;
			int iTotalTime = 0;
			int iBCurrPos = 1;
			int iOCurrPos = 1;
			int iBAdditionalTime = 0;
			int iOAdditionalTime = 0;
			for(int iStep = 1; iStep <= iStepsCount; ++iStep)
			{
				char ch;
				ss >> ch;
				int iButton;
				ss >> iButton;

				int* pCurrPos = 0;
				int* pAdditionalTime = 0;
				int* pOthersAdditionalTime = 0;

				if('B' == ch)
				{
					pCurrPos = &iBCurrPos;
					pAdditionalTime = &iBAdditionalTime;
					pOthersAdditionalTime = &iOAdditionalTime;
				}
				else if('O' == ch)
				{
					pCurrPos = &iOCurrPos;
					pAdditionalTime = &iOAdditionalTime;
					pOthersAdditionalTime = &iBAdditionalTime;
				}
				else
				{
					continue;
				}

				int iDist = (iButton > (*pCurrPos)) ? (iButton - (*pCurrPos)) : ((*pCurrPos) - iButton);
				int iTimeToTravel = (iDist > (*pAdditionalTime)) ? (iDist - (*pAdditionalTime)) : 0;
				int iTimeToAction = iTimeToTravel + 1;
				(*pOthersAdditionalTime) += iTimeToAction;
				iTotalTime += iTimeToAction;
				(*pAdditionalTime) = 0;
				(*pCurrPos) = iButton;
			}
			ofs << "Case #" << iTestCaseNo << ": " << iTotalTime << endl;
		}
	}
}