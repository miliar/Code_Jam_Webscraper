#include<iostream>
#include<fstream>
#include<vector>

#define MAX 256

using namespace std;

struct Board{
	char board[4][4];
	bool full;
	Board()
	{
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				board[i][j]='.';
			}
		}
	}
	char getFromInput(){
		full = true;
		for(int i=0;i<4;i++)
		{
			string line;
			cin >> line;
			for(int j=0;j<4;j++)
			{
				char c = line[j];
				board[i][j] = c;

				if(c == '.')
				{
					full = false;
				}
			}
		}
		
		return getWinner2();
	}
	char getWinner2()
	{
		char c;
		bool flag;
		// vertical
		for(int i=0;i<4;i++)
		{
			flag = true;
			c=board[i][0];
			if(c == 'T')
			{
				c = board[i][1];
			}
			if(c == '.')
			{
				continue;
			}
			for(int j=0;j<4;j++)
			{
				if(board[i][j] != c && board[i][j] != 'T')
				{
					flag = false;
					break;
				}
			}
			if(flag)
			{
				return c;
			}
		}

		// horizontal
		for(int i=0;i<4;i++)
		{
			flag = true;
			c=board[0][i];
			if(c == 'T')
			{
				c = board[1][i];
			}
			if(c == '.')
			{
				continue;
			}
			for(int j=0;j<4;j++)
			{
				if(board[j][i] != c && board[j][i] != 'T')
				{
					flag = false;
					break;
				}
			}
			if(flag)
			{
				return c;
			}
		}

		// diagonal \.
		flag = true;
		c=board[0][0];
		if(c == 'T')
		{
			c = board[1][1];
		}
		if(c != '.')
		{
			for(int i=0;i<4;i++)
			{
				if(board[i][i] != c && board[i][i] != 'T')
				{
					flag = false;
					break;
				}
			}
			if(flag)
			{
				return c;
			}
		}
		

		// diagonal /.
		flag = true;
		c=board[0][3];
		if(c == 'T')
		{
			c = board[1][2];
		}
		if(c != '.')
		{
			for(int i=0;i<4;i++)
			{
				if(board[i][3-i] != c && board[i][3-i] != 'T')
				{
					flag = false;
					break;
				}
			}
			if(flag)
			{
				return c;
			}
		}

		return '.';
	}
};

int main(int argc, char const *argv[])
{
	streambuf *iBackup = NULL , *oBackup = NULL;
	ofstream output;
	ifstream input;

	// backsup input/output
	iBackup = cin.rdbuf();
	oBackup = cout.rdbuf();
	
	input.open(argv[1]);
	
	if( input.fail()){
		cout << "input failed." << endl;
		return 1;
	}
	cin.rdbuf(input.rdbuf());
	
	output.open(argv[2]);
	if( output.fail()){
		cout << "output failed." << endl;
		return 1;
	}
	cout.rdbuf(output.rdbuf());
	
	int T=0;
	cin >> T;
	char winner;
	for(int i=1;i<=T;i++)
	{
		Board b;
		winner = b.getFromInput();
		
		switch(winner)
		{
			case 'X': cout << "Case #" << i << ": X won" << endl; break;
			case 'O': cout << "Case #" << i << ": O won" << endl; break;
			case '.': cout << "Case #" << i << (b.full ? ": Draw" : ": Game has not completed") << endl; break;
		}
	}
	
	input.close();
	cin.rdbuf(iBackup);
	output.close();
	cout.rdbuf(oBackup);

	return 0;
}
