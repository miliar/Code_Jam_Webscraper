#include <string>
#include <fstream>

using namespace std;

void calc(char vals[4][4], int startX, int startY, int incX, int incY, int& dotCnt, string& result)
{
    int cntX = 0, cntO = 0, cntT = 0;
    for (int i = 0; i < 4; ++i)
    {
	char curr = vals[startX + i * incX][startY + i * incY];
	if ('X' == curr)
	    ++cntX;
	else if ('O' == curr)
	    ++cntO;
	else if ('T' == curr)
	    ++cntT;
	else
	    ++dotCnt;
    }
    if (cntX + cntT == 4)
	result = "X won";
    else if (cntO + cntT == 4)
	result = "O won";
}

int main (int argc, char*argv[])
{
    char board[4][4];
    ifstream input("A-large.in");
    ofstream output("out.txt");
    int x = 0;
    input >> x;
    for (int i = 0; i < x; ++i)
    {
	for (int j = 0; j < 4; ++j)
	{
	    string s;
	    input >> s;
	    for (int k = 0; k < 4; ++k)
	    {
		board[j][k] = s[k];
	    }
	}
	int dotCnt = 0;
	string result;
	for (int j = 0; j < 4; ++j)
	{
	    calc(board, j, 0, 0, 1, dotCnt, result);
	    calc(board, 0, j, 1, 0, dotCnt, result);
	}
	calc(board, 0, 0, 1, 1, dotCnt, result);
	calc(board, 0, 3, 1, -1, dotCnt, result);
	output << "Case #" << i + 1 << ": ";
	if (!result.empty())
	{
	    output << result;
	}
	else if (dotCnt > 0)
	{
	    output << "Game has not completed";
	}
	else
	{
	    output << "Draw";
	}
	output << std::endl;
    }
}
