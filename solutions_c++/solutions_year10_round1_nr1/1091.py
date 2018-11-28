#include <iostream>

using namespace std;

typedef char Colour;
typedef Colour* LineOfColours;
const char empty = '.';

bool hasWon(Colour **Board, int N, int K, Colour colour)
{
	int score, i, j;
	for(i=0; i<N; ++i)
	{
		score = 0;
		for(j=0; j<N; ++j)
		{
			if(Board[i][j] == colour)
				++score;
			else
				score = 0;
			if(score == K)
				return true;
		}
	}
	for(i=0; i<N; ++i)
	{
		score = 0;
		for(j=0; j<N; ++j)
		{
			if(Board[j][i] == colour)
				++score;
			else
				score = 0;
			if(score == K)
				return true;
		}
	}
	for(i=0; i<N; ++i)
	{
		score = 0;
		for(j=0; i+j<N; ++j)
		{
			if(Board[i+j][j] == colour)
				++score;
			else
				score = 0;
			if(score == K)
				return true;
		}
	}
	for(i=1; i<N; ++i)
	{
		score = 0;
		for(j=0; i+j<N; ++j)
		{
			if(Board[j][i+j] == colour)
				++score;
			else
				score = 0;
			if(score == K)
				return true;
		}
	}
	i=0;
	for(j=0; j<N-1; ++j)
	{
		score = 0;
		for(int k=0; i+k<N && j-k>=0; ++k)
		{
			if(Board[i+k][j-k] == colour)
				++score;
			else
				score=0;
			if(score == K)
				return true;
		}
	}
	j=N-1;
	for(i=0; i<N-1; ++i)
	{
		score = 0;
		for(int k=0; i+k<N && j-k>=0; ++k)
		{
			if(Board[i+k][j-k] == colour)
				++score;
			else
				score=0;
			if(score == K)
				return true;
		}
	}
	return false;
}

void outBoard(Colour **Board, int N)
{
	for(int i=0; i<N; ++i)
	{
		for(int j=0; j<N; ++j)
			cout << Board[i][j];
		cout << endl;
	}
	cout << endl;
}

void squeeze(LineOfColours line, int N)
{
	int i, j;
	for(i=0; i<N; ++i)
	{
		if(line[i] == empty)
		{
			for(j=i; j<N; ++j)
				if(line[j]!=empty)
					break;
			if(j!=N)
			{
				for(int k=0; k+j<N; ++k)
				{
					line[i+k] = line[j+k];
					line[j+k] = empty;
				}
			}
		}
	}
}

int main()
{
	Colour **XBoard, **Board;
	XBoard = new LineOfColours[51];
	Board = new LineOfColours[51];
	int T, t, N, i, j, K;
	char c;
	for(i=0; i<50; ++i)
		XBoard[i] = new Colour[101];

	for(i=0; i<50; ++i)
		for(j=50; j<100; ++j)
			XBoard[i][j] = empty;

	cin >> T;
	for(t=1; t<=T; ++t)
	{
		for(i=0; i<50; ++i)
			for(j=0; j<50; ++j)
				XBoard[i][j] = empty;
		cin >> N >> K;
		for(i=N-1; i>=0; --i)
			for(j=N-1; j>=0; --j)
				cin >> XBoard[i][j];
		for(i=0; i<N; ++i)
		{
			for(j=0; j<N; ++j)
				if(XBoard[i][j] != empty)
					break;
			Board[i] = XBoard[i]+j;
			squeeze(Board[i], N);

		}
		cout << "Case #" << t << ": ";
		bool blueHasWon = hasWon(Board, N, K, 'B');
		bool redHasWon = hasWon(Board, N, K, 'R');
		if(blueHasWon)
		{
			if(redHasWon)
				cout << "Both";
			else
				cout << "Blue";
		}
		else
		{
			if(redHasWon)
				cout << "Red";
			else
				cout << "Neither";
		}
		cout << endl;
	}

	return 0;
}
