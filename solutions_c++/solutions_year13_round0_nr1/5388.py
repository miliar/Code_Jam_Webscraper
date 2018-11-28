#include<iostream>
#include<fstream>
using namespace std;

char*writeSummary(char selection[4][4]);

int main ()
{
	ifstream myfileIn;
	myfileIn.open ("C:/stack/oldstuff/Computer Languages/Google/sample.txt");
	if(!myfileIn.good())
	{
		return 0;
	}
	int cases = 0;
	myfileIn >> cases;
	
	ofstream myfileOut;
	myfileOut.open ("C:/stack/oldstuff/Computer Languages/Google/out.txt");
	for(int i = 0; i < cases; i++)
	{
		char selection[4][4];
		for(int y = 0; y < 4; y++)
		{
			for(int x = 0; x < 4; x++)
			{
				myfileIn >> selection[x][y];
			}
		}
		myfileOut << "Case #" << (i+1) << ": " << writeSummary(selection) << endl;
		cout << "Case #" << (i+1) << ": " << writeSummary(selection) << endl;
	}



	myfileIn.close();
	myfileOut.close();
	return 0;
}

char*writeSummary(char selection[4][4])
{
	for(int select = 0; select < 4; select++)
	{
		char start = selection[select][0];
		int adjust = 1;
		while(start == 'T' && adjust < 4)
		{
			start = selection[select][adjust];
			adjust++;
		}
		if((selection[select][1] == start || selection[select][1] == 'T' || adjust > 1) &&
			(selection[select][2] == start || selection[select][2] == 'T' || adjust > 2) &&
			(selection[select][3] == start || selection[select][3] == 'T' || adjust > 3))
		{
			switch(start)
			{
			case 'X':
				return "X won";
				break;
			case 'O':
				return "O won";
				break;
			}
		}


		start = selection[0][select];
		adjust = 1;
		while(start == 'T' && adjust < 4)
		{
			start = selection[adjust][select];
			adjust++;
		}
		if((selection[1][select] == start || selection[1][select] == 'T' || adjust > 1) &&
			(selection[2][select] == start || selection[2][select] == 'T' || adjust > 2) &&
			(selection[3][select] == start || selection[3][select] == 'T' || adjust > 3))
		{
			switch(start)
			{
			case 'X':
				return "X won";
				break;
			case 'O':
				return "O won";
				break;
			}
		}
	}

		char start = selection[0][0];
		int adjust = 1;
		while(start == 'T' && adjust < 4)
		{
			start = selection[adjust][adjust];
			adjust++;
		}
		if((selection[1][1] == start || selection[1][1] == 'T' || adjust > 1) &&
			(selection[2][2] == start || selection[2][2] == 'T' || adjust > 2) &&
			(selection[3][3] == start || selection[3][3] == 'T' || adjust > 3))
		{
			switch(start)
			{
			case 'X':
				return "X won";
				break;
			case 'O':
				return "O won";
				break;
			}
		}

		start = selection[0][3];
		adjust = 1;
		while(start == 'T' && adjust < 4)
		{
			start = selection[adjust-1][4-adjust];
			adjust++;
		}
		if((selection[1][2] == start || selection[1][2] == 'T' || adjust > 1) &&
			(selection[2][1] == start || selection[2][1] == 'T' || adjust > 2) &&
			(selection[3][0] == start || selection[3][0] == 'T' || adjust > 3))
		{
			switch(start)
			{
			case 'X':
				return "X won";
				break;
			case 'O':
				return "O won";
				break;
			}
		}

		for(int y = 0; y < 4; y++)
		{
			for(int x = 0; x < 4; x++)
			{
				if(selection[x][y] == '.')
				{
					return "Game has not completed";
				}
			}
		}
		return "Draw";
}