#include <fstream>
#include <iostream>

using namespace std;

char Win(char *line);

int main()
{
	int T, dots;
	bool win;
	fstream in("A-large.in", ios::in);
	fstream out("out.out", ios::out);

	char **board = new char*[4];
	for (int i = 0; i < 4; i++)
		board[i] = new char[4];
	char *line = new char[4];

	in >> T;

	for (int k = 0; k < T; k++)
	{
		win = false;
		dots = 0;

		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				in >> board[i][j];
				if (board[i][j] == '.')
					dots++;
			}
		}

		for (int i = 0; i < 4; i++)
			if (Win(board[i]) != 'N')
			{
				out << "Case #" << k+1 << ": "<< Win(board[i]) <<" won"<<endl;
				win = true;
			}
		if (win)
			continue;

		for (int j = 0; j < 4; j++)
		{
			for (int i = 0; i < 4; i++)
				line[i] = board[i][j];
			
			if (Win(line) != 'N')
			{
				out << "Case #" << k+1 << ": "<< Win(line) <<" won"<<endl;
				win = true;
			}
		}

		if (win)
			continue;

		for (int i = 0; i < 4; i++)
			line[i] = board[i][i];

		if (Win(line) != 'N')
			{
				out << "Case #" << k+1 << ": "<< Win(line) <<" won"<<endl;
				win = true;
			}

		if (win)
			continue;

		int q = 0;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
				if (i + j == 3)
				{
					line[q] = board[i][j];
					q++;
				}
		}

		if (Win(line) != 'N')
			{
				out << "Case #" << k+1 << ": "<< Win(line) <<" won"<<endl;
				win = true;
			}

		if (win)
			continue;

		if (dots == 0)
			out << "Case #" << k+1 << ": Draw" << endl;
		else
			out << "Case #" << k+1 << ": Game has not completed" << endl;

	}


	in.close();
	out.close();

	system("pause");

	return 0;
}

char Win (char *line)
{
	int Tpos = -1;
	for (int i = 0; i < 4; i++)
		if (line[i] == 'T')
			Tpos = i;

	if (Tpos != -1)
	{
		int Oquant = 0;
		int Xquant = 0;

		for (int i = 0; i < 4; i++)
			if (line[i] == 'O')
				Oquant++;
			else if(line[i] == 'X')
				Xquant++;

		if (Oquant == 3)
			return 'O';
		if (Xquant == 3)
			return 'X';
		return 'N';
	}

	else
	{
		int Oquant = 0;
		int Xquant = 0;

		for (int i = 0; i < 4; i++)
			if (line[i] == 'O')
				Oquant++;
			else if(line[i] == 'X')
				Xquant++;

		if (Xquant == 4)  
			return 'X';
		if (Oquant == 4)
			return 'O';
		
		return 'N';
	}

}