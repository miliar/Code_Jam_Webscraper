#include <iostream>
#include <fstream>
#include <vector>
#include <strstream>
#include <string>
#include <map>

using namespace std;

class CMyMark
{
public:
	void InitMark(int i);
	void ClearMark(int i);
	void Mark(int idx);
	bool IsLastOne();
	int  GetClearTime();
private:
	int iLength;
	vector<int> vMarkStat;
	int iSum;
	int iTimer;
};

void CMyMark::InitMark(int i)
{
	vMarkStat.resize(i, 1);
	iLength = i;
	iSum = iLength;
	iTimer = 0;
}

void CMyMark::ClearMark(int i)
{
	vMarkStat.assign(iLength, 1);
	vMarkStat[i] = 0;
	iSum = iLength - 1;
	iTimer++;
}

void CMyMark::Mark(int idx)
{
	if (vMarkStat[idx] == 1)
	{
		vMarkStat[idx] = 0;
		iSum--;
	} 
}

bool CMyMark::IsLastOne()
{
	if(iSum == 0)
		return true;
	else
		return false;
}

int CMyMark::GetClearTime()
{
	return iTimer;
}

void main()
{
	ifstream ifs("A-large.in");
	ofstream ofs("A-large.out");
	int iTestNumber;
	ifs>>iTestNumber;

	for (int i=0; i<iTestNumber; i++)
	{
		int iEngNumber;
		ifs>>iEngNumber;
		ifs.ignore(1);
		map<string, int> vEngineMap;
		vector<string> vEngineName;
		vEngineName.resize(iEngNumber);

		for (int j=0; j<iEngNumber; j++)
		{
			getline(ifs, vEngineName[j]);
			//cout<<vEngineName[j]<<endl;
			vEngineMap[vEngineName[j]] = j;
		}

		//cout << "-----"<<endl;

		int iQueNumber;
		ifs>>iQueNumber;
		ifs.ignore(1);
		vector<string> vQueue;
		vQueue.resize(iQueNumber);
		CMyMark myMark;
		myMark.InitMark(iEngNumber);

		for (int j=0; j<iQueNumber; j++)
		{
			getline(ifs, vQueue[j]);
			//cout<<vQueue[j]<<endl;
			int idx = vEngineMap[vQueue[j]];
			myMark.Mark(idx);
			if (myMark.IsLastOne())
			{
				myMark.ClearMark(idx);
			}
		}
		ofs<<"Case #"<<i+1<<": "<<myMark.GetClearTime()<<endl;
	}
}