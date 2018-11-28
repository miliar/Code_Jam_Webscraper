#include <fstream>

using namespace std;

char board[4][5];

int main(int argc, char const *argv[])
{
	int T, t, i, j, xc0, oc0, xc1, oc1, total_count, win;
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	in>>T;
	for (t = 1; t <= T; t++)
	{
		total_count = 0;
		for (i = 0; i < 4; i++)
			in>>board[i];

		for (i = 0, win = 0; i < 4 && !win; i++)
		{
			xc0 = xc1 = oc0 = oc1 = 0;	
			for (j = 0; j < 4; j++)
			{
				if ('.' != board[i][j])
				{
					total_count++;
					if ('O' != board[i][j])
						xc0++;
					if ('X' != board[i][j])
						oc0++;
				}
				if ('.' != board[j][i])
				{
					if ('O' != board[j][i])
						xc1++;
					if ('X' != board[j][i])
						oc1++;
				}
			}
			if (4 == xc0 || 4 == xc1)
				win = 1;	// X win
			else if (4 == oc0 || 4 == oc1)
				win = 2;	// O win
		}
		if(!win)
		{
			int sum;
			sum = board[0][0]+board[1][1]+board[2][2]+board[3][3];
			if(sum == 'X'*4 || sum == 'X'*3+'T')
				win = 1;
			else if (sum == 'O'*4 || sum == 'O'*3+'T')
				win = 2;
			else
			{
				sum = board[0][3]+board[1][2]+board[2][1]+board[3][0];
				if(sum == 'X'*4 || sum == 'X'*3+'T')
					win = 1;
				else if (sum == 'O'*4 || sum == 'O'*3+'T')
					win = 2;
			}
		}
		string result;
		if(1 == win)
			result = "X won";
		else if(2 == win)
			result = "O won";
		else if(16 == total_count)
			result = "Draw";
		else
			result = "Game has not completed";
		out<<"Case #"<<t<<": "<<result<<endl;
	}

	return 0;
}




