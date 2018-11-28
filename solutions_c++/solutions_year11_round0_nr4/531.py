#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	//ifstream fin("D-small-attempt0.in");
	ifstream fin("D-large.in");
	//ofstream fout("DSmallOut.txt");
	ofstream fout("DLargeOut.txt");
	int nCaseNum,nCaseIdx;
	int nSeqNum,nSeqIdx;
	int nSeqData;
	fin >> nCaseNum;
	for (nCaseIdx=0;nCaseIdx<nCaseNum;nCaseIdx++)
	{
		int nMismatch=0;
		fin >> nSeqNum;
		for (nSeqIdx=1;nSeqIdx<=nSeqNum;nSeqIdx++)
		{
			fin >> nSeqData; 
			if(nSeqIdx!=nSeqData)
				nMismatch++;
		}
		fout << "Case #" << nCaseIdx+1 << ": ";
		fout << nMismatch << ".000000" << endl;
	}
	
	fin.close();
	fout.close();
	return 0;
}