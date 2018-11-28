#include <fstream>
#include <cstring>

using namespace std;

string s;
int i, j, completed, win, test, t, a[10][10];

int main()
{
    ifstream fi("test.in");
    ofstream fo("test.out");
    fi >> t;
    for(test = 1; test <= t; test++)
    {
        completed = 1;
        for(i = 1; i <= 4; i++)
        {
            fi >> s;
            for(j = 1; j <= 4; j++)
            {
                a[i][j] = s[j-1];
                if(a[i][j] == '.') completed = 0;
            }
        }
        win = 0;
        for(i = 1; i <= 4 and !win; i++)
        {
            win = 1;
            for(j = 1; j <= 4; j++) if(a[i][j] == '.' or a[i][j] == 'X') win = 0;
            if(win) break;
            win = 2;
            for(j = 1; j <= 4; j++) if(a[i][j] == '.' or a[i][j] == 'O') win = 0;
        }

        for(j = 1; j <= 4 and !win; j++)
        {
            win = 1;
            for(i = 1; i <= 4; i++) if(a[i][j] == '.' or a[i][j] == 'X') win = 0;
            if(win) break;
            win = 2;
            for(i = 1; i <= 4; i++) if(a[i][j] == '.' or a[i][j] == 'O') win = 0;
        }
        if(!win)
        {
            win = 1;
            for(i = 1; i <= 4; i++) if(a[i][i] == '.' or a[i][i] == 'X') win = 0;
        }
        if(!win)
        {
            win = 1; 
            for(i = 1; i <= 4; i++) if(a[i][5-i] == '.' or a[i][5-i] == 'X') win = 0;  
        }
        if(!win)
        {
            win = 2;
            for(i = 1; i <= 4; i++) if(a[i][i] == '.' or a[i][i] == 'O') win = 0;
        }
        if(!win)
        {
            win = 2;
            for(i = 1; i <= 4; i++) if(a[i][5-i] == '.' or a[i][5-i] == 'O') win = 0;
        }
        fo << "Case #" << test << ": "; 
        if(win == 1)  fo << "O won\n";
        if(win == 2) fo << "X won\n";
        if(win == 0 and completed) fo << "Draw\n";
        if(win == 0 and !completed) fo << "Game has not completed\n";
    }
}
