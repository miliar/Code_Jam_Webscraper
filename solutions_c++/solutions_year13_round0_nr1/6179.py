#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>

std::ifstream input;
std::ofstream output;

char specSymbol = 'T';
char* line1;
char* line2;
char* line3;
char* line4;

inline bool CheckNothing(char* line, int index)
{
	return line[index] == '.';
}

inline bool CheckSymbol(char* line, int index, char& player)
{
	return line[index] == player || line[index] == specSymbol;
}
inline bool CheckLine(char* line,char& player)
{
	return	CheckSymbol(line,0,player) &&
			CheckSymbol(line,1,player) &&
			CheckSymbol(line,2,player) &&
			CheckSymbol(line,3,player);
}

inline bool CheckAllRows(char player)
{
	if(CheckLine(line1,player))
		return true;
	if(CheckLine(line2,player))
		return true;
	if(CheckLine(line3,player))
		return true;
	if(CheckLine(line4,player))
		return true;
}

inline bool CheckAllColumns(char player)
{
	//Column 1
	if(	CheckSymbol(line1,0,player) &&
		CheckSymbol(line2,0,player) &&
		CheckSymbol(line3,0,player) &&
		CheckSymbol(line4,0,player))
		return true;
	//Column 2
	if(	CheckSymbol(line1,1,player) &&
		CheckSymbol(line2,1,player) &&
		CheckSymbol(line3,1,player) &&
		CheckSymbol(line4,1,player))
		return true;
	//Column 3
	if(	CheckSymbol(line1,2,player) &&
		CheckSymbol(line2,2,player) &&
		CheckSymbol(line3,2,player) &&
		CheckSymbol(line4,2,player))
		return true;
	//Column 4
	if(	CheckSymbol(line1,3,player) &&
		CheckSymbol(line2,3,player) &&
		CheckSymbol(line3,3,player) &&
		CheckSymbol(line4,3,player))
		return true;
	return false;
}

inline bool CheckAllDiagonali(char player)
{
	// Diagonal -1,1 -- 1,-1 
	if(	CheckSymbol(line1,0,player) &&
		CheckSymbol(line2,1,player) &&
		CheckSymbol(line3,2,player) &&
		CheckSymbol(line4,3,player))
		return true;

	// Diagonal -1,-1 -- 1,1 
	if(	CheckSymbol(line1,3,player) &&
		CheckSymbol(line2,2,player) &&
		CheckSymbol(line3,1,player) &&
		CheckSymbol(line4,0,player))
		return true;
	return false;
}
inline bool CheckXWon()
{
	if(CheckAllRows('X'))
		return true;
	if(CheckAllColumns('X'))
		return true;
	if(CheckAllDiagonali('X'))
		return true;
	return false;
}

inline bool CheckOWon()
{
	if(CheckAllRows('O'))
		return true;
	if(CheckAllColumns('O'))
		return true;
	if(CheckAllDiagonali('O'))
		return true;
	return false;
}

inline bool CheckNullField()
{
	if(line1[0] == '.' || line1[1] == '.'  || line1[2] == '.'  || line1[3] == '.' )
		return false;
	if(line2[0] == '.' || line2[1] == '.'  || line2[2] == '.'  || line2[3] == '.' )
		return false;
	if(line3[0] == '.' || line3[1] == '.'  || line3[2] == '.'  || line3[3] == '.' )
		return false;
	if(line4[0] == '.' || line4[1] == '.'  || line4[2] == '.'  || line4[3] == '.' )
		return false;
	return true;
}

int main()
{
	input.open("task.in");
	output.open("taskResult.out");
	int countCases;
	input >> countCases;
	printf("%d\n",countCases);
	
	line1 = (char*)::malloc(sizeof(char)*4);
	line2 = (char*)::malloc(sizeof(char)*4);
	line3 = (char*)::malloc(sizeof(char)*4);
	line4 = (char*)::malloc(sizeof(char)*4);

	for(int i=0; i < countCases; i++)
	{
		input >> line1;
		input >> line2;
		input >> line3;
		input >> line4;

		if(CheckXWon())
			output << "Case #" << i + 1 << ": X won\n";
		else
		{
			if(CheckOWon())
				output << "Case #" << i + 1 << ": O won\n";
			else
			{
				if(CheckNullField())
					output << "Case #" << i + 1 << ": Draw\n";
				else
					output << "Case #" << i + 1 << ": Game has not completed\n";
			}
		}
	}

	input.close();
	output.flush();
	output.close();
   return 0;
}