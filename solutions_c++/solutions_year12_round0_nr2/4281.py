#include <iostream>
#include <fstream>

using namespace std;

int fyP2Avg(const int n);
int fyP4Avg(const int n);

int main()
{
	
	ifstream fin;
	ofstream fout;
	//fin.open("testin.txt");
	//fin.open("B-small-attempt0.in");	
	//fout.open("B-small-attempt0.out");
	
	fin.open("B-large.in");
	fout.open("B-large.out");
	
	int nCaseNum;
	fin >> nCaseNum;

	int nReadIdx;
	int nN,nS,np,nt;
	int ntIdx;
	int nSCnt = 0, nAbvPCnt = 0;
	for (nReadIdx=0;nReadIdx<nCaseNum;nReadIdx++)
	{
		fin >> nN >> nS >> np;
		nSCnt = 0; nAbvPCnt = 0;
		for (ntIdx=0;ntIdx<nN;ntIdx++)
		{
			fin >>nt;
			if (fyP2Avg(nt)>=np)
				nAbvPCnt++;
			else if ( (fyP4Avg(nt)>=np) && (nSCnt<nS) )
			{
				nSCnt++;
				nAbvPCnt++;
			}
		}

		fout << "Case #" << nReadIdx+1 << ": ";
		fout << nAbvPCnt;
		fout << endl;


	}
	
	fin.close();
	fout.close();
	return 0;
}

int fyP2Avg(const int n)
{
	if (n==0)
		return 0;
	else
		return  (n+2)/3;
}

int fyP4Avg(const int n)
{
	if (n==0)
		return 0;
	else
		return  (n+4)/3;
}