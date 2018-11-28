#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	int caseCnt, caseNum;
	int comboCnt, oppCnt;
	int len;
	string strList;
	string strCombo, strOpp;
	char combo[128][128];	
	char opp[128];
	char bitset[128];
	vector<char> vec;
	
	ifstream fin("B-small-attempt5.in");
	ofstream fout("B-small-attempt5.out");
	fin>>caseCnt;
	
	int C1,C2,C;
		
	for(int i=0; i<caseCnt; ++i)
	{
		memset(combo, 0, 128*128);
		memset(opp,0,128);
		memset(bitset,0,128);		
		vec.clear();
		C = 0;
		C1 = 0;
		C2 = 0;
		
		fin>>comboCnt;
		for(int j=0; j<comboCnt; ++j)
		{
			fin>>strCombo;
			combo[strCombo[0]][strCombo[1]] = strCombo[2];
			combo[strCombo[1]][strCombo[0]] = strCombo[2];
		}
		fin>>oppCnt;
		for(int k=0; k<oppCnt; ++k)
		{
			fin>>strOpp;
			opp[strOpp[0]] = strOpp[1];
			opp[strOpp[1]] = strOpp[0];
		}
		
		fin>>len;
		fin>>strList;		
		for(int ix=0; ix<len; ++ix)
		{	
			C=0;
			C2 = strList[ix];			
			if(vec.size() == 0)
			{
				vec.push_back(C2);
				bitset[C2]++;
				continue;
			}			
									
			if(comboCnt)
			{
				C1 = vec.back();
				C = combo[C1][C2];
				if(C > 0)
				{
					bitset[C1]--;
					vec.pop_back();					
					vec.push_back(C);					
				}
				else
				{
					bitset[C2]++;
					vec.push_back(C2);					
				}
			}
			else
			{
				bitset[C2]++;
				vec.push_back(C2);	
			}
			
			if(0==C)
			{
				if(oppCnt && bitset[opp[vec.back()]])
				{
					vec.clear();
					memset(bitset,0,128);					
				}
			}			
		}		
		
		caseNum = i+1;		
		fout<<"Case #"<<caseNum<<": "<<"[";
		if(vec.size() > 0)
		{
			for(int vecIx=0; vecIx<vec.size()-1; ++vecIx)
			{			
				fout<<vec[vecIx]<<", ";
			}
			fout<<vec.back();
		}
		fout<<"]"<<endl;		
	}
	fin.close();
	fout.close();
	return 0;
}