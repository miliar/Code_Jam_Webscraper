#include <iostream>


char bx[4][4];
char by[4][4];

int main(void)
{
    int runs;
    std::cin >> runs;

    for(int r = 0; r < runs; ++r)
    {
        //Read board
        for(int i = 0; i < 4; ++i)
        {
            for(int j = 0; j < 4; ++j)
            {
                std::cin >> bx[i][j];
                by[i][j] = bx[i][j];
                if(bx[i][j] == 'T')
                {
                    bx[i][j] = 'X';
                    by[i][j] = 'O';
                }
            }
        }

        bool incompleteGame = false;
        bool won1 = false;
        bool won2 = false;
        for(int i = 0; i < 4; i++)
        {
            bool allX = true;
            bool allY = true;
            for(int j = 0; j < 4; j++)
            {
                if(bx[i][j] != 'X')
                    allX = false;
                if(by[i][j] != 'O')
                    allY = false;
                if(bx[i][j] == '.')
                    incompleteGame = true;
            }
            if(allX)
                won1 = true;
            if(allY)
                won2 = true;
            if(won1 || won2)
                break;
        }
        for(int i = 0; i < 4; i++)
        {
            bool allX = true;
            bool allY = true;
            for(int j = 0; j < 4; j++)
            {
                if(bx[j][i] != 'X')
                    allX = false;
                if(by[j][i] != 'O')
                    allY = false;
            }
            if(allX)
                won1 = true;
            if(allY)
                won2 = true;
            if(won1 || won2)
                break;
        }
        if(bx[0][0] == 'X' && bx[1][1] == 'X' && bx[2][2] == 'X' && bx[3][3] == 'X')
            won1 = true;
        else if(by[0][0] == 'O' && by[1][1] == 'O' && by[2][2] == 'O' && by[3][3] == 'O')
            won2 = true;
        else if(by[3][0] == 'O' && by[2][1] == 'O' && by[1][2] == 'O' && by[0][3] == 'O')
            won2 = true;
        else if(bx[3][0] == 'X' && bx[2][1] == 'X' && bx[1][2] == 'X' && bx[0][3] == 'X')
            won1 = true;

        std::cout << "Case #" << r+1 << ": ";
        if(won1)
            std::cout << "X won" << std::endl;
        else if(won2)
            std::cout << "O won" << std::endl;
        else if(incompleteGame)
            std::cout << "Game has not completed" << std::endl;
        else
            std::cout << "Draw" << std::endl;
    }

	return 0;
}

