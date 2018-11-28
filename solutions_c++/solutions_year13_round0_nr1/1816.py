#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct esac
{
    string f[4];

    void read()
    {
        cin >> f[0];
        cin >> f[1];
        cin >> f[2];
        cin >> f[3];
    }

    bool check_vert(char p, int col)
    {
        for (int i = 0; i < 4; ++i)
            if ( f[i][col] != p )
                if ( f[i][col] != 'T' )
                    return false;
        return true;
    }

    bool check_horiz(char p, int row)
    {
        for (int i = 0; i < 4; ++i)
            if ( f[row][i] != p )
                if ( f[row][i] != 'T' )
                    return false;
        return true;
    }

    bool check_left_diag(char p)
    {
        for (int i = 0; i < 4; ++i)
            if ( f[i][i] != p )
                if ( f[i][i] != 'T' )
                    return false;
        return true;
    }

    bool check_right_diag(char p)
    {
        for (int i = 0; i < 4; ++i)
            if ( f[3 - i][i] != p )
                if ( f[3 - i][i] != 'T' )
                    return false;
        return true;
    }

    bool have_empty_cells()
    {
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                if ( f[i][j] == '.' )
                    return true;
        return false;
    }

    void print_answer()
    {
        int X_win = 0, O_win = 0;

        X_win += check_left_diag('X') + check_right_diag('X');
        O_win += check_left_diag('O') + check_right_diag('O');

        for (int i = 0; i < 4; ++i)
        {
            X_win += check_horiz('X', i) + check_vert('X', i);
            O_win += check_horiz('O', i) + check_vert('O', i);
        }

        if ( X_win > 0 )
        {
            printf("X won\n");
            return;
        }

        if ( O_win > 0 )
        {
            printf("O won\n");
            return;
        }

        // else...

        if ( have_empty_cells() )
            printf("Game has not completed\n");
        else
            printf("Draw\n");

    }

};

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T; cin >> T;
    esac es;

    for (int i = 0; i < T; ++i)
    {
        es.read();

        printf("Case #%d: ", i + 1);
        es.print_answer();
    }

    fclose(stdout);
    return 0;
}
