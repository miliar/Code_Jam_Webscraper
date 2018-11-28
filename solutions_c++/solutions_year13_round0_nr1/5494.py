#define ROW_SIZE 4
#define COLUMN_SIZE 4

#include <fstream>

bool has_blank( char*, int row_size, int column_size );
char search_array_win( char*, int len );
char test_dig_win( char*, int row_size, int column_size );

int main()
{
	//open files.
	std::ifstream in;
	std::ofstream out;

	in.open("A-small-attempt1.in");
	out.open("A-small-attempt1.out");

	//global variables.
	int T;
	char * board;
	char result;

	//in and out.
	in >> T;
	for( int t = 0; t < T; t ++ )
	{
		//get board.
		board = new char [ ROW_SIZE * COLUMN_SIZE ];
		//not_filled = false;

		//output.
		out << "Case #" << t + 1 << ": ";

		//read lines.
		for( int row = 0; row < ROW_SIZE; row ++ )
		{
			in >> board[ row * COLUMN_SIZE ]
			>> board[ row * COLUMN_SIZE + 1 ]
			>> board[ row * COLUMN_SIZE + 2 ]
			>> board[ row * COLUMN_SIZE + 3 ];
		}

		//search rows and columns.
		for( int i = 0; i < ROW_SIZE; i ++ )
		{
			//rows.
			result = search_array_win( board + i * ROW_SIZE , ROW_SIZE );
			if( result != ' ' )
			{
				//out << result << " won" << std::endl;
				break;
			}

			//columns.		
			char *arr = new char [COLUMN_SIZE];
			arr[ 0 ] = board[ i ];
			arr[ 1 ] = board[ i + COLUMN_SIZE ];
			arr[ 2 ] = board[ i + COLUMN_SIZE * 2 ];
			arr[ 3 ] = board[ i + COLUMN_SIZE * 3 ];

			result = search_array_win( arr, COLUMN_SIZE );	

			if( result != ' ' )
			{
				break;
			}

			delete arr;
		}

		
		//not completed possible.
		if( result == ' ' )
		{
			result = test_dig_win( board, ROW_SIZE, COLUMN_SIZE );
		}

		//show results.
		if( result != ' ' )
		{
			out << result << " won" << std::endl;
		}else if( has_blank( board, ROW_SIZE, COLUMN_SIZE ) )
		{
			out << "Game has not completed" << std::endl;
		}else
		{
			out << "Draw" << std::endl;
		}

		//release.
		delete board;
	}

	//close files.
	in.close();
	out.close();

	return 0;
}

bool has_blank( char* b, int row_size, int column_size )
{
	for( int i = 0; i < row_size; i ++ )
	{
		for( int j = 0; j < column_size; j ++ )
		{
			if( b[ i * column_size + j ] == '.' )
			{
				return true;
			}
		}
	}

	return false;
}

char search_array_win( char* a, int len )
{
	char p_result = a[ 0 ];

	if( p_result == '.' )
	{
		return ' ';
	}

	for( int i = 1; i < len; i ++ )
	{
		if( a[ i ] != p_result && a[ i ] != 'T' )
		{
			p_result = ' ';
		}
	}

	return p_result;
}

char test_dig_win( char* b, int row_size, int column_size )
{
	char result;
	char *arr = new char[ row_size ];
	arr[0] = b[0];
	arr[1] = b[5];
	arr[2] = b[10];
	arr[3] = b[15];

	result = search_array_win( arr, row_size );
	if( result != ' ' )
	{
		return result;
	}

    arr[0] = b[3];
	arr[1] = b[6];
	arr[2] = b[9];
	arr[3] = b[12];

	result = search_array_win( arr, row_size );
	if( result != ' ' )
	{
		return result;
	}

	return ' ';
}