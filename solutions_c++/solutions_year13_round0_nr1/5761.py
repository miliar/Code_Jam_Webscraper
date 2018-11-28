	#include <iostream>

using namespace std;

char plansza[4][4];

int main()
{
	int t;
	int licznik_x = 0, licznik_o = 0;
	int licznik = 0;
	bool koniec = false;
	cin >> t;
	for (int k = 1; k <= t; k++)
	{
		koniec = false;
		licznik = 0;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				cin >> plansza[i][j];
				if (plansza[i][j] != '.')
					licznik++;
			}
		
		
		for (int i = 0; i < 4; i++)
		{
			licznik_x = 0;
			for (int j = 0; j < 4; j++)
				if (plansza[i][j] == 'X' || plansza[i][j] == 'T')
					licznik_x++;
			if (licznik_x == 4)
			{
				koniec = true;
				break;
			}
		}
		if (koniec == false)
		{
			for (int i = 0; i < 4; i++)
			{
				licznik_x = 0;
				for (int j = 0; j < 4; j++)
					if (plansza[j][i] == 'X' || plansza[i][j] == 'T')
						licznik_x++;
				if (licznik_x == 4)
				{
					koniec = true;
					break;
				}
			}
		}
		if (koniec == false)
		{
			if (((plansza[0][0] == 'T' || plansza[0][0] == 'X') &&
				 (plansza[1][1] == 'T' || plansza[1][1] == 'X') &&
				 (plansza[2][2] == 'T' || plansza[2][2] == 'X') &&
				 (plansza[3][3] == 'T' || plansza[3][3] == 'X')) ||
				 ((plansza[0][3] == 'T' || plansza[0][3] == 'X') &&
				 (plansza[1][2] == 'T' || plansza[1][2] == 'X') &&
				 (plansza[2][1] == 'T' || plansza[2][1] == 'X') &&
				 (plansza[3][0] == 'T' || plansza[3][0] == 'X')))
				 {
				 	licznik_x = 4;
				 	koniec = true;
				 }
		}
		if (koniec == false)
		{
			for (int i = 0; i < 4; i++)
			{
				licznik_o = 0;
				for (int j = 0; j < 4; j++)
					if (plansza[i][j] == 'O' || plansza[i][j] == 'T')
						licznik_o++;
				if (licznik_o == 4)
				{
					koniec = true;
					break;
				}
			}
		}
		if (koniec == false)
		{
			for (int i = 0; i < 4; i++)
			{
				licznik_o = 0;
				for (int j = 0; j < 4; j++)
					if (plansza[j][i] == 'O' || plansza[i][j] == 'T')
						licznik_o++;
				if (licznik_o == 4)
				{
					koniec = true;
					break;
				}
			}
		}
		if (koniec == false)
		{
			if (((plansza[0][0] == 'O' || plansza[0][0] == 'T') &&
				 (plansza[1][1] == 'O' || plansza[1][1] == 'T') &&
				 (plansza[2][2] == 'O' || plansza[2][2] == 'T') &&
				 (plansza[3][3] == 'O' || plansza[3][3] == 'T')) ||
				 ((plansza[0][3] == 'O' || plansza[0][3] == 'T') &&
				 (plansza[1][2] == 'O' || plansza[1][2] == 'T') &&
				 (plansza[2][1] == 'O' || plansza[2][1] == 'T') &&
				 (plansza[3][0] == 'O' || plansza[3][0] == 'T')))
				 {
				 	licznik_o = 4;
				 	koniec = true;
				 }
		}
		cout << "Case #" << k;
		if (licznik_o == 4)
			cout << ": O won";	
		else if (licznik_x == 4)
			cout << ": X won";
		else if (licznik == 16)
			cout << ": Draw";
		else
			cout << ": Game has not completed";
		cout << endl;
			
	}
	return 0;
}	
