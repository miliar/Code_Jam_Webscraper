#include <iostream>
#include <vector>
using namespace std;

void HPass(vector< vector<char> >&board, int N, int K, bool&redWins, bool& blueWins)
{
	for(int j=0;j<N;j++)
	{
		char lastItem='.';
		int loopLen = 0;
		for(int k=0;k<N;k++)
		{
			if(board[j][k]==lastItem)
			{
				if(lastItem!='.')
					loopLen++;
			}
			else
			{
				lastItem=board[j][k];
				if(lastItem!='.')
					loopLen=1;
				else
					loopLen=0;
			}
			if(loopLen==K)
			{
				if(lastItem=='R')
					redWins = true;
				if (lastItem=='B')
					blueWins = true;	
			}
		}
	}
}

void VPass(vector< vector<char> >&board, int N, int K, bool&redWins, bool& blueWins)
{
	for(int k=0;k<N;k++)
	{
		char lastItem='.';
		int loopLen = 1;
		for(int j=0;j<N;j++)
		{
			if(board[j][k]==lastItem)
			{
				if(lastItem!='.')
					loopLen++;
			}
			else
			{
				lastItem=board[j][k];
				loopLen=1;
			}
			if(loopLen==K)
			{
				if(lastItem=='R')
					redWins = true;
				if (lastItem=='B')
				{
					blueWins = true;
				}
			}
		}
	}

}

void DPass1(vector< vector<char> >&board, int N, int K, bool&redWins, bool& blueWins)
{
	for(int initCol=0;initCol<N;initCol++)
	{
		char lastItem='.';
		int loopLen = 1;
		for(int offset=0;offset<=(N-1-initCol);offset++)
		{
			int col = initCol+offset;
			int row = offset;
			if(board[row][col]==lastItem)
			{
				if(lastItem!='.')
					loopLen++;
			}
			else
			{
				lastItem=board[row][col];
				loopLen=1;
			}
			if(loopLen==K)
			{
				if(lastItem=='R')
					redWins = true;
				if (lastItem=='B')
					blueWins = true;
			}
		}
	}
}

void DPass2(vector< vector<char> >&board, int N, int K, bool&redWins, bool& blueWins)
{
	for(int initRow=1;initRow<N;initRow++)
	{
		char lastItem='.';
		int loopLen = 1;
		for(int offset=0;offset<=(N-1-initRow);offset++)
		{
			int row = initRow+offset;
			int col = offset;
			if(board[row][col]==lastItem)
			{
				if(lastItem!='.')
					loopLen++;
			}
			else
			{
				lastItem=board[row][col];
				loopLen=1;
			}
			if(loopLen==K)
			{
				if(lastItem=='R')
					redWins = true;
				if (lastItem=='B')
					blueWins = true;
			}
		}
	}
}
void DPass3(vector< vector<char> >&board, int N, int K, bool&redWins, bool& blueWins)
{
	for(int initRow=1;initRow<N;initRow++)
	{
		char lastItem='.';
		int loopLen = 1;
		for(int offset=0;offset<=initRow;offset++)
		{
			int row = initRow-offset;
			int col = offset;
			if(board[row][col]==lastItem)
			{
				if(lastItem!='.')
					loopLen++;
			}
			else
			{
				lastItem=board[row][col];
				loopLen=1;
			}
			if(loopLen==K)
			{
				if(lastItem=='R')
					redWins = true;
				if (lastItem=='B')
					blueWins = true;
			}
		}
	}
}
void DPass4(vector< vector<char> >&board, int N, int K, bool&redWins, bool& blueWins)
{
	for(int initCol=0;initCol<N;initCol++)
	{
		char lastItem='.';
		int loopLen = 1;
		for(int offset=0;offset<=(N-1-initCol);offset++)
		{
			int col = initCol+offset;
			int row = N-1-offset;
			if(board[row][col]==lastItem)
			{
				if(lastItem!='.')
					loopLen++;
			}
			else
			{
				lastItem=board[row][col];
				loopLen=1;
			}
			if(loopLen==K)
			{
				if(lastItem=='R')
					redWins = true;
				if (lastItem=='B')
					blueWins = true;
			}
		}
	}
}

int main()
{
	int tc;
	cin >> tc;
	for(int i=0;i<tc;i++)
	{
		int N, K; // N^2 grid, K in a row
//		cout << "Case "<<i<<endl;
		cin >> N;
		cin >> K;
//		cout << N << " " << K << endl;
		vector < vector <char> > board;

		for(int j=0; j<N;j++)
		{
			vector<char> boardRow(N);
			board.push_back(boardRow);
		}

		char c;
		for(int j=0;j<N;j++) // j => Row
		{
			for(int k=0;k<N;k++) // k=> Col
			{
				cin >> c;
				board[k][(N-1)-j] = c;
			}
		}
#if 0
		for(int j=0;j<N;j++) // j => Row
		{
			for(int k=0;k<N;k++) // k=> Col
			{
				cout<< board[j][k];
			}
			cout << endl;
		}
		cout << endl;
#endif

		// simulate gravity
		for(int k=0;k<N;k++)
		{
			vector<int> lastDot;
			for(int j=N-1;j>=0;j--)
			{
				if(board[j][k]!='.')
				{
					if(lastDot.size()>0)
					{
						board[lastDot[0]][k]=board[j][k];
						board[j][k] = '.';
						lastDot.erase(lastDot.begin());
						lastDot.push_back(j);
					}
				}
				else
				{
					lastDot.push_back(j);
				}
			}
		}
#if 0
		for(int j=0;j<N;j++) // j => Row
		{
			for(int k=0;k<N;k++) // k=> Col
			{
				cout<< board[j][k];
			}
			cout << endl;
		}
		cout << endl;
#endif
		bool redWins = false, blueWins=false;
		HPass(board, N, K, redWins, blueWins);
//		cout << "HPass " << redWins << " " << blueWins << endl;
		VPass(board, N, K, redWins, blueWins);
//		cout << "VPass " << redWins << " " << blueWins << endl;
		DPass1(board, N, K, redWins, blueWins);
//		cout << "DPass1 " << redWins << " " << blueWins << endl;
		DPass2(board, N, K, redWins, blueWins);
//		cout << "DPass2 " << redWins << " " << blueWins << endl;
		DPass3(board, N, K, redWins, blueWins);
		DPass4(board, N, K, redWins, blueWins);
		cout << "Case #"<<i+1<<": ";
		if(redWins && blueWins)
		{
			cout <<"Both";
		}
		else
		if(redWins)
		{
			cout << "Red";
		}
		else
		if(blueWins)
		{
			cout << "Blue";
		}
		else
		{
			cout << "Neither";
		}
		cout << endl;
#if 0
		for(int j=0;j<N;j++) // j => Row
		{
			for(int k=0;k<N;k++) // k=> Col
			{
				cout<< board[j][k];
			}
			cout << endl;
		}
		cout << endl;
#endif
		// make a H-pass
	}
	return 0;
}

