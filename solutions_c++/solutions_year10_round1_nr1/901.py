#include<iostream>
#include<vector>
using namespace std;



bool check(vector<string> board, int ii, int jj, int k, int n, char c)
{
	bool good = true;
	for(int i = ii; i < ii+k;i++)
	{
		if(i >= n)
		{
			good = false;
			break;
		}
		if(board[i][jj] != c)
		{
			good = false;
			break;
		}
	}
	if(good == true)
		return true;
	good = true;
	for(int j = jj; j < jj+k;j++)
	{
		if(j >= n)
		{
			good = false;
			break;
		}
		if(board[ii][j] != c)
		{
			good = false;
			break;
		}
	}
	if(good == true)
		return true;
	good = true;

	int i = ii;
	for(int j = jj; (j < jj + k) && (i < ii + k); j++)
	{
		//cout << " i j " << i << " " << j << endl;
		if(i >= n)
		{
			good = false;
			break;
		}
		if(j >= n)
		{
			good = false;
			break;
		}
			
		if(board[i][j] != c)
		{
			good = false;
			break;
		}
		i++;
		
	}
	if(good == true)
		return true;
	good = true;
	i = ii;
	for(int j = jj; (j < jj + k) && (i < ii + k); j++)
	{
		if(i < 0)
		{
			good = false;
			break;
		}
		if(j >= n)
		{
			good = false;
			break;
		}
			
		if(board[i][j] != c)
		{
			good = false;
			break;
		}
		i--;
	}
	if(good == true)
		return true;
	good = true;

	return false;
	
}

int main()
{
	int T;
	cin >> T;
	for(int t = 0; t < T;t++)
	{
		
		int N, K;
		cin >> N >> K;
		vector<string> board;
		for(int i = 0; i < N;i++)
		{
			string g;
			cin >> g;
			board.push_back(g);
		}
		vector<string> newBoard = board;
		for(int i = N-1; i >=0 ; i--)
		{
			string g;
			for(int j = 0; j < N; j++)
			{
				newBoard[j][N-1-i] = board[i][j];
			}
			
		}
		
		for(int j = 0; j < N;j++)
		{
			for(int i = N-1; i >= 0; i--)
			{
				if(newBoard[i][j] == '.')
					continue;
					
				int ii = i+1;
				
				char c = newBoard[i][j];
				newBoard[i][j] = '.';
				while(ii < N && newBoard[ii][j] == '.' )
				{
					//newBoard[ii][j] = '.';
					ii++;
					//cout << "ii is " << ii << endl;
				}
				newBoard[ii-1][j] = c;
				//cout << "YO" << endl;
					
				
				
			}
			
		}
		
		/*for(int i = 0; i < newBoard.size();i++)
		{
			cout << newBoard[i] << endl;
		}*/
	
		//check blue
		bool blue = false;
		bool red = false;
		for(int i = 0; i < N;i++)
		{
			for(int j = 0; j < N;j++)
			{
				blue = check(newBoard, i,j,K,N,'B') || blue;
				red = check(newBoard, i,j,K,N,'R') || red;
			}
		}
		
		
		cout << "Case #" << (t+1) << ": " ;
		if(blue == true)
		{
			if(red)
				cout << "Both" << endl;
			else
				cout << "Blue" << endl;
		}
		else
		{
			if(red) 
				cout << "Red" << endl;
			else
				cout << "Neither" << endl;
		}
	}


}
