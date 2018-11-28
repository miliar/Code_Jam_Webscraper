#include <fstream>
#include <cmath>
using namespace std;
int main()
{
	int iLine = 0;
	int iSnapperNum = 0;
	int iSnapTime = 0;
	int Freq = 1;
	ifstream filein("A-large.in");
	ofstream fileout("A-large.out");
	if (filein)
	{
		filein >> iLine;
		for (int i = 0; i < iLine; i++)
		{
			filein >> iSnapperNum;
			filein >> iSnapTime;
			fileout << "Case #" << (i+1) <<": ";
			Freq = 1;
			for (int j = 0; j < iSnapperNum; j++)
			{
				Freq *= 2;
			}
			if (((iSnapTime+1)%Freq)) 
			{
				fileout << "OFF\n";
			}
			else
			{
				fileout << "ON\n";
			}
		}
	}
	return 0;
}

