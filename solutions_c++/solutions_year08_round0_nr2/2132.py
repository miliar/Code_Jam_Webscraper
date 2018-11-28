#pragma warning(disable:4786)
#include <fstream>
#include <iterator>
#include <math.h>
#include <sstream>
#include <cstring>
#include <iostream.h>
#include<algorithm>
#include <vector>
using namespace std;
void GetLimit(vector<int>inA,vector<int>outA,vector<int>inB,vector<int>outB,int *ANum, int *bNum);
int turneraround = 0;
int main(int argc, char* argv[])
{
    ifstream fin("B-small-attempt5.in"); 
    ofstream fout("B-small-attempt5.out"); 
    string buf;
	char arrive[5] = {0},leave[5] = {0};
    getline(fin,buf);
	int anum,bnum;
    int case_max = atoi(buf.c_str());
    for (int i = 0; i < case_max; i++)
    {
        vector<int>inA;
        vector<int>inB;
        vector<int>outA;
        vector<int>outB;
		inA.push_back(1440);
		inB.push_back(1440);
       int nResult = 0;
        buf.empty();
		fin>>turneraround;
		fin>>anum>>bnum;
        for(int j = 0; j < anum; j++)
        {
            buf.empty();
			fin>>leave>>arrive;
			int leaveTime = atoi(&leave[0]) * 60;
			leaveTime += atoi(&leave[3]);
			int arriveTime = atoi(&arrive[0]) * 60;
			arriveTime += atoi(&arrive[3]);
			outA.push_back(leaveTime);
			inB.push_back(arriveTime);
        }
        for(j = 0; j < bnum; j++)
        {
            buf.empty();
			fin>>leave>>arrive;
			int leaveTime = atoi(&leave[0]) * 60;
			leaveTime += atoi(&leave[3]);
			int arriveTime = atoi(&arrive[0]) * 60;
			arriveTime += atoi(&arrive[3]);
			outB.push_back(leaveTime);
			inA.push_back(arriveTime);
        }
		int aLimit = 0,bLimit = 0;
		GetLimit(inA,outA,inB,outB,&aLimit,&bLimit);
        fout<<"Case #"<<i+1<<": "<<aLimit<<" "<<bLimit<<endl;
    }
    
    return 0;
}

void GetLimit(vector<int>inA,vector<int>outA,vector<int>inB,vector<int>outB,int *ANum, int *bNum)
{
	sort(inA.begin(),inA.end());
	sort(outA.begin(),outA.end());
	sort(inB.begin(),inB.end());
	sort(outB.begin(),outB.end());
	*ANum = outA.size();
	*bNum = outB.size();
	vector<int>::iterator iterIn = inA.begin();
	for (vector<int>::iterator iterOut = outA.begin();iterOut!=outA.end();iterOut++)
	{
		
		if (*iterOut >= (turneraround + *iterIn))
		{
			*ANum = *ANum-1;
			iterIn++;
		}
		if(iterIn == inA.end()|| *ANum == 0)
		{
			break;
		}		
	}
	iterIn = inB.begin();
	for (iterOut = outB.begin();iterOut!=outB.end();iterOut++)
	{
		if (*iterOut >= (turneraround + *iterIn))
		{
			*bNum = *bNum - 1;
			iterIn++;
		}
		if(iterIn == inB.end() || *bNum == 0)
		{
			break;
		}		
	}
}
