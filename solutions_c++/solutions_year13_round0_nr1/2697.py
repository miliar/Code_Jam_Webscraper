#include <string>
#include <cstring>
#include <fstream>

#define N 4
char board [N][N];

bool won(char p)
{
	bool res = false;
	for (int i=0; i<4; i++)
	{
		if ((board[i][0] == p || board[i][0] == 'T') && 
			(board[i][1] == p || board[i][1] == 'T') &&
			(board[i][2] == p || board[i][2] == 'T') &&
			(board[i][3] == p || board[i][3] == 'T') )
			return true;
		if ((board[0][i] == p || board[0][i] == 'T') && 
			(board[1][i] == p || board[1][i] == 'T') &&
			(board[2][i] == p || board[2][i] == 'T') &&
			(board[3][i] == p || board[3][i] == 'T') )
			return true;
		
	}
	if ((board[0][0] == p || board[0][0] == 'T') && 
		(board[1][1] == p || board[1][1] == 'T') &&
		(board[2][2] == p || board[2][2] == 'T') &&
		(board[3][3] == p || board[3][3] == 'T') )
		return true;
	if ((board[0][3] == p || board[0][3] == 'T') && 
		(board[1][2] == p || board[1][2] == 'T') &&
		(board[2][1] == p || board[2][1] == 'T') &&
		(board[3][0] == p || board[3][0] == 'T') )
		return true;
	return res;
}
bool find_blank()
{
	for (int i=0; i<N; i++)
		for (int j=0; j<N; j++)
			if (board[i][j] == '.')
				return true;
	return false;
}
int main()
{
	std::ifstream in;
	std::ofstream out;
	in.open("a.in");
	out.open("a.out");
	int Case;
	in >> Case;
	for (int t=1; t<=Case; t++)
	{
		for (int i=0; i<N; i++) {
			for (int j=0; j<N; j++)
			{
				in >> board[i][j];
			}
		}
		if (won('X'))
		{
			out << "Case #" << t<< ": X won\n";
			continue;
		}
		else if (won('O'))
		{
			out << "Case #" << t<< ": O won\n";
			continue;
		}
		bool not_over = false;
		for (int i=0; i<N; i++) {
			for (int j=0; j<N; j++) {
				if (board[i][j] == '.')
					not_over = true;
			}
		}
		if (not_over)
		{
			out << "Case #" << t<< ": Game has not completed" <<std::endl;
		}
		else
		{
			out << "Case #" << t<< ": Draw" <<std::endl;
		}
	}
	out.close();
	system("pause");
	return 1;
}