#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int simulate(vector< vector<int> > & board)
{
	int liveCells = 0;
	vector< vector<int> > v = board;
	for(int i = 0; i < board.size();i++)
	{
		for(int j = 0; j < board[i].size();j++)
		{
			bool north = false;
			bool west = false;
			
			if(i-1 >= 0 && board[i-1][j] == 1)
				north = true;
			
			if(j-1 >= 0 && board[i][j-1] == 1)
				west = true;
			
			if(board[i][j] == 0 && north && west)
				v[i][j] = 1;
			
			if(board[i][j] == 1 && !north && !west)
				v[i][j] = 0;
				
				
			if(v[i][j] == 1)
				liveCells++;
		}
	}
	board = v;
	return liveCells;
}

int main()
{
	int T;
	cin >> T;
	for(int t = 0; t < T;t++)
	{
		int r;
		cin >> r;
		vector<int> row(101,0);
		vector< vector<int> > board(101,row);
		for(int i = 0; i < r;i++)
		{
			int x1, x2, y1, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			for(int x = x1; x <= x2;x++)
			{
				for(int y = y1; y <= y2;y++)
				{
					board[y][x] = 1;
				}
			}
		
		}
		
	/*	for(int i = 0; i < board.size();i++)
		{
			for(int j = 0; j < board[i].size();j++)
			{
				cout << board[i][j] << " ";
			}
			cout << endl;
		}
		*/
		int time = 1;
		while(simulate(board) > 0)
			time++;
		
		cout << "Case #" << t+1 << ": " << time << endl;


	}
}
