#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("LargeOut.txt");
	//ofstream fout("SmallOut.txt");
	int nCaseNum,nCaseIdx;
	fin >> nCaseNum;
	int nSeqNum,nSeqIdx;
	char chRobot;
	int nPosIdx;
	for (nCaseIdx=0;nCaseIdx<nCaseNum;nCaseIdx++)
	{
		int nLastPos[2] = {1,1};
		int nCurrRobot = 0, nLastRobot = 0; // 0 for orange, 1 for blue
		int nTotalTime = 0;
		int nDurationTime = 0;
		fin >> nSeqNum;
		for (nSeqIdx=0;nSeqIdx<nSeqNum;nSeqIdx++)
		{
			fin >> chRobot;
			fin >> nPosIdx;
			if (chRobot == 'O')
				nCurrRobot = 0;
			else
				nCurrRobot = 1;
			if (nCurrRobot == nLastRobot)
			{
				nTotalTime += abs(nPosIdx-nLastPos[nCurrRobot])+1;
				nDurationTime += abs(nPosIdx-nLastPos[nCurrRobot])+1;
				nLastPos[nCurrRobot] = nPosIdx;
			}
			else
			{
				if (abs(nPosIdx-nLastPos[nCurrRobot])<=nDurationTime)
				{
					nTotalTime += 1;
					nDurationTime = 1;
					nLastPos[nCurrRobot] = nPosIdx;
				}
				else
				{
					nTotalTime += abs(nPosIdx-nLastPos[nCurrRobot])-nDurationTime+1;
					nDurationTime = abs(nPosIdx-nLastPos[nCurrRobot])-nDurationTime+1;
					nLastPos[nCurrRobot] = nPosIdx;
				}
			}
			nLastRobot = nCurrRobot;
		}

		fout << "Case #" << nCaseIdx+1 << ": " << nTotalTime << endl;
	}

	fin.close();
	fout.close();
	return 0;
}