#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
#include <string.h>
#include <iomanip>


using namespace std;

int testIndex, testNum;
int n;
vector< vector < char > > a;

vector< double > res;
int winall, loseall;

void printInput()
{
    cout << n << "\n";
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
            cout << a[i][j];
        cout << "\n";
    }
}

void readInput()
{
    cin >> n;
    a.resize( n );
    for (int i = 0; i < n; ++i)
    {
        a[i].resize( n );
        for (int j = 0; j < n; ++j)
            cin >> a[i][j];
    }
}

void init()
{
    res.assign( n, 0 );
}

int valw( char c )
{
    if (c == '1') return 1;
    else return 0;
}

int vall( char c )
{
    if (c == '0') return 1;
    else return 0;
}


void compute()
{
    vector<int> win(n ,0 ),
                lose( n, 0);
    int winall = 0 , loseall = 0;
    vector<double> wp(n,0 );
    vector<double> owp(n,0);
    vector<double> oowp(n,0);

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
        {
            win[i] += valw( a[i][j] );
            winall += valw( a[i][j] );
            lose[i] += vall( a[i][j] );
            loseall += vall( a[i][j] );
        }

    for (int i = 0; i < n; ++i)
    {
        wp[i] = (double) win[i] / (win[i] + lose[i]);
    }

    for (int i = 0; i < n; ++i)
    {
        owp[i] = 0;
        int games = 0;
        for (int j = 0; j < n; ++j)
            if (a[i][j] != '.')
            {
                owp[i] += (double) (win[j] - valw( a[j][i] )) / (win[j] + lose[j] - 1 );
                ++games;
            }
        owp[i] /= games;
    }

    for (int i = 0; i < n; ++i)
    {
        int games = 0;
        oowp[i] = 0;
        for (int j = 0; j < n; ++j)
            if (a[i][j] != '.')
            {
                oowp[i] += owp[j];
                ++games;
            }
        oowp[i] /= games;
    }
    for (int i = 0; i < n; ++i)
        res[i] = wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25;
}

void output()
{
    cout << "Case #" << testIndex << ":\n";
    for (int i = 0; i < n; ++i)
        cout << setprecision(10) << res[i] << "\n";
}

int main()
{
    cin >> testNum;
    for (testIndex = 1; testIndex <= testNum; ++testIndex)
    {
        readInput();
        //printInput();
        init();
        compute();
        output();
    }
    return 0;
}
