#include <iostream>
#include <cstdio>
using namespace std;

string slowo[ 10 ];

bool X_Won()
{
	int licznik = 0;
	for (int i = 1; i <= 4; i++) // sprawdzamy przekatna wychodzaca z lewego gornego rogu
		if( slowo[ i ][ i-1 ] == 'X' || slowo[ i ][ i-1 ] == 'T' )
			licznik++;
	if( licznik == 4 )
		return true;
	
	licznik = 0;
	for (int i = 1; i <= 4; i++) // sprawdzamy przekatna wychodzaca z prawego gornego rogu
		if( slowo[ i ][ 4-i ] == 'X' || slowo[ i ][ 4-i ] == 'T' )
			licznik++;
	if( licznik == 4 )
		return true;
	
	licznik = 0;
	for (int i = 1; i <= 4; i++) {
		for (int j = 0; j <= 3; j++) // sprawdzamy wierszami
			if( slowo[ i ][ j ] == 'X' || slowo[ i ][ j ] == 'T' )
				licznik++;
		if( licznik == 4 )
			return true;
		licznik = 0;
		for (int j = 0; j <= 3; j++) // sprawdzamy kolumnami
			if( slowo[ j+1 ][ i-1 ] == 'X' || slowo[ j+1 ][ i-1 ] == 'T' )
				licznik++;
		if( licznik == 4 )
			return true;
		licznik = 0;
	}
	
	return false;
}

bool O_Won()
{
	int licznik = 0;
	for (int i = 1; i <= 4; i++) // sprawdzamy przekatna wychodzaca z lewego gornego rogu
		if( slowo[ i ][ i-1 ] == 'O' || slowo[ i ][ i-1 ] == 'T' )
			licznik++;
	if( licznik == 4 )
		return true;
	
	licznik = 0;
	for (int i = 1; i <= 4; i++) // sprawdzamy przekatna wychodzaca z prawego gornego rogu
		if( slowo[ i ][ 4-i ] == 'O' || slowo[ i ][ 4-i ] == 'T' )
			licznik++;
	if( licznik == 4 )
		return true;
	
	licznik = 0;
	for (int i = 1; i <= 4; i++) { 
		for (int j = 0; j <= 3; j++) // sprawdzamy wierszami
			if( slowo[ i ][ j ] == 'O' || slowo[ i ][ j ] == 'T' )
				licznik++;
		if( licznik == 4 )
			return true;
		licznik = 0;
		for (int j = 0; j <= 3; j++) // sprawdzamy kolumnami
			if( slowo[ j+1 ][ i-1 ] == 'O' || slowo[ j+1 ][ i-1 ] == 'T' )
				licznik++;
		if( licznik == 4 )
			return true;
		licznik = 0;
	}
	
	return false;
}

bool WszystkieZajete()
{
	for (int i = 1; i <= 4; i++)
		for (int j = 0; j <= 3; j++)
			if( slowo[ i ][ j ] == '.' )
				return false;
	return true;
}

int main()
{
	ios_base::sync_with_stdio(0);
	int n = 0;
	cin >> n;
	
	for (int i = 1; i <= n; i++) { // przypadki testowe
		for (int j = 1; j <= 4; j++)
			cin >> slowo[ j ];
		if( X_Won() ) {
			cout << "Case #" << i << ": X won\n";
			continue;
		}
		if( O_Won() ) {
			cout << "Case #" << i << ": O won\n";
			continue;
		}
		if( WszystkieZajete() ) {
			cout << "Case #" << i << ": Draw\n";
			continue;
		}
		cout << "Case #" << i << ": Game has not completed\n";
	}
	return 0;
}