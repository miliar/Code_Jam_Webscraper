#include <iostream>
#include <fstream>

using namespace std;

char checkBoard(char board[4][4])
{
	int lines[10][4][2] = {{{0,0},{0,1},{0,2},{0,3}},
                           {{1,0},{1,1},{1,2},{1,3}},
                           {{2,0},{2,1},{2,2},{2,3}},
                           {{3,0},{3,1},{3,2},{3,3}},
                           {{0,0},{1,0},{2,0},{3,0}},
                           {{0,1},{1,1},{2,1},{3,1}},
                           {{0,2},{1,2},{2,2},{3,2}},
                           {{0,3},{1,3},{2,3},{3,3}},
                           {{0,0},{1,1},{2,2},{3,3}},
                           {{0,3},{1,2},{2,1},{3,0}}};

	for(int i=0;i<10;i++)
	{
	    char c[4];
	    for(int j=0;j<4;j++)
        {
            c[j] = board[lines[i][j][0]][lines[i][j][1]];
        }
        char t = (c[0] == 'T')?c[1] : c[0];
        bool flag = true;
        for(int j=0;j<4;j++)
        {
            if(c[j] == 'T')
                continue;
            if(c[j] != t)
            {
                flag = false;
                break;
            }
        }

        if(flag && t != '.')
            return t;
	}

	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(board[i][j] == '.')
				return 'N';
		}
	}

	return 'D';
}

int main()
{
    ifstream datafile("A-large.in");
    ofstream output("A-large.out");
    char board[4][4];
    int T;
    datafile>>T;
    for(int k=1;k<=T;k++)
    {
        //read board
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                datafile>>board[i][j];
            }
        }
        char result = checkBoard(board);
        switch(result)
        {
        case 'X':
            output<<"Case #"<<k<<": X won"<<endl;
            break;
        case 'O':
            output<<"Case #"<<k<<": O won"<<endl;
            break;
        case 'D':
            output<<"Case #"<<k<<": Draw"<<endl;
            break;
        case 'N':
            output<<"Case #"<<k<<": Game has not completed"<<endl;
        }
    }

    return 0;
}
