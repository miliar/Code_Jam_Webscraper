#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>

using namespace std;

int main()
{
    vector<string> board;
    int t;
    int r, c;
    string str;
    cin >> t;
    for (int ca = 1; ca <= t; ++ca)
    {
        cin >> r >> c;
        board.clear();
        for (int i = 0; i < r; ++i)
        {
            cin >> str;
            board.push_back( str );
        }
        bool flag = true;
        int cnt = 0;
        for (int i = 0; i < r; ++i)
        {
            for (int j = 0; j < c; ++j)
            {
                cnt = 0;
                while ( j < c && board[i][j] == '#' )
                {
                    cnt++;
                    ++j;
                }
                if ( cnt%2 != 0 )
                {
                    flag = false;
                    break;
                }
            }
            if ( !flag )
                break;
        }
        if ( flag )
        {
            for (int i = 0; i < c; ++i)
            {
                for (int j = 0; j < r; ++j)
                {
                    cnt = 0;
                    while ( j < r && board[j][i] == '#' )
                    {
                        cnt++;
                        j++;
                    }
                    if ( cnt%2 != 0 )
                    {
                        flag = false;
                        break;
                    }
                }
                if ( !flag )
                    break;
            }
        }
        printf("Case #%d:\n", ca);
        if ( !flag )
            printf("Impossible\n");
        else
        {
            for (int i = 0; i < r; ++i)
            {
                for (int j = 0; j < c; ++j)
                {
                    if ( board[i][j] == '#' )
                    {
                        board[i][j] = '/';
                        board[i+1][j] = '\\';
                        board[i][j+1] = '\\';
                        board[i+1][j+1] = '/';
                    }
                }
            }
            for (int i = 0; i < r; ++i)
            {
                for (int j = 0; j < c; ++j)
                    printf("%c", board[i][j]);
                printf("\n");
            }
        }
    }
    return 0;
}
