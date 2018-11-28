#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream in("E:\\input4.txt");
	ofstream out("E:\\output.txt");
	int total;
	in>>total;

	int XWon1 = 'X' + 'X' + 'X' + 'X';
	int XWon2 = 'X' + 'X' + 'X' + 'T';
	int OWon1 = 'O' + 'O' + 'O' + 'O';
	int OWon2 = 'O' + 'O' + 'O' + 'T';


	for(int i=0; i<total; i++)
	{
		bool finished = false;
		bool draw = true;

		char p[4][4];
		for(int j=0; j<4; j++)
		{
			for(int k=0; k<4; k++)
			{
				in>>p[j][k];
			}
		}

		int diag1 = p[0][0] + p[1][1] + p[2][2] + p[3][3];
		int diag2 = p[0][3] + p[1][2] + p[2][1] + p[3][0];
		
		if(diag1 == XWon1 || diag1 == XWon2 || diag2 == XWon1 || diag2 == XWon2)
		{
			out<<"Case #"<<i+1<<": X won"<<endl;
			continue;
		}
		else if(diag1 == OWon1 || diag1 == OWon2 || diag2 == OWon1 || diag2 == OWon2)
		{
			out<<"Case #"<<i+1<<": O won"<<endl;
			continue;
		}
		else
		{
			for(int j=0; j<4; j++)
			{
				int column=0, row=0;
				for(int k=0; k<4; k++)
				{
					row += p[j][k];
					column += p[k][j];
				}
				if(column == XWon1 || column == XWon2 || row == XWon1 || row == XWon2)
				{
					out<<"Case #"<<i+1<<": X won"<<endl;
					finished = true;
					break;
				}
				else if(column == OWon1 || column == OWon2 || row == OWon1 || row == OWon2)
				{
					out<<"Case #"<<i+1<<": O won"<<endl;
					finished = true;
					break;
				}
			}
			if(finished == false)
			{
				for(int j=0; j<4; j++)
				{
					for(int k=0; k<4; k++)
					{
						if (p[j][k]=='.')
						{
							draw = false;
						}
					}
				}
				if(draw == true)
				{
					out<<"Case #"<<i+1<<": Draw"<<endl;
				}
				else
				{
					out<<"Case #"<<i+1<<": Game has not completed"<<endl;
				}
			}
			
		}



		

	}
	return 0;
}