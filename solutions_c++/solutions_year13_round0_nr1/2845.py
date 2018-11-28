#include <iostream>

using namespace std;

int main()
{
	int n;
	char table[4][4];
	cin >> n;
	int count = 0;
	while(count < n)
	{
		count++;
		int ganhou = 0;//0 empatou, 1 X ganhou, 2 O ganhou, 3 ainda tem jogo
		int saw = 0;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				cin >> table[i][j];
		for(int i = 0; i < 4; i++)
		{
			int numX = 0, numO = 0, numT = 0;
			for(int j = 0; j < 4; j++)
			{
				if(table[i][j] == 'X')
					numX++;
				else if(table[i][j] == 'O')
					numO++;
				else if(table[i][j] == 'T')
					numT++;
				else if(table[i][j] == '.')
					saw++;
			}
			if(numX + numT == 4)
				ganhou = 1;
			else if(numO + numT == 4)
				ganhou = 2;
		}
		for(int i = 0; i < 4; i++)
		{
			int numX = 0, numO = 0, numT = 0;
			for(int j = 0; j < 4; j++)
			{
				if(table[j][i] == 'X')
					numX++;
				else if(table[j][i] == 'O')
					numO++;
				else if(table[j][i] == 'T')
					numT++;
				else if(table[j][i] == '.')
					saw++;
			}
			if(numX + numT == 4)
				ganhou = 1;
			else if(numO + numT == 4)
				ganhou = 2;
		}
		int numX = 0, numO = 0, numT = 0;
		for(int i = 0; i < 4; i++)
		{

			if(table[i][i] == 'X')
				numX++;
			else if(table[i][i] == 'O')
				numO++;
			else if(table[i][i] == 'T')
				numT++;
			else if(table[i][i] == '.')
				saw++;
		}
		if(numX + numT == 4)
			ganhou = 1;
		else if(numO + numT == 4)
			ganhou = 2;
		numX = 0;
		numO = 0;
		numT = 0;
		for(int i = 0; i < 4; i++)
		{
			if(table[i][3 - i] == 'X')
				numX++;
			else if(table[i][3 - i] == 'O')
				numO++;
			else if(table[i][3 - i] == 'T')
				numT++;
			else if(table[i][3 - i] == '.')
				saw++;
			if(numX + numT == 4)
				ganhou = 1;
			else if(numO + numT == 4)
				ganhou = 2;
		}

		if(numX + numT == 4)
			ganhou = 1;
		else if(numO + numT == 4)
			ganhou = 2;

		if(ganhou == 1)
			cout << "Case #"<<count<<": X won";
		else if(ganhou == 2)
			cout << "Case #"<<count<<": O won";
		else if(ganhou == 0 && saw == 0)
			cout << "Case #"<<count<<": Draw";
		else if(ganhou == 0 && saw > 0)
			cout << "Case #"<<count<<": Game has not completed";
		cout << endl;

	}
	return 0;
}
