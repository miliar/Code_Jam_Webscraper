#include <string.h>
#include <iostream>
#define MAX_LENGTH 9999
using namespace std;

char board[4][4]; // y, x

char get_winner() // 'O', 'X', 'D':Draw, 'N':Game has not completed
{
	bool exist_blank = false;
	for ( int yloop=0; yloop<4 && !exist_blank; yloop++ )
	for ( int xloop=0; xloop<4 && !exist_blank; xloop++ )
		if ( board[yloop][xloop] == '.' ) exist_blank = true;

	// horizontal check
	for ( int yloop=0; yloop<4; yloop++ )
	for ( int xloop=0; xloop<4; xloop++ )
	{
		if ( board[yloop][xloop] == '.' ) break;
		char tmp = board[yloop][0] != 'T' ? board[yloop][0] : board[yloop][1]; 
		if ( xloop && board[yloop][xloop] != 'T' && tmp != board[yloop][xloop] ) break;
		if ( xloop == 3 ) return tmp;
	}

	// vertical check
	for ( int xloop=0; xloop<4; xloop++ )
	for ( int yloop=0; yloop<4; yloop++ )
	{
		if ( board[yloop][xloop] == '.' ) break;
		char tmp = board[0][xloop] != 'T' ? board[0][xloop] : board[1][xloop]; 
		if ( yloop && board[yloop][xloop] != 'T' && tmp != board[yloop][xloop] ) break;
		if ( yloop == 3 ) return tmp;
	}

	// diagonal(1) check
	for ( int loop=0; loop<4; loop++ )
	{
		if ( board[loop][loop] == '.' ) break;
		char tmp = board[0][0] != 'T' ? board[0][0] : board[1][1]; 
		if ( loop && board[loop][loop] != 'T' && tmp != board[loop][loop] ) break;
		if ( loop == 3 ) return tmp;
	}

	// diagonal(2) check
	for ( int loop=0; loop<4; loop++ )
	{
		if ( board[loop][3-loop] == '.' ) break;
		char tmp = board[0][3-0] != 'T' ? board[0][3-0] : board[1][3-1]; 
		if ( loop && board[loop][3-loop] != 'T' && tmp != board[loop][3-loop] ) break;
		if ( loop == 3 ) return tmp;
	}

	return exist_blank ? 'N' : 'D';
}

int main()
{
	FILE *in_file, *out_file;
	char in_string [MAX_LENGTH];
	char out_string[MAX_LENGTH];

	in_file  = fopen("in.txt",  "r");
	out_file = fopen("out.txt", "w");
	if ( in_file  == NULL ) { cout << "in.txt open error" <<  endl; exit(0); }
	if ( out_file == NULL ) { cout << "out.txt open error" << endl; exit(0); }

	int T = 0;
	fscanf(in_file, "%d\n", &T);
	cout << "T:" << T << endl;
	for ( int tloop=0; tloop<T; tloop++ )
	{
		for ( int loop=0; loop<4; loop++ )
		{
			char a, b, c, d;
			fscanf(in_file, "%c%c%c%c\n", &board[loop][0], &board[loop][1], &board[loop][2], &board[loop][3]);
			cout << "T:" << tloop+1 << " : " << board[loop][0] << board[loop][1] << board[loop][2] << board[loop][3] << endl;
		}
		cout << endl;

		switch ( get_winner() )
		{
		case 'O' : sprintf(out_string, "Case #%d: O won\n", tloop+1); break;
		case 'X' : sprintf(out_string, "Case #%d: X won\n", tloop+1); break;
		case 'D' : sprintf(out_string, "Case #%d: Draw\n", tloop+1); break;
		case 'N' : sprintf(out_string, "Case #%d: Game has not completed\n", tloop+1); break;
		}
		fputs(out_string, out_file);
	}
	fclose (in_file);
	fclose (out_file);
}