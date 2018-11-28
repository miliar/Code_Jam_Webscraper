#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <deque>
#include <cctype>
#include <list>
#include <queue>
#include <map>
#include <cmath>
#include <algorithm>
#include <vector>
#include <fstream>

using namespace std;

int t;
char s[4][4];

bool win(char c) {
	for ( int i = 0 ; i < 4 ; ++i ) {
		int x_c = 0;
		bool t_f = false;

		for ( int j = 0 ; j < 4 ; ++j )
			if ( s[i][j] == c )
				++x_c;
			else if ( s[i][j] == 'T' )
				t_f = true;

		if ( x_c == 4 || (x_c == 3 && t_f) )
			return true;

		x_c = 0, t_f = false;

		for ( int j = 0 ; j < 4 ; ++j )
			if ( s[j][i] == c )
				++x_c;
			else if ( s[j][i] == 'T' )
				t_f = true;

		if ( x_c == 4 || (x_c == 3 && t_f) )
			return true;
	}

	int x_c = 0;
	bool t_f = false;

	for ( int i = 0 ; i < 4 ; ++i )
		if ( s[i][i] == c )
			++x_c;
		else if ( s[i][i] == 'T' )
			t_f = true;

	if ( x_c == 4 || (x_c == 3 && t_f) )
			return true;

	x_c = 0;
	t_f = false;

	for ( int i = 0 ; i < 4 ; ++i )
		if ( s[3 - i][i] == c )
			++x_c;
		else if ( s[3 - i][i] == 'T' )
			t_f = true;

	if ( x_c == 4 || (x_c == 3 && t_f) )
			return true;

	return false;
}

bool end() {
	for ( int i = 0 ; i < 4 ; ++i )
		for ( int j = 0 ; j < 4 ; ++j )
			if ( s[i][j] == '.' )
				return false;
	return true;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif

	scanf("%d\n", &t);
	for ( int i = 0 ; i < t ; ++i ) {
		
		for ( int a = 0 ; a < 4 ; ++a )
			for ( int b = 0 ; b < 4 ; ++b ) {
				s[a][b] = getchar();
				if ( s[a][b] == '\n' )
					s[a][b] = getchar();
			}
		getchar();

		printf("Case #%d: ", i + 1);

		if ( win('X') )
			printf("X won\n");
		else if ( win('O') )
			printf("O won\n");
		else {

			if ( end() )
				printf("Draw\n");
			else
				printf("Game has not completed\n");

		}
	}

	return 0;
}