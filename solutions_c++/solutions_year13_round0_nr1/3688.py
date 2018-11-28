#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

char maze[5][5];

int Check(char ch)
{
    for (int i = 0; i < 4; i++)
    {
        int s1 = 0, s2 = 0;
        for (int j = 0; j < 4; j++)
        {
            if (maze[i][j] == ch || maze[i][j] == 'T') s1++;
            if (maze[j][i] == ch || maze[j][i] == 'T') s2++;
        }
        if (s1 == 4 || s2 == 4) return 1;
    }

    int s1 = 0, s2 = 0;
    for (int i = 0; i < 4; i++)
        if (maze[i][i] == ch || maze[i][i] == 'T') s1++;
    for (int i = 0, x = 0, y = 3; i < 4; i++, x++, y--)
        if (maze[x][y] == ch || maze[x][y] == 'T') s2++;
    if (s1 == 4 || s2 == 4) return 1;
    return 0;
}

int Fill()
{
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if (maze[i][j] == '.') return 0;
    return 1;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin>>T;
    for (int Case = 1; Case <= T; Case++)
    {
        for (int i = 0; i < 4; i++)
            cin>>maze[i];
        cout<<"Case #"<<Case<<": ";
        if (Check('X'))
            cout<<"X won"<<endl;
        else if (Check('O'))
            cout<<"O won"<<endl;
        else if (Fill())
            cout<<"Draw"<<endl;
        else
            cout<<"Game has not completed"<<endl;
    }
    return 0;
}
