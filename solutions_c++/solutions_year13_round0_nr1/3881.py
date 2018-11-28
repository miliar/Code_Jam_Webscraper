#include <fstream>
#include <string>

using namespace std;

char cInput[4][4];
int iCaseNo = 0;
ifstream fin ("C:/Users/SHERMAL/Desktop/A-large.in");
ofstream fout ("C:/Users/SHERMAL/Desktop/out.txt");
  

bool ExamineRows();
bool ExamineCols();
bool ExamineDiag1();
bool ExamineDiag2();
void init();

int main(int argc, char* argv[])
{
	
	if (fin.is_open())
	{
		init();

		fin.close();
	}

	fout.close();

	return 0;
}

void init(){
	int iNo;
	bool bIsEmpty;
	bool bIsWin;

	fin >> iNo;

	while(iNo > 0)
	{
		bIsEmpty = false;

		--iNo;
		++iCaseNo;

		//inputs
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				fin >> cInput[i][j];
			}
		}

		bIsWin = ExamineRows();

		if ( !bIsWin )
		{
			bIsWin = ExamineCols();

			if ( !bIsWin )
			{
				bIsWin = ExamineDiag1();

				if ( !bIsWin )
				{
					bIsWin = ExamineDiag2();

				}
			}
		}

		if ( !bIsWin ){
			for (int i = 0; i < 4 && !bIsEmpty; i++)
			{
				for (int j = 0; j < 4; j++)
				{
					if (cInput[i][j] == '.')
					{
						bIsEmpty = true;
						break;
					}

				}
			}

			if ( bIsEmpty )
			{
				fout << "Case #" << iCaseNo << ": " << "Game has not completed" << endl;
			}
			else
			{
				fout << "Case #" << iCaseNo << ": " << "Draw" << endl;
			}
		}

	}

}

bool ExamineRows()
{
	for (int i = 0; i < 4; i++)
	{
		char cSym;

		if (cInput[i][0] == '.')
		{
			continue;
		}
		else if (cInput[i][0] == 'T')
		{
			if (cInput[i][1] == '.')
			{
				continue;
			}
			else
			{
				cSym = cInput[i][1];
			}
		}
		else
		{
			cSym = cInput[i][0];
		}

		for (int j = 1; j < 4; j++)
		{
		
			if (cInput[i][j] != cSym && cInput[i][j] != 'T')
			{
				break;
			}
			else if (j == 3)
			{
				fout << "Case #" << iCaseNo << ": " << cSym << " won" << endl;
				return true;
			}
		}

	}

	return false;
}

bool ExamineCols()
{
	for (int i = 0; i < 4; i++)
	{
		char cSym;

		if (cInput[0][i] == '.')
		{
			continue;
		}
		else if (cInput[0][i] == 'T')
		{
			if (cInput[1][i] == '.')
			{
				continue;
			}
			else
			{
				cSym = cInput[1][i];
			}
		}
		else
		{
			cSym = cInput[0][i];
		}

		for (int j = 1; j < 4; j++)
		{

			if (cInput[j][i] != cSym && cInput[j][i] != 'T')
			{
				break;
			}
			else if (j == 3)
			{
				fout << "Case #" << iCaseNo << ": " << cSym << " won" << endl;
				return true;
			}
		}

	}

	return false;
}

bool ExamineDiag1()
{
	char cSym;

	if (cInput[0][0] == '.')
	{
		return false;
	}
	else if (cInput[0][0] == 'T')
	{
		if (cInput[1][1] == '.')
		{
			return false;
		}
		else
		{
			cSym = cInput[1][1];
		}
	}
	else
	{
		cSym = cInput[0][0];
	}

	for (int i = 1; i < 4; i++)
	{
		if (cInput[i][i] != cSym && cInput[i][i] != 'T')
		{
			return false;
		}
		else if (i == 3)
		{
			fout << "Case #" << iCaseNo << ": " << cSym << " won" << endl;
			return true;
		}
	}
}

bool ExamineDiag2()
{
	char cSym;

	if (cInput[0][3] == '.')
	{
		return false;
	}
	else if (cInput[0][3] == 'T')
	{
		if (cInput[1][2] == '.')
		{
			return false;
		}
		else
		{
			cSym = cInput[1][2];
		}
	}
	else
	{
		cSym = cInput[0][3];
	}

	for (int i = 1; i < 4; i++)
	{
		if (cInput[i][3-i] != cSym && cInput[i][3-i] != 'T')
		{
			return false;
		}
		else if (i == 3)
		{
			fout << "Case #" << iCaseNo << ": " << cSym << " won" << endl;
			return true;
		}
	}
}
