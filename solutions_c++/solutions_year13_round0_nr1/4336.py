#include <iostream>
#include <cstdio>

using namespace std;

bool compare(string S, string W)
{
    unsigned found = S.find('T');
    if(found!=string::npos)
    {
        S[found] = W[0];
    }
    return S==W;
}

int main()
{
    int t;
    cin >> t;
    for(int itr = 1; itr <= t; itr++)
    {
        string board[4];
        int i, j;
        for(i=0; i<4; i++)
            cin >> board[i];



        bool Xwon = false, Owon = false;
        for( i = 0; i < 4; i++)
        {
            if (compare(board[i], "XXXX"))
                Xwon = true;
            if (compare(board[i], "OOOO"))
                Owon = true;
        }

        for(i = 0; i< 4; i++)
        {
            string col(4, '.');
            for(j=0; j<4; j++)
                col[j] = board[j][i];
            if(compare(col, "XXXX")) Xwon = true;
            else if(compare(col, "OOOO")) Owon = true;
        }

        string md(4, '.'), od(4, '.');
        for(i=0; i<4; i++)
        {
            md[i] = board[i][i];
            od[i] = board[i][3-i];
        }
        if(compare(md, "XXXX") || compare(od, "XXXX")) Xwon = true;
        if(compare(md, "OOOO") || compare(od, "OOOO")) Owon = true;

        if(Xwon)
            printf("Case #%d: X won\n", itr);
        else if(Owon)
            printf("Case #%d: O won\n", itr);
        else{

        bool complete = true;
        for(i = 0; i < 4; i ++)
        {
            for(j=0; j<4; j++)
                if(board[i][j] == '.')
                    complete = false;
        }
        if(!complete)
            printf("Case #%d: Game has not completed\n", itr);
        else
            printf("Case #%d: Draw\n", itr);

        }

    }
    return 0;
}
