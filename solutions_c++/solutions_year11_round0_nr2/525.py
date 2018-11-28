#include <iostream>
#include <fstream>
#include <math.h>
#include <string>

using namespace std;

int main()
{
	//ifstream fin("B-small-attempt2.in");
	ifstream fin("B-large.in");
	//ofstream fout("BSmallOut.txt");
	ofstream fout("BLargeOut.txt");
	int nCaseNum,nCaseIdx;
	fin >> nCaseNum;
	int nCombineNum, nCombineIdx;
	int nOpposeNum, nOpposeIdx;
	int nSeqNum, nSeqIdx;
	for (nCaseIdx=0;nCaseIdx<nCaseNum;nCaseIdx++)
	{
		int chMagicCombineRule[26][26],chMagicOppoRule[26][26];
		int i,j;
		for (i=0;i<26;i++)
			for(j=0;j<26;j++)
			{
				chMagicCombineRule[i][j] =0;
				chMagicOppoRule[i][j] = 0;	
			}

		string strInput;
		char ch1,ch2,ch3;

		// set rules: combining rule
		fin >> nCombineNum;
		for (nCombineIdx=0;nCombineIdx<nCombineNum;nCombineIdx++)
		{
			fin >> strInput;
			ch1 = strInput[0];
			ch2 = strInput[1];
			ch3 = strInput[2];
			chMagicCombineRule[ch1-'A'][ch2-'A'] = ch3-'A'+1; // notice: there is 1 plus here
			chMagicCombineRule[ch2-'A'][ch1-'A'] = ch3-'A'+1; 
		}

		// set rules: opposing rule
		fin >> nOpposeNum;
		for (nOpposeIdx=0;nOpposeIdx<nOpposeNum;nOpposeIdx++)
		{
			fin >> strInput;
			ch1 = strInput[0];
			ch2 = strInput[1];
			chMagicOppoRule[ch1-'A'][ch2-'A'] = 1;
			chMagicOppoRule[ch2-'A'][ch1-'A'] = 1;
		}

		fin >> nSeqNum;
		int nSeqLen = 0;
		int chSeq[100];
		for (nSeqIdx=0;nSeqIdx<nSeqNum;nSeqIdx++)
		{
			fin >> ch1;
			nSeqLen++;
			chSeq[nSeqLen-1]=ch1-'A';
			while (nSeqLen>1)
			{
				if(chMagicCombineRule[chSeq[nSeqLen-1]][chSeq[nSeqLen-2]]>0)
				// first priority, combining elements
				{
					chSeq[nSeqLen-2] = chMagicCombineRule[chSeq[nSeqLen-1]][chSeq[nSeqLen-2]]-1; // notice: remove the 1 plus here
					nSeqLen--;					
				}
				else
				// second priority, erasing seq while opposing elements exist
				{
					int nIdx = nSeqLen-2;
					while (nIdx>=0)
					{
						if (chMagicOppoRule[chSeq[nSeqLen-1]][chSeq[nIdx]]>0)
						{
							nSeqLen = 0;
							break;
						}
						else
							nIdx--;
					}
					if(nIdx<0)
						break;
				}
			}
		}

		// output
		fout << "Case #" << nCaseIdx+1 << ": ";
		fout << '[';
		for(i=0;i<nSeqLen;i++)
		{
			fout << char('A'+chSeq[i]);
			if (i<nSeqLen-1)
				fout << ", ";
		}
		fout << ']' << endl;

	}

	fin.close();
	fout.close();
	return 0;
}