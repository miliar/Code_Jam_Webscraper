#include <iostream>

bool winning_char(const char c, char e)
{
    if(e == c || e == 'T')
        return true;
    else
        return false;
}

struct board{
    char x[4][5];
    void read()
    {
        std::cin >> x[0];
        std::cin >> x[1];
        std::cin >> x[2];
        std::cin >> x[3];
    }
    void state();
    board()
    {
        this->read();
    }
    void d_print()
    {
        std::cout << x[0] << '\n';
        std::cout << x[1] << '\n';
        std::cout << x[2] << '\n';
        std::cout << x[3] << '\n';
    }
};


void board::state()
{
    for(int i = 0; i < 4; i++)
        if(winning_char('X', x[i][0])
        && winning_char('X', x[i][1])
        && winning_char('X', x[i][2])
        && winning_char('X', x[i][3]))
        {
            std::cout << "X won\n";
            return;
        }

    for(int i = 0; i < 4; i++)
        if(winning_char('X', x[0][i])
        && winning_char('X', x[1][i])
        && winning_char('X', x[2][i])
        && winning_char('X', x[3][i]))
        {
            std::cout << "X won\n";
            return;
        }

    for(int i = 0; i < 4; i++)
        if(winning_char('O', x[i][0])
        && winning_char('O', x[i][1])
        && winning_char('O', x[i][2])
        && winning_char('O', x[i][3]))
        {
            std::cout << "O won\n";
            return;
        }

    for(int i = 0; i < 4; i++)
        if(winning_char('O', x[0][i])
        && winning_char('O', x[1][i])
        && winning_char('O', x[2][i])
        && winning_char('O', x[3][i]))
        {
            std::cout << "O won\n";
            return;
        }

    if(winning_char('X', x[0][0])
    && winning_char('X', x[1][1])
    && winning_char('X', x[2][2])
    && winning_char('X', x[3][3]))
    {
        std::cout << "X won\n";
        return;
    }

    if(winning_char('O', x[0][0])
    && winning_char('O', x[1][1])
    && winning_char('O', x[2][2])
    && winning_char('O', x[3][3]))
    {
        std::cout << "O won\n";
        return;
    }

    if(winning_char('O', x[0][3])
    && winning_char('O', x[1][2])
    && winning_char('O', x[2][1])
    && winning_char('O', x[3][0]))
    {
        std::cout << "O won\n";
        return;
    }

    if(winning_char('X', x[0][3])
    && winning_char('X', x[1][2])
    && winning_char('X', x[2][1])
    && winning_char('X', x[3][0]))
    {
        std::cout << "X won\n";
        return;
    }

    for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            if(x[i][j] == '.')
            {
                std::cout << "Game has not completed\n";
                return;
            }

    std::cout << "Draw\n";
}


int main()
{
    int num_cases;
    std::cin >> num_cases;
    board * b = new board[num_cases];
    for(int i = 0; i < num_cases; i++)
    {

        std::cout << "Case #" << i + 1 << ": ";
        //b[i].d_print();
        b[i].state();
    }
    delete[] b;
    return 0;
}