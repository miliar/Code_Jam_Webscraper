#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;
bool xwon(vector<string> board)
{
	// check row-wise	
	for(int i = 0; i < board.size() ;i++)
	{
		int mv = 0;		
		for(int j = 0; j < board[0].size() ;j++)
		{	
			if(board[i][j] == 'X' || board[i][j] == 'T')
				mv++;
			else
				break;
		}
		//cout << mv << endl;
		if(mv == 4)
			return true;
	}
	//cout << endl;
	//check column-wise
	for(int i = 0; i < board[0].size() ; i++)
	{
		int mv = 0;		
		for(int j = 0 ;j < board.size();j++)
		{
			if(board[j][i] == 'X' || board[j][i] == 'T')
				mv++;
			else
				break;
		}
		//cout << mv << endl;
		if(mv == 4)
			return true;
	}
	// check diagonal
	int mov = 0;
	for(int i = 0; i < board.size(); i++)
	{
		if(board[i][i] == 'X' || board[i][i] == 'T')
			mov++;
	}
	//cout << endl;
	//cout << mov << endl;
	if(mov == 4)
		return true;
	//check diagonal
	mov = 0;
	for(int i = 0; i < board.size();i++)
	{
		if(board[i][board.size() - i-1] == 'X' || board[i][board.size() - i-1] == 'T')
			mov++;
	}
	//cout << endl;
	//cout << mov << endl;
	if(mov == 4)
		return true;
	return false;
}
bool owon(vector<string> board)
{
	// check row-wise
	//cout << endl;	
	for(int i = 0; i < board.size() ;i++)
	{
		int mv = 0;		
		for(int j = 0; j < board[0].size() ;j++)
		{	
			if(board[i][j] == 'O' || board[i][j] == 'T')
				mv++;
			else
				break;
		}
		//cout << mv << endl;
		if(mv == 4)
			return true;
	}
	//check column-wise
	for(int i = 0; i < board[0].size() ; i++)
	{
		int mv = 0;		
		for(int j = 0 ;j < board.size();j++)
		{
			if(board[j][i] == 'O' || board[j][i] == 'T')
				mv++;
			else
				break;
		}
		//cout << mv << endl;
		if(mv == 4)
			return true;
	}
	// check diagonal
	int mov = 0;
	for(int i = 0; i < board.size(); i++)
	{
		if(board[i][i] == 'O' || board[i][i] == 'T')
			mov++;
	}
	//cout << endl;
	//cout << mov << endl;		
	if(mov == 4)
		return true;
	//check diagonal
	mov = 0;
	for(int i = 0; i < board.size();i++)
	{
		if(board[i][board.size() - i-1] == 'O' || board[i][board.size() - i-1] == 'T')
			mov++;
	}
	//cout << endl;
	//cout << mov << endl;	
	if(mov == 4)
		return true;
	return false;
}
bool game_not_completed(vector<string> board)
{
	for(int i = 0; i < board.size();i++)
	{
		for(int j = 0; j < board[0].size() ;j++)
		{
			//cout << board[i][j];			
			if(board[i][j]=='.')
				return true;
		}
	}
	return false;
}
int main()
{
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		vector<string> board;
		string new_line;
		for(int it = 0 ; it < 4;it++)
		{
			string temp="";
			cin >> temp;
			//cout << temp << endl;
			board.push_back(temp);
		}
		//cin >> new_line;
		//cout << endl;
		cout << "Case #" << i << ": "; 
		if(xwon(board))
		{
			cout << "X won";	
		}
		else if(owon(board))
		{
			cout << "O won";
		}
		else if(game_not_completed(board))
		{
			cout << "Game has not completed";
		}
		else
			cout << "Draw";
		cout << endl;
		//cin >> new_line;		
	} 
}
