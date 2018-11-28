#include <iostream>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
using namespace std;

void solve()
{
    char board[4][4];
    for(size_t i=0; i < 4; i++)
    for(size_t j=0; j < 4; j++)
    {
        while(std::cin.peek() == '\n'
        || std::cin.peek() == ' '
        || std::cin.peek() == '\r'
) std::cin.get();
        board[i][j] = std::cin.get();
    }

    for(size_t i=0; i < 4; i++)
    {
        char o = 'T';
        int c = 0;
        for(size_t j=0; j < 4; j++)
        {
            char oo = board[i][j];
            if(o == 'T') o = oo;
            if(oo != o && oo != 'T') o = oo, c = 0;

            c++;

            if(c == 4 && (o == 'O' || o == 'X'))
            {
                std::cout << o << " won";
                return;
            }
        }
    }

    for(size_t i=0; i < 4; i++)
    {
        char o = 'T';
        int c = 0;
        for(size_t j=0; j < 4; j++)
        {
            char oo = board[j][i];
            if(o == 'T') o = oo;
            if(oo != o && oo != 'T') o = oo, c = 0;

            c++;

            if(c == 4 && (o == 'O' || o == 'X'))
            {
                std::cout << o << " won";
                return;
            }
        }
    }

    {
        char o = 'T';
        int c = 0;
        for(size_t j=0; j < 4; j++)
        {
            char oo = board[j][j];
            if(o == 'T') o = oo;
            if(oo != o && oo != 'T') o = oo, c = 0;

            c++;

            if(c == 4 && (o == 'O' || o == 'X'))
            {
                std::cout << o << " won";
                return;
            }
        }
    }

    {
        char o = 'T';
        int c = 0;
        for(size_t j=0; j < 4; j++)
        {
            char oo = board[j][3-j];
            if(o == 'T') o = oo;
            if(oo != o && oo != 'T') o = oo, c = 0;

            c++;

            if(c == 4 && (o == 'O' || o == 'X'))
            {
                std::cout << o << " won";
                return;
            }
        }
    }

    for(size_t i=0; i < 4; i++)
    for(size_t j=0; j < 4; j++)
        if(board[i][j] == '.')
        {
            std::cout << "Game has not completed";
            return;
        }

    std::cout << "Draw";
}

int main()
{
	size_t n;
	std::cin >> n;
	while(std::cin.get() != '\n');
	for(size_t i=1; i <= n; i++)
	{
		std::cout << "Case #" << i << ": ";
		solve();
		std::cout << std::endl;
	}
}
