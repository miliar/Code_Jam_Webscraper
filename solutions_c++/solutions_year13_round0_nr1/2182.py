#include <iostream>
#include <vector>
#include <string>
#include <limits>

using namespace std;

bool is_boardfull(const vector<string>& tab)
{
    for (auto& s : tab)
    {
        for (auto c : s)
        {
            if (c == '.')
            {
                return false;
            }
        }
    }
    
    return true;
}

bool player_won(const vector<string>& tab, char player)
{
    int numP = 0;
    int numT = 0;
    
    for (int i=0;i<4;++i)
    {
        numP = 0;
        numT = 0;
        for (int j=0;j<4;++j)
        {
            if (tab[i][j] == player)
            {
                ++numP;
            }
            else if (tab[i][j] == 'T')
            {
                ++numT;
            }
        }
        
        if ((numP == 4) || (numP == 3 && numT == 1))
        {
            return true;
        }
    }
    
    for (int j=0;j<4;++j)
    {
        numP = 0;
        numT = 0;
        for (int i=0;i<4;++i)
        {
            if (tab[i][j] == player)
            {
                ++numP;
            }
            else if (tab[i][j] == 'T')
            {
                ++numT;
            }
        }
        
        if ((numP == 4) || (numP == 3 && numT == 1))
        {
            return true;
        }
    }
    
    numP = 0;
    numT = 0;
    for (int i=0;i<4;++i)
    {
            if (tab[i][i] == player)
            {
                ++numP;
            }
            else if (tab[i][i] == 'T')
            {
                ++numT;
            }
    }
    
        if ((numP == 4) || (numP == 3 && numT == 1))
        {
            return true;
        }
        
    numP = 0;
    numT = 0;
    for (int i=0;i<4;++i)
    {
            if (tab[i][3-i] == player)
            {
                ++numP;
            }
            else if (tab[i][3-i] == 'T')
            {
                ++numT;
            }
    }
    
        if ((numP == 4) || (numP == 3 && numT == 1))
        {
            return true;
        }
    
    return false;
}

int main()
{
    int t;
    cin >> t;

    for (int lp=1;lp<=t;++lp)
    {
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        vector<string> tab(4);
        for (auto& s : tab)
        {
            getline(cin, s);
        }
        
        string ret = "Game has not completed";
        if (player_won(tab, 'X'))
        {
            ret = "X won";
        }
        else if (player_won(tab, 'O'))
        {
            ret = "O won";
        }
        else if (is_boardfull(tab))
        {
            ret = "Draw";
        }
        
        cout << "Case #" << lp << ": " << ret << "\n";
    }
    
    return 0;
}