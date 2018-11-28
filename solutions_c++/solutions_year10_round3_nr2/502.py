#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream fin("B-small-attempt0.in");
	ofstream fout("ProbelmB.out");
	
	int T;
	fin >> T;
	int i,j,k;
	int L,P,C;	
	int nTestNum = 0;
	int Temp = 0, times = 0;
	
	for (i=0;i<T;i++)
	{
		fin >> L >> P >> C;
		nTestNum = 0;

		times = 0;
		Temp = L;
		while(Temp < P)
		{
			Temp = Temp*C;
			times++;
		}

		Temp = 1;
		while (Temp<times)
		{
			Temp *= 2;
			nTestNum++;
		}

		fout << "Case #" << i+1 << ": " << nTestNum << endl;
			
	}
	fin.close();
	fout.close();
	return 0;
}