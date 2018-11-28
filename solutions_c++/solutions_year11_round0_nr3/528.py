#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int main()
{
	//ifstream fin("C-small-attempt1.in");
	ifstream fin("C-large.in");
	//ofstream fout("CSmallOut.txt");
	ofstream fout("CLargeOut.txt");
	int nCaseNum,nCaseIdx;
	int nSeqNum, nSeqIdx;
	int nValue;	
	fin >> nCaseNum;
	for (nCaseIdx=0;nCaseIdx<nCaseNum;nCaseIdx++)
	{
		int nTotalValue = 0;
		int nSmallestValue = 1000000;
		long nSumValue = 0;
		fin >> nSeqNum;
		for (nSeqIdx=0;nSeqIdx<nSeqNum;nSeqIdx++)
		{
			fin >> nValue;
			if(nSmallestValue>nValue)
				nSmallestValue = nValue;
			nTotalValue = nTotalValue^nValue;
			nSumValue += nValue;
		}
		
		fout << "Case #" << nCaseIdx+1 << ": ";
		if (nTotalValue)
			fout << "NO";
		else 
			fout << nSumValue-nSmallestValue;
		fout << endl;
	}
	
	fin.close();
	fout.close();
	return 0;
}