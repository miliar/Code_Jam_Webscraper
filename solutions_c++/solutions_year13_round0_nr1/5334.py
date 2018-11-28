#include <iostream>
#include <cstdio>
using namespace std;
#define N 4
const int DRAW=0, NOBODY=1, WINX=2, WINO=3;
const bool debug = false;
int main() 
{
	int T;
	char *board[N];
	char first;
	short int result;
	bool isFull;
	for(int i=0; i<N; i++)
		board[i] = new char[N+1];
	cin >> T;
	for(int l=1; l<=T; l++)
	{
		for(int i=0; i<N; i++)
		{
			cin >> board[i];
			//scanf("%s", board[i]);
			if(debug)
				cout << board[i] << endl;
		}
		result = DRAW;
		for(int i=0; i<N; i++)
		{
			first = board[i][0];
			if(first=='T')
				first = board[i][1];
			if(first=='.')
				result = DRAW;
			else
			{
				result = (first=='X') ? WINX : WINO;
				for(int j=1; j<N; j++)
					if(board[i][j]!=first && board[i][j]!='T')
					{
						result = DRAW;
						break;
					}
				if(result != DRAW)
					break;
			}
		}
		if(result==DRAW)
		{
			for(int j=0; j<N; j++)
			{
				first = board[0][j];
				if(first=='T')
					first = board[1][j];
				if(first=='.')
					result = DRAW;
				else
				{
					result = (first=='X') ? WINX : WINO;
					for(int i=1; i<N; i++)
					{
						if(board[i][j]!=first && board[i][j]!='T')
						{
							result = DRAW;
							break;
						}
					}
					if(result != DRAW)
						break;
				}
			}
		}
		if(result==DRAW)
		{
			first = board[0][0];
			if(first=='T')
				first = board[1][1];
			if(first=='.')
				result = DRAW;
			else
			{
				result = (first=='X') ? WINX : WINO;
				for(int i=1; i<N; i++)
					if(board[i][i]!=first && board[i][i]!='T')
						result = DRAW;
			}
		}
		if(result==DRAW)
		{
			first = board[0][N-1];
			if(first=='T')
				first = board[1][N-2];
			if(first=='.')
				result = DRAW;
			else
			{
				result = (first=='X') ? WINX : WINO;
				for(int i=1; i<N; i++)
					if(board[i][N-i-1]!=first && board[i][N-i-1]!='T')
						result = DRAW;
			}
		}
		if(result==DRAW)
		{
			isFull = true;
			for(int i=0; i<N && isFull; i++)
				for(int j=0; j<N; j++)
					if(board[i][j]=='.')
					{
						isFull = false;
						break;
					}
			if(isFull)
				printf("Case #%d: Draw\n", l);
			else
				printf("Case #%d: Game has not completed\n", l);
		}
		else
		{
			if(result==WINX)
				printf("Case #%d: X won\n", l);
			else
				printf("Case #%d: O won\n", l);
		}
		cin.getline(board[0], N+1);
	}
	for(int i=0; i<N; i++)
		delete board[i];
	return 0;
}