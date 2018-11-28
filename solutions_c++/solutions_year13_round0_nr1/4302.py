#include<iostream>
#include<string>

using namespace std;

string s[4];

bool check_win(char c)
{
    int t;
    bool win;
    for (int i=0;i<4;i++)
    {
        t = 0;
        win = true;
        for (int j=0;j<4 && win && t <= 1;j++)
        {
            if (s[i][j] == 'T')
                t++;
            else if (s[i][j] != c)
                win = false;
            
        }
        if (win && t <= 1)
            return true;
        
        t = 0;
        win = true;
        for (int j=0;j<4 && win && t <= 1;j++)
        {
            if (s[j][i] == 'T')
                t++;
            else if (s[j][i] != c)
                win = false;
            
        }
        if (win && t <= 1)
            return true;
        
        t = 0;
        win = true;
        for (int j=0;j<4 && win && t <= 1;j++)
        {
            if (s[j][j] == 'T')
                t++;
            else if (s[j][j] != c)
                win = false;
        }
        if (win && t <= 1)
            return true;
        
        t = 0;
        win = true;
        for (int j=0;j<4 && win && t <= 1;j++)
        {
            if (s[j][3-j] == 'T')
                t++;
            else if (s[j][3-j] != c)
                win = false;
        }
        if (win && t <= 1)
            return true;
        
    }
}

int main()
{
    int n;
    cin>>n;
    
    for (int o=0;o<n;o++)
    {
        cout<<"Case #"<<o+1<<": ";
        for (int i=0;i<4;i++)
            cin>>s[i];
        bool Xwin = check_win('X');
        bool Owin = check_win('O');
        bool Draw = !Xwin && !Owin;
        for (int i=0;i<4 && Draw;i++)
            for (int j=0;j<4 && Draw;j++)
                if (s[i][j] == '.')
                    Draw = false;
        if (Xwin)
            cout<<"X won"<<endl;
        else if (Owin)
            cout<<"O won"<<endl;
        else if (Draw)
            cout<<"Draw"<<endl;
        else 
            cout<<"Game has not completed"<<endl;
    }
    return 0;
}
