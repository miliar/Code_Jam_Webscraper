/*
    Aleksandar "Al3kSaNdaR" Ivanović

    Problem A. Tic-Tac-Toe-Tomek
*/
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <bitset>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <vector>
#include <numeric>
#include <sstream>
#include <iomanip>
#include <cstdlib>
#include <ctime>
#include <utility>
#include <functional>

#define pb push_back
#define sz size
#define for_each(it, X) for (__typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)

using namespace std;

typedef long long int lld;
typedef pair < int, int > pii;

int T;
char S[1 << 3][1 << 3];

int main ( void )
{
    //freopen ( "A-small-attempt0.in", "r", stdin );
    //freopen ( "A-small-attempt0.out", "w", stdout );
    freopen ( "A-large.in", "r", stdin );
    freopen ( "A-large.out", "w", stdout );

    scanf ( "%d", &T );
    for ( int __T = 1; __T <= T; __T++ )
    {
        int Cnt = 0;
        for ( int i = 0; i < 4; i++ )
        {
            scanf ( " %s", S[i] );
            for ( int j = 0; j < 4; j++ ) if ( S[i][j] != '.' ) Cnt++;
        }

        bool WonX = false, WonO = false;

        for ( int i = 0; i < 4; i++ )
        {
            bool AllX = true, AllO = true;
            for ( int j = 0; j < 4; j++ )
            {
                AllX &= S[i][j] == 'X' || S[i][j] == 'T';
                AllO &= S[i][j] == 'O' || S[i][j] == 'T';
            }

            WonX |= AllX;
            WonO |= AllO;
        }

        for ( int j = 0; j < 4; j++ )
        {
            bool AllX = true, AllO = true;
            for ( int i = 0; i < 4; i++ )
            {
                AllX &= S[i][j] == 'X' || S[i][j] == 'T';
                AllO &= S[i][j] == 'O' || S[i][j] == 'T';
            }

            WonX |= AllX;
            WonO |= AllO;
        }

        bool D1X = true, D1O = true;
        for ( int i = 0; i < 4; i++ )
        {
            D1X &= S[i][i] == 'X' || S[i][i] == 'T';
            D1O &= S[i][i] == 'O' || S[i][i] == 'T';
        }

        WonX |= D1X;
        WonO |= D1O;

        bool D2X = true, D2O = true;
        for ( int i = 0; i < 4; i++ )
        {
            D2X &= S[i][3 - i] == 'X' || S[i][3 - i] == 'T';
            D2O &= S[i][3 - i] == 'O' || S[i][3 - i] == 'T';
        }

        WonX |= D2X;
        WonO |= D2O;

        if ( Cnt == 16 && ! WonX && ! WonO ) WonX = true, WonO = true;

        printf ( "Case #%d: ", __T );
        if ( WonX && WonO ) printf ( "Draw\n" );
        else if ( WonX ) printf ( "X won\n" );
             else if ( WonO ) printf ( "O won\n" );
                  else printf ( "Game has not completed\n" );
    }

    return 0;
}
