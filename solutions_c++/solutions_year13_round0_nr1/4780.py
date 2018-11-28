#include <iostream>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

vector<string> tablero;

char checa()
{

	int O=0, X=0;

	for(int j=0; j<4; ++j)
	{
		O=0; X=0;
		for(int i=0; i<4; ++i)
		{
			if(tablero[i][j] == 'O')
			{
				O++;
			}
			else if(tablero[i][j] == 'X')
			{
				X++;
			}
			else if(tablero[i][j] == 'T')
			{
				++X; ++O;
			}
		}
		if (O==4)
			return 'O';
		if(X==4)
			return 'X';
	}
	for(int i=0; i<4; ++i)
	{
		O=0; X=0;
		for(int j=0; j<4; ++j)
		{
			if(tablero[i][j] == 'O' )
			{
				O++;
			}
			else if(tablero[i][j] == 'X')
			{
				X++;
			}
			else if(tablero[i][j] == 'T')
			{
				++X; ++O;
			}
		}
		if (O==4)
			return 'O';
		if(X==4)
			return 'X';
	}
	O=0; X=0;

	for(int j=0; j<4; ++j)
	{
		if(tablero[j][j] == 'O')
		{
			O++;
		}
		else if(tablero[j][j] == 'X')
		{
			X++;
		}
		else if(tablero[j][j] == 'T')
		{
			++X; ++O;
		}
	}
	if (O==4)
		return 'O';
	if(X==4)
		return 'X';

	O=0; X=0;
	for(int j=0; j<4; ++j)
	{
		if(tablero[j][3-j] == 'O' )
		{
			O++;
		}
		else if(tablero[j][3-j] == 'X' )
		{
			X++;
		}
		else if(tablero[j][3-j] == 'T')
		{
			++X; ++O;
		}
	}
	if (O==4)
		return 'O';
	if(X==4)
		return 'X';


	
	return 'D';

}

void solve(int iteracion)
{
	bool completed = true;

	tablero.assign( 4, string("....") );
	cin >> tablero[0];
	cin >> tablero[1];
	cin >> tablero[2];
	cin >> tablero[3];

	for(int i=0; i < 4; ++i)
	{
		for (int j = 0; j < 4 ; ++j)
		{
			if(tablero[i][j] == '.')
				completed = false;
		}
	}

	char status = checa();

	if (status == 'O')
		printf("Case #%d: O won\n", iteracion);
	else if (status == 'X')
		printf("Case #%d: X won\n", iteracion);
	else if (status == 'D' and completed == true)
		printf("Case #%d: Draw\n", iteracion);
	else
		printf("Case #%d: Game has not completed\n", iteracion);

}


int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("Tic-Tac-Toe-Tomek.out", "w", stdout);
	int casos = 0;
	scanf("%d\n", &casos);
	for(int i=0; i<casos; ++i)
	{
		solve(i+1);
	}

	return 0;
}