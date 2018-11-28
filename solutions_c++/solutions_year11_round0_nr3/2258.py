#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

int PatrickAdd(int a, int b)
{
	int iRes = 0;
	int iAdd = 1;
	while(a | b)
	{
		unsigned char uc1 = a & 1;
		unsigned char uc2 = b & 1;
		if((uc1 & (!uc2)) || ((!uc1) & uc2))
		{
			iRes += iAdd;
		}
		a >>= 1;
		b >>= 1;
		iAdd <<= 1;
	}

	return iRes;
}

int main()
{
	ifstream ifs("C-large.in");
	ofstream ofs("output.txt");
	bool bFirstLineRead = false;
	string sLine = "";
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
			if(iTestCaseNo > iTestCaseCount)
			{
				break;
			}
			int iCandyCount = 0;
			ss >> iCandyCount;
			getline(ifs, sLine);
			istringstream ss2(sLine);
			vector<int> vecCandies(iCandyCount);
			int iIndex = 0;
			int iCandy = 0;
			int iCandySum = 0;
			int iCandyPatrickSum = 0;
			int iSmallest = -1;
			for( ; iIndex < iCandyCount; ++iIndex)
			{
				ss2 >> iCandy;
				vecCandies[iIndex] = iCandy;
				iCandySum += iCandy;
				iCandyPatrickSum = PatrickAdd(iCandyPatrickSum, iCandy);
				if((-1 == iSmallest) || (iCandy < iSmallest))
				{
					iSmallest = iCandy;
				}
			}

			if(0 == iCandyPatrickSum)
			{
				// solution exists
				ofs << "Case #" << iTestCaseNo << ": " << iCandySum - iSmallest << endl;
			}
			else
			{
				ofs << "Case #" << iTestCaseNo << ": NO" << endl;
			}
		}
	}
}