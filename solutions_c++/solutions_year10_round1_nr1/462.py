#include<iostream>
#include<vector>
#include<string>
#include<cassert>
#include<set>

using namespace std;

bool match(vector<string> & board, char tomatch, int matches, size_t row, size_t col)
{
	assert(board[row][col]==tomatch);
	//across first
	if((col+matches)<=(board.size()))
	{
		string mystr = board[row].substr(col,matches);
		set<char> vals(mystr.begin(),mystr.end());
		if(vals.size()==1)
		{
//			cerr << "Winner: " << tomatch << endl;
			return true;
		}
	}

	//now down
	if((row+matches)<=(board.size()))
	{
		size_t i;
		for(i=row;i<(row+matches);i++)
		{
			if(board[i][col]!=tomatch)
			{
				break;
			}
		}
		if(i==(row+matches))
		{
//			cerr << "Winner: " << tomatch << endl;
			return true;
		}
	}

	//now down-right
	if(((row+matches)<=(board.size())) && ((col+matches)<=(board.size())))
	{
		size_t i, j;
		for(i=row, j=col;i<(row+matches);i++,j++)
		{
			if(board[i][j]!=tomatch)
			{
				break;
			}
		}
		if(i==(row+matches))
		{
//			cerr << "Winner: " << tomatch << endl;
			return true;
		}
	}

	//now down-left
	if(((row+matches)<=(board.size())) && ((col-matches)>=0))
	{
		size_t i, j;
		for(i=row, j=col;i<(row+matches);i++,j--)
		{
			if(board[i][j]!=tomatch)
			{
				break;
			}
		}
		if(i==(row+matches))
		{
//			cerr << "Winner: " << tomatch << endl;
			return true;
		}
	}

	return false;
}

int scan(vector<string> & board, int k)
{
	bool red = false, blue = false;
	for(size_t i=0;i<board.size();i++)
	{
		for(size_t j=0;j<board.size();j++)
		{
			if(board[i][j]=='R')
			{
				red |= match(board,'R',k,i,j);
			}
			else if(board[i][j]=='B')
			{
				blue |= match(board,'B',k,i,j);
			}
		}
	}
	return (int)(red) + ((int)blue << 1);
}

int main()
{
	int num;
	cin >> num;
	for(int x=1;x<=num;x++)
	{
		int K, N;
		cin >> N >> K;
		vector<string> board(N);
		for(size_t i=0;i<N;i++)
		{
			cin >> board[i];
			for(string::iterator it=board[i].begin();it!=board[i].end();)
			{
				if((*it)=='.')
				{
					it = board[i].erase(it);
				}
				else
				{
					it++;
				}
			}
			while(board[i].size()<N)
			{
				board[i].insert(board[i].begin(),'.');
			}
		}

/*		for(size_t i=0;i<N;i++)
		{
			cerr << board[i] << endl;
		}
*/
		int winners = scan(board,K);

		cout << "Case #" << x << ": ";
		switch(winners)
		{
		case 0:
			cout << "Neither";
			break;
		case 1:
			cout << "Red";
			break;
		case 2:
			cout << "Blue";
			break;
		case 3:
			cout << "Both";
			break;
		default:
			assert(0);
			break;
		}
		cout << endl;
			
	}
	return 0;	
}
