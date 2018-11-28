#include<iostream>

int main()
{
    int T; std::cin >> T;
    for(int j = 0; j < T; j++)
    {
        int R, C; std::cin >> R >> C;
        char tab[50][50];
        for(int i = 0; i < R; i++)
            for(int j = 0; j < C; j++)
                std::cin >> tab[i][j];
        bool impossible = 0;
        for(int i = 0; i < R && !impossible; i++)
            for(int j = 0; j < C && !impossible; j++)
            {
                if(tab[i][j] == '#')
                {
                    if((i+1 >= R)||(j+1 >= C)) {impossible = 1; break;}
                    if(tab[i][j+1] == '#' && tab[i+1][j] == '#' && tab[i+1][j+1] == '#')
                    {
                        tab[i][j] = '/';
                        tab[i][j+1] = '\\';
                        tab[i+1][j] = '\\';
                        tab[i+1][j+1] = '/';
                        //i++;
                        
                        continue;
                    }
                    else {impossible = 1; break;}
                }
            }
        
        std::cout << "Case #" << j+1 << ":\n";
        if(impossible)
            std::cout << "Impossible\n";
        else
        for(int i = 0; i < R; i++)
            {for(int j = 0; j < C; j++)
                std::cout << tab[i][j]; std::cout << '\n';}
    }
    return 0;
}
