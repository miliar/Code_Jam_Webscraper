#include <Math.h>
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int testCases;
	in >> testCases;
	int result[100];

	for(int i = 0; i < testCases; i ++)
	{
		int numberButtons;
		int caseO = 0;
		int caseB = 0;
		int currPosO = 1;
		int currPosB = 1;
		in >> numberButtons;
		while(numberButtons-- > 0)
		{
			char robColor;
			int pushedButton;
			in >> robColor;
			in >> pushedButton;

			if(robColor == 'O')
			{
				caseO = caseO + abs(pushedButton - currPosO) + 1;
				currPosO = pushedButton;
				if(caseO - caseB <= 0)
					caseO += caseB - caseO + 1;
			}
			else if(robColor == 'B')
			{
				caseB = caseB + abs(pushedButton - currPosB) + 1;
				currPosB = pushedButton;
				if(caseB - caseO <= 0)
					caseB += caseO - caseB + 1;
			}
		}
		if(caseO > caseB)
		{
			result[i] = caseO;
		}
		else if(caseO < caseB)
		{
			result[i] = caseB;
		}
	}

	for(int i = 0; i < testCases; i++)
	{
		out << "Case #" << (i + 1) << ": " << result[i] << endl ;
	}
	return 0;
}
