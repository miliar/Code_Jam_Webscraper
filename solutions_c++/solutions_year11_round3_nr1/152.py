#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
#include <string.h>
#include <iomanip>

using namespace std;

#define REP(i,n) for (int i = 0; i < n; ++i)
#define REPAB(i,a,n) for (int i = a; i < b; ++i)
#define MIN2(a,b) ((a) < (b) ? (a) : (b))
#define MAX2(a,b) ((a) > (b) ? (a) : (b))

int testIndex, testNum;

vector< vector< char > > a;
bool impossible;
int m,n;

void printInput()
{
    cout << m  << " " <<  n << "\n";
    REP(i,m+2)
    {
        REP(j,n+2) cout << a[i][j];
        cout << "\n";
    }
}

void readInput()
{
    cin >> m >> n;
    a.resize( m + 2 );
    REP(i,m)
    {
        a[i].assign( n + 2, '.' );
        REP(j,n) cin >> a[i][j];
    }
    a[m].assign(n+2,'.');
    a[m+1].assign(n+2,'.');
}

void init()
{

}

void compute()
{
    impossible = true;
    REP(i,m)
        REP(j,n)
        {
            if (a[i][j] == '#')
            {
                if (a[i][j+1] != '#' ||
                    a[i+1][j] != '#' ||
                    a[i+1][j+1] != '#')
                {
                    return;
                }
                a[i][j] = '/';
                a[i][j+1] = '\\';
                a[i+1][j] = '\\';
                a[i+1][j+1] = '/';
            }
        }
    impossible = false;
}

void output()
{
    cout << "Case #" << testIndex << ":\n";
    if (impossible)
    {
        cout << "Impossible\n";
    }
    else
    {
        REP(i,m)
        {
            REP(j,n)
                cout << a[i][j];
            cout << "\n";
        }
    }
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
