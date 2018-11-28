#include <iostream>
#include <string>

using std::cout;    using std::endl;

int main (void)
{
    int trials;
    std::cin >> trials;
    
    for (int i = 0; i < trials; i++)
    {
        char grid[4][4];
        for (int j = 0; j < 4; j++)
        {
            for (int k = 0; k < 4; k++)
            {
                std::cin >> grid[j][k];
            }
        }
        
        char win = 'e';
        for (int j = 0; j < 4; j++)
        {
            bool winner = true;
            char prev = grid[j][0];
            if (prev == '.')
            {
                continue;
            }

            if (prev == 'T')
                prev = grid[j][1];
            for (int k = 1; k < 4; k++)
            {
                char c = grid[j][k];
                if (c == '.')
                {   
                    winner = false;
                    break;
                }

                if (c != 'T' && c != prev)
                {
                    winner = false;
                    break;
                }
    
                if (c != 'T')
                    prev = c;
            }
            
            if (winner)
            {
                win = prev;
                break;
            }
        }
        
        if (win != 'e')
        {
            cout << "Case #" << i+1 << ": " << win << " won" << endl;
            continue;
        }

        for (int j = 0; j < 4; j++)
        {
            bool winner = true;
            char prev = grid[0][j];
            if (prev == '.')
            {
                continue;
            }
            if (prev == 'T')
                prev = grid[1][j];
            for (int k = 1; k < 4; k++)
            {
                char c = grid[k][j];
                if (c == '.')
                {
                    winner = false;
                    break;
                }

                if (c != 'T' && c != prev)
                {
                    winner = false;
                    break;
                }
    
                if (c != 'T')
                    prev = c;
            }
            
            if (winner)
            {
                win = prev;
                break;
            }
        }
        if (win != 'e')
        {
            cout << "Case #" << i+1 << ": " << win << " won" << endl;
            continue;
        }
        
        char prev = grid[0][0];
        if (prev == 'T')
            prev = grid[1][1];
        if (prev == '.') goto point1;
        for (int j = 1; j < 4; j++)
        {
            char c = grid[j][j];

            if (c == '.')
            goto point1;

            if (c != 'T' && c != prev)
                goto point1;
        }
        
    
        win = prev;
        cout << "Case #" << i+1 << ": " << win << " won" << endl;
        continue;
        point1:
        

        prev = grid[0][3];
        if (prev == 'T')
            prev = grid[1][2];
        if (prev == '.') goto point2;
        for (int j = 1; j < 4; j++)
        {
            char c = grid[j][3-j];

            if (c == '.')
                goto point2;

            if (c != 'T' && c != prev)
                goto point2;
        }
        
    
        win = prev;
        cout << "Case #" << i+1 << ": " << win << " won" << endl;
        continue;
        point2:;

        bool dot = false;
        for (int j = 0; j < 4; j++)
        {
            for (int k = 0; k < 4; k++)
            {
                if (grid[j][k] == '.')
                {
                    dot = true;
                    break;
                }
            }
            if (dot == true)
                break;
        }

        if (dot)
            cout << "Case #" << i+1 << ": " <<"Game has not completed" << endl;
        else
            cout << "Case #" << i+1 << ": " << "Draw" << endl;
    }
    return 0;
}
