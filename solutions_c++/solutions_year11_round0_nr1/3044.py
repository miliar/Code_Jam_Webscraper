#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	int caseCnt, caseNum;
	int buttonCnt;
	int pos;
	char robot;
	char curRobot;
	
	int curOrgPos = 1;
	int curBluPos = 1;
	
	int dstOrgPos;
	int dstBluPos;
	
	vector<int> vecOrg;
	int vecOrgIx = 0;
	vector<int> vecBlu;
	int vecBluIx = 0;
	vector<char> vecSeq;
 	
	int tm = 0;
	int dltTm;
	
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	
	fin>>caseCnt;
	for(int i=0; i<caseCnt; ++i)
	{
	    caseNum = i+1;
		fin >> buttonCnt;
		for(int j=0; j<buttonCnt; ++j)
		{
			fin >> robot;
			fin >> pos;
			vecSeq.push_back(robot);
			if(robot=='O')
				vecOrg.push_back(pos);
			else
				vecBlu.push_back(pos);
		}

		for(int ix=0; ix<buttonCnt; ++ix)
		{
			curRobot = vecSeq[ix];			
			if(curRobot == 'O')
			{
				dstOrgPos = vecOrg[vecOrgIx++];				
				dltTm = dstOrgPos > curOrgPos ? (dstOrgPos-curOrgPos+1):(curOrgPos-dstOrgPos+1);  
				tm += dltTm;
				curOrgPos = dstOrgPos;
				
				if(vecBluIx < vecBlu.size())
				{				
					if(vecBlu[vecBluIx] > curBluPos)
					{
						if( curBluPos + dltTm > vecBlu[vecBluIx])
							curBluPos = vecBlu[vecBluIx];
						else
							curBluPos += dltTm;
					}
					else
					{
						if(curBluPos - dltTm < vecBlu[vecBluIx])
							curBluPos = vecBlu[vecBluIx];
						else
							curBluPos -= dltTm;
					}
				}
			}
			else
			{
				dstBluPos = vecBlu[vecBluIx++];
				dltTm = dstBluPos > curBluPos ? (dstBluPos - curBluPos+1):(curBluPos-dstBluPos+1);
				tm += dltTm;
				curBluPos = dstBluPos;
				
				if(vecOrgIx < vecOrg.size()){
					if(vecOrg[vecOrgIx] > curOrgPos)
					{	
						if( curOrgPos + dltTm > vecOrg[vecOrgIx])
							curOrgPos = vecOrg[vecOrgIx];
						else
							curOrgPos += dltTm;
					}
					else
					{
						if(curOrgPos - dltTm < vecOrg[vecOrgIx])
							curOrgPos = vecOrg[vecOrgIx];
						else
							curOrgPos -= dltTm;
					}
				}				
			}
		}
		
		fout<<"Case #"<<caseNum<<": "<<tm<<endl;
		vecOrg.clear();
		vecOrgIx = 0;
		vecBlu.clear();
		vecBluIx = 0;
		vecSeq.clear();
		
		tm = 0;
		curOrgPos = 1;
		curBluPos = 1;
	}
	fin.close();
	fout.close();
	return 0;
}