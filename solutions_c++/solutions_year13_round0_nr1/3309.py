#include <iostream>
#include <fstream>
using namespace std;
#include <string.h>
#include <assert.h>

const char* filename = "data.txt";
const char* answerfile = "answer.txt";

// TICTACTOMEK
enum CaseContent
{
	X,
	O,
	EMPTY,
	T,
};

CaseContent convertCharToEnum(char c)
{
	switch( c )
	{
	case 'X':
		return CaseContent::X;
	case 'O':
		return CaseContent::O;
	case '.':
		return CaseContent::EMPTY;
	case 'T':
		return CaseContent::T;
	}
	assert(false);
	cout<<"couldn't convert "<<c<<endl;
	return CaseContent::X;
}

enum ProblemAnswer
{
	ERROR,
	XWON,
	OWON,
	DRAW,
	UNCOMPLETE,
};

// return true if 'winner' (X or O) won, false otherwise
bool Checkforwin( CaseContent board[4][4], CaseContent winner)
{
	// check lines:
	for( int i=0; i<4; i++)
	{
		bool a = board[i][0] == winner || board[i][0] == T;
		bool b = board[i][1] == winner || board[i][1] == T;
		bool c = board[i][2] == winner || board[i][2] == T;
		bool d = board[i][3] == winner || board[i][3] == T;

		if( a && b && c && d  )
			return true;
	}

	// check columns:
	for( int j=0; j<4; j++)
	{
		bool a = board[0][j] == winner || board[0][j] == T;
		bool b = board[1][j] == winner || board[1][j] == T;
		bool c = board[2][j] == winner || board[2][j] == T;
		bool d = board[3][j] == winner || board[3][j] == T;

		if( a && b && c && d  )
			return true;
	}

	// check diagonals
	{
		bool a = board[0][0] == winner || board[0][0] == T;
		bool b = board[1][1] == winner || board[1][1] == T;
		bool c = board[2][2] == winner || board[2][2] == T;
		bool d = board[3][3] == winner || board[3][3] == T;
		if( a && b && c && d  )
			return true;
	}

	{
		bool a = board[3][0] == winner || board[3][0] == T;
		bool b = board[2][1] == winner || board[2][1] == T;
		bool c = board[1][2] == winner || board[1][2] == T;
		bool d = board[0][3] == winner || board[0][3] == T;
		if( a && b && c && d  )
			return true;
	}

	return false;
}

ProblemAnswer solveProblem(ifstream& instream)
{
	// read the data in this array
	CaseContent board[4][4]; // board[row][column]
	for( int i=0; i<4; i++ )
	{
		char a,b,c,d;
 		char ptr[200];
 		instream.getline (ptr, 200);
		sscanf(ptr,"%c%c%c%c",&a,&b,&c,&d);
		cout<<a<<b<<c<<d<<endl;
		board[i][0] = convertCharToEnum(a);
		board[i][1] = convertCharToEnum(b);
		board[i][2] = convertCharToEnum(c);
		board[i][3] = convertCharToEnum(d);
	}

	//1. O or X won
	if( Checkforwin(board, O) )
		return ProblemAnswer::OWON;

	if( Checkforwin(board, X) )
		return ProblemAnswer::XWON;

	//2. Make sure it's finished
	for( int i=0; i<4; i++ )
	{
		for( int j=0; j<4; j++ )
		{
			if( board[i][j] == CaseContent::EMPTY )
			{
				return ProblemAnswer::UNCOMPLETE;
			}
		}
	}	

	//3. Then it's a draw
	return ProblemAnswer::DRAW;
}

void writeAnswer( ofstream& outstream, int caseNum, ProblemAnswer answer )
{
	outstream<<"Case #"<<caseNum<<": ";
	switch( answer )
	{
	case XWON:
		outstream<<"X won"<<endl;
		cout<<"X won"<<endl;
		break;
	case OWON:
		outstream<<"O won"<<endl;
		cout<<"O won"<<endl;
		break;
	case DRAW:
		outstream<<"Draw"<<endl;
		cout<<"Draw"<<endl;
		break;
	case UNCOMPLETE:
		outstream<<"Game has not completed"<<endl;
		cout<<"Game has not completed"<<endl;
		break;
	}
}

int main()
{
	ifstream instream;
	instream.open (filename, ifstream::in );
	if( ! instream.good() )
	{
		cout<<"couldn't open "<<filename<<endl;
		return 0;
	}

	ofstream outstream;
	outstream.open (answerfile, ifstream::out );
	if( ! outstream.good() )
	{
		cout<<"couldn't open "<<answerfile<<endl;
		return 0;
	}

  char ptr[200];
  instream.getline (ptr, 200);
	int nbPbm = 0;
	sscanf(ptr,"%d",&nbPbm);
	cout<<nbPbm<<endl;

	for( int i=0; i< nbPbm; i++ )
	{
		ProblemAnswer answer = solveProblem( instream );
		writeAnswer(outstream,i+1,answer);

		instream.getline (ptr, 200); // empty line
		cout<<ptr<<endl;
	}

	cout<<"solved"<<endl;
	return 0;
}
