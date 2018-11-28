#include <iostream>
#include <fstream>
#include <vector>


using namespace std;

int main() {

	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int T;

	fin >> T;

	for (int i = 0; i < T; ++i)
	{
		vector<vector<char>> field;
		vector<char> tmpV;
		field.push_back(tmpV);
		field.push_back(tmpV);
		field.push_back(tmpV);
		field.push_back(tmpV);
		char tmp;

		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				fin >> tmp;
				field[j].push_back(tmp);
			}
		}

		//обработка

		int result = 0; //0 - не завершена, 1 - ничья, 2 - победа О, 3 - победа Х

		//проверка вертикалей
		
		for (int j = 0; j < 4; ++j)
		{
			bool tFound = false;
			int column = 0;
			for (int k = 0; k < 4; ++k)
			{
				if (field[j][k] == 'O')
					column++;
				else if (field[j][k] == 'X')
					column--;
				else if (field[j][k] == 'T')
					tFound = true;
			}

			if (tFound && column != 0)
			{
				column += abs(column)/column;
			}

			if (column == 4)
			{
				result = 2;
				break;
			}
			else if (column == -4)
			{
				result = 3;
				break;
			}
		}

		for (int j = 0; j < 4; ++j) //проверка горизонталей
		{
			int line = 0;
			bool tFound = false;

			for (int k = 0; k < 4; ++k)
			{
				if (field[k][j] == 'O')
					line++;
				else if (field[k][j] == 'X')
					line--;
				else if (field[j][k] == 'T')
					tFound = true;
			}
			if (tFound && line != 0)
			{
				line += abs(line)/line;
			}
			if (line == 4)
			{
				result = 2;
				break;
			}
			else if (line == -4)
			{
				result = 3;
				break;
			}
		}

		//проверка диагоналей

		int diag = 0;
		
		bool tFound = false;
		for (int j = 0; j < 4; ++j)
		{
			if (field[j][j] == 'O')
					diag++;
			else if (field[j][j] == 'X')
				diag--;
			else if (field[j][j] == 'T')
				tFound = true;
		}
		if (tFound && diag != 0)
		{
			diag += abs(diag)/diag;
		}
		if (diag == 4)
		{
			result = 2;
		}
		else if (diag == -4)
		{
			result = 3;
		}

		diag = 0;
		tFound = false;
		for (int j = 0; j < 4; ++j)
		{
			if (field[3 - j][j] == 'O')
					diag++;
			else if (field[3 - j][j] == 'X')
				diag--;
			else if (field[3 - j][j] == 'T')
				tFound = true;
		}
		if (tFound && diag != 0)
		{
			diag += abs(diag)/diag;
		}
		if (diag == 4)
		{
			result = 2;
		}
		else if (diag == -4)
		{
			result = 3;
		}

		//проверка на завершенность

		if (result < 2)
		{
			int counter = 0;
			for (int j = 0; j < 4; ++j)
			{
				for (int k = 0; k < 4; ++k)
				{
					if (field[j][k] != '.')
						counter++;
				}
			}
			if (counter == 16)
			{
				result = 1;
			}
		}

		switch (result)
		{
		case 0:
			fout << "Case #" << i + 1 << ": Game has not completed" << endl; 
			break;
		case 1:
			fout << "Case #" << i + 1 << ": Draw" << endl; 
			break;
		case 2:
			fout << "Case #" << i + 1 << ": O won" << endl; 
			break;
		case 3:
			fout << "Case #" << i + 1 << ": X won" << endl; 
			break;
		}
	}

	fin.close();
	fout.close();

	return 0;
}