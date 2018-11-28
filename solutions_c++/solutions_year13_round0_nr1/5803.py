#include <iostream>
#include <fstream>
using namespace std;
ofstream fo("haha.out");
int main () {
	int T;
	int t, i, j;
	int count_row_x[4], count_column_x[4];
	int count_row_o[4], count_column_o[4];
	int count_cross_x, count_cross_o;
	int count_across_x, count_across_o;
	bool dot;
	char c, winner;
	
	cin >> T;
	
	for ( t = 1 ; t <= T ; ++ t ) {
		
		for ( i = 0 ; i < 4 ; ++ i ) {
			count_row_x[i] = count_column_x[i] = 0;
			count_row_o[i] = count_column_o[i] = 0;
		}
		count_cross_x = count_cross_o = 0;
		count_across_x = count_across_o = 0;
		
		dot = false;
		winner = ' ';
			
		for ( i = 0 ; i < 4 ; ++ i ) {
			for ( j = 0 ; j < 4 ; ++ j ) {
				cin >> c;
				switch (c) {
				case 'T':
					++count_row_o[i];
					++count_column_o[j];
					++count_row_x[i];
					++count_column_x[j];
					if ( i==j ) {
						++count_cross_x;
						++count_cross_o;
					} else if ( i+j==3 ) {
						++count_across_x;
						++count_across_o;
					}
					break;
				case 'O':
					++count_row_o[i];
					++count_column_o[j];
					if ( i==j )	++count_cross_o;
					else if ( i+j==3 ) ++count_across_o;
					break;
				case 'X':
					++count_row_x[i];
					++count_column_x[j];
					if ( i==j )	++count_cross_x;
					else if ( i+j==3 ) ++count_across_x;
					break;
				case '.':
					dot = true;
					break;
				}
			}
		}
		cout << "Case #" << t << ": ";
		if ( count_cross_o == 4 || count_across_o == 4 ) {
			winner = 'O';
		}
		if ( count_cross_x == 4 || count_across_x == 4) {
			winner = 'X';
		}
		if ( winner == ' ' ) {
			for ( i = 0 ; i < 4 ; ++ i ) {
				if ( count_row_o[i]==4 || count_column_o[i]==4 ) {
					winner = 'O';
					break;
				}
				if ( count_row_x[i]==4 || count_column_x[i]==4 ) {
					winner = 'X';
					break;
				}
			}
		}
		if ( winner == ' ' ) {
			if ( dot == false ) {
				cout << "Draw" << endl;	
			} else cout << "Game has not completed" << endl;
		} else cout << winner << " won" << endl;
	}
	return 0;
}
