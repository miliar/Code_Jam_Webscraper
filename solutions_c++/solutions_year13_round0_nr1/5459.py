#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

bool check(string *plansza, char znak)
{
    for(int i = 0; i < 4; i++)
	{
		bool line = true;
		for(int j = 0; j < 4; j++)
			if(plansza[i][j] != 'T' && plansza[i][j] != znak)
				line = false;
		if(line)
			return true;
	}
	
	for(int i = 0; i < 4; i++)
	{
		bool line = true;
		for(int j = 0; j < 4; j++)
			if(plansza[j][i] != 'T' && plansza[j][i] != znak)
				line = false;
		if(line)
			return true;
	}

	
	{
		bool line = true;
		for(int j = 0; j < 4; j++)
			if(plansza[j][j] != 'T' && plansza[j][j] != znak)
				line = false;
		if(line)
			return true;
	}

	{
		bool line = true;
		for(int j = 0; j < 4; j++)
			if(plansza[j][3 - j] != 'T' && plansza[j][3 - j] != znak)
				line = false;
		if(line)
			return true;
	}

	return false;
}

int main()
{
	int t;
	cin >> t;

	for(int s = 0; s < t; s++)
	{
		string *plansza = new string[4];
		for(int i = 0; i < 4; i++)
			cin >> plansza[i];
		
		int k = 0;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				if(plansza[i][j] == '.')
					k++;

		if(check(plansza, 'X'))
			printf("Case #%d: X won\n", s + 1);
		else if(check(plansza, 'O'))
			printf("Case #%d: O won\n", s + 1);
		else if(k == 0)
			printf("Case #%d: Draw\n", s + 1);
		else
			printf("Case #%d: Game has not completed\n", s + 1);

		//cin >> plansza[0];
		delete[] plansza;
	}

	return 0;
}