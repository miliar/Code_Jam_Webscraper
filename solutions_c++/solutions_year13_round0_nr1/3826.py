#include <iostream>
#include <vector>
using namespace std;

int check(const vector< string > & board, const char & c)
{
	unsigned j, i;
 	for(i = 0; i < 4; ++i)
	{
		
		for(j = 0; j < 4 && (board[i][j] == c || board[i][j] == 'T'); ++j);
		if(j == 4) return true;
		for(j = 0; j < 4 && (board[j][i] == c || board[j][i] == 'T'); ++j);
		if(j == 4) return true;
	}
		
	for(i = 0; i < 4 && (board[i][i] == c || board[i][i] == 'T'); ++i);
	if(i == 4) return true;
	for(j = 0; j < 4 && (board[j][j] == c || board[j][j] == 'T') ; ++j);
	if(j == 4) return true;
	for(i = 0, j = 3; i < 4 && (board[i][j] == c || board[i][j] == 'T'); ++i, --j);
	return i == 4;
}

bool game_finished(const vector<string> & board)
{
	unsigned j;
	for(unsigned i = 0; i < 4; ++i)
	{
		for(j = 0; j < 4; ++j)
		{
			if(board[i][j] == '.') return false;
		}
	}
	return true;

}
void winner(const vector<string> & board, const int & N)
{
	cout << "Case #" << N << ": ";
	if(check(board, 'X'))
	{
		cout << "X won";
	}
	else if(check(board, 'O'))
	{
		cout << "O won";
	}
	else
	{
		if(game_finished(board))
		{
			cout << "Draw";
		}
		else
		{
			cout << "Game has not completed";
		}
	}

}


vector <string> make_board()
{
	vector <string> board;
	string row;
	for(unsigned i = 0; i < 4; ++i)
	{
		cin >> row;
		board.push_back(row);
	}
	return board;			
}



int main()
{
	unsigned N = 0;
	cin >> N;
	vector<string> board;
	unsigned ntl = N-1;
	for(unsigned i = 0; i < N; ++i)
	{
		board = make_board();
		winner(board ,i+1);
		if(i < ntl) cout << endl;
	}
	return 0;
}
