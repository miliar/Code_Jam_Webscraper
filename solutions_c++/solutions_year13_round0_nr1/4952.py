#include<iostream>
#include<cstdio>
#include<cstdlib>

char board[5][5];

void read()
{
    for(int i=0; i<4; ++i)
        scanf("%s", &board[i]);

}

bool inrow(int &r, char &ch)
{
    int i=0;
    bool flag = false;
    for(i=0; i<4; ++i)
    {
        if(board[r][i] != ch)
        {
            if(board[r][i] == 'T' && !flag)
                flag = true;
            else return false;
        }
    }
    return true;
}

bool incol(int &c, char &ch)
{
    int i=0;
    bool flag = false;
    for(i=0; i<4; ++i)
    {

        if(board[i][c] != ch)
        {
            if(board[i][c] == 'T' && !flag)
                flag = true;
            else return false;
        }
    }
    return true;
}

bool diag(char &ch)
{
    int i=0;
    bool flag = false;
    for(i=0; i<4; ++i)
        if(board[i][i]!=ch)
        {
            if(board[i][i]=='T' &&!flag)
                flag = true;
            else goto DIA_COL;
        }

    return true;
DIA_COL:
    flag = false;
    for(i=0; i<4; ++i)
        if(board[i][3-i]!= ch)
        {
            if(board[i][3-i]=='T' &&!flag)
                flag = true;
            else return false;
        }
    return true;
}
bool iswin(char ch)
{
    int i=0;
    for(i=0; i<4; ++i)
    {
        if( inrow(i, ch) )
            return true;
        if( incol(i, ch) )
            return true;
    }
    if( diag(ch) ) return true;
    return false;
}
bool cont(char  ch)
{
    for(int i(0); i<4; ++i)
        for(int j(0); j<4; ++j)
            if(board[i][j] == '.') return true;
    return false;
}
void solve(int k)
{
    if(iswin('X'))
        printf("Case #%d: X won\n", k);
    else if( iswin('O') )
        printf("Case #%d: O won\n", k);
    else if( cont('.'))
        printf("Case #%d: Game has not completed\n", k);
    else printf("Case #%d: Draw\n", k);

}
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("a_s.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int i=0; i<t; )
    {
        read();
        solve(++i);
    }
    return 0;
}
