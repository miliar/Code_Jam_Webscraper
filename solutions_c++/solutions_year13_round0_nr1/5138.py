#include<iostream>
#include<fstream>
#include<vector>
#include<map>
#include<string>

#define DRAW 0x00
#define CIRCLE 0x01
#define CROSS 0x02
#define UNKNOWN 0x03

//#define USE_STDIN

using namespace std;

bool isNoSpace( int board )
{
	int mask = 0x3;
	for( int i=0; i<16; i++ ){
		if( (mask & board) == 0 ) return false;
		mask <<= 2;
	}

	return true;
}

int main()
{

#ifdef USE_STDIN
	istream& in = cin;
#else
	ifstream infile;
	infile.open ("A-large.in", ifstream::in);
	istream& in = infile;
#endif

	ofstream outfile;
	outfile.open("A-large.out", ofstream::out);

//XXXT
//....
//OO..
//....

	//00 . empty
	//01 O
	//10 X
	//11 T

	int line[3][10];

	line[CIRCLE][0] = CIRCLE | CIRCLE << 2 | CIRCLE << 4 | CIRCLE << 6;
	line[CIRCLE][1] = CIRCLE << 8 | CIRCLE << 10 | CIRCLE << 12 | CIRCLE << 14;
	line[CIRCLE][2] = CIRCLE << 16| CIRCLE << 18 | CIRCLE << 20 | CIRCLE << 22;
	line[CIRCLE][3] = CIRCLE << 24| CIRCLE << 26 | CIRCLE << 28 | CIRCLE << 30;

	line[CIRCLE][4] = CIRCLE | CIRCLE << 8 | CIRCLE << 16 | CIRCLE << 24;
	line[CIRCLE][5] = CIRCLE << 2 | CIRCLE << 10 | CIRCLE << 18 | CIRCLE << 26;
	line[CIRCLE][6] = CIRCLE << 4| CIRCLE << 12 | CIRCLE << 20 | CIRCLE << 28;
	line[CIRCLE][7] = CIRCLE << 6| CIRCLE << 14 | CIRCLE << 22 | CIRCLE << 30;

	line[CIRCLE][8] = CIRCLE | CIRCLE << 10 | CIRCLE << 20 | CIRCLE << 30;
	line[CIRCLE][9] = CIRCLE << 6 | CIRCLE << 12 | CIRCLE << 18 | CIRCLE << 24;



	line[CROSS][0] = CROSS | CROSS << 2 | CROSS << 4 | CROSS << 6;
	line[CROSS][1] = CROSS << 8 | CROSS << 10 | CROSS << 12 | CROSS << 14;
	line[CROSS][2] = CROSS << 16| CROSS << 18 | CROSS << 20 | CROSS << 22;
	line[CROSS][3] = CROSS << 24| CROSS << 26 | CROSS << 28 | CROSS << 30;

	line[CROSS][4] = CROSS | CROSS << 8 | CROSS << 16 | CROSS << 24;
	line[CROSS][5] = CROSS << 2 | CROSS << 10 | CROSS << 18 | CROSS << 26;
	line[CROSS][6] = CROSS << 4| CROSS << 12 | CROSS << 20 | CROSS << 28;
	line[CROSS][7] = CROSS << 6| CROSS << 14 | CROSS << 22 | CROSS << 30;

	line[CROSS][8] = CROSS | CROSS << 10 | CROSS << 20 | CROSS << 30;
	line[CROSS][9] = CROSS << 6 | CROSS << 12 | CROSS << 18 | CROSS << 24;

    int T;
	in >> T;

	for( int i=0; i<T; i++ ){
		
		int board = 0x0;

		for( int row=0; row<4; row++ ){
			for( int col=0; col<4; col++ ){
			
				char grid;
				int surge = 0x0;
				in >> grid;
				switch( grid ){
					case '.':
						surge = 0x0;
						break;
					case 'O':
						surge = 0x1;
						break;
					case 'X':
						surge = 0x2;
						break;
					case 'T':
						surge = 0x3;
						break;
					default:
						outfile << "error: unknown text";
						exit(0);
				}

				board |= ( surge << (col+row*4)*2 );
			}
		}
		
		int result = UNKNOWN;

		for( int j=0; j<10; j++ ){
			if( (board & line[CIRCLE][j]) == line[CIRCLE][j] ){
				result = CIRCLE;
				break;
			} else if( (board & line[CROSS][j]) == line[CROSS][j] ){
				result = CROSS;
				break;
			}
		}

		if( result == UNKNOWN && isNoSpace(board) ) result = DRAW;

//Case #1: X won
//Case #2: Draw
//Case #3: Game has not completed
//Case #4: O won
//Case #5: O won
//Case #6: O won

		outfile << "Case #" << i+1 << ": ";
		switch( result ){
			case DRAW:
				outfile << "Draw";
				break;
			case UNKNOWN:
				outfile << "Game has not completed";
				break;
			case CIRCLE:
				outfile << "O won";
				break;
			case CROSS:
				outfile << "X won";
				break;
			default:
				outfile << "error: unknown result";
				exit(0);
		}
		outfile << endl;
	}
	
#ifdef USE_STDIN

#else
	infile.close();
#endif
	outfile.close();
}