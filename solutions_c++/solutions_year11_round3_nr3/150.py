#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
#include <string.h>
#include <iomanip>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i = 0; i < n; ++i)
#define REPAB(i,a,n) for (int i = a; i < b; ++i)
#define MIN2(a,b) ((a) < (b) ? (a) : (b))
#define MAX2(a,b) ((a) > (b) ? (a) : (b))

int testIndex, testNum;

vector< long long > a;
long long L, H;
int N;

bool yes;
long long res;

void printInput()
{
    cout << " " << N << " " << L << " " << H << "\n";
    a.resize( N );
    REP(i,N)
        cout << " " << a[i];
    cout << "\n";
}

void readInput()
{
    cin >> N >> L >> H;
    a.resize( N );
    REP(i,N)
        cin >> a[i];
}

void init()
{

}

long long lcd(long long a, long long b)
{
    if (a == 0) return b;
    if (b == 0) return a;
    do
    {
        if (a < b)
        {
            long long tmp = a;
            a = b;
            b = tmp;
        }
        a = a % b;
    } while (a != 0);
    return b;
}


long long scm( long long a, long long b )
{
    if (a == 0 || b == 0) return 0;
    if ((double) a * b / lcd( a,b ) >= 1e16) return 0;
    return (a / lcd( a,b ) * b);
}

void compute()
{
    yes = false;
    sort( a.begin(), a.end() );
    long long scmall = 1;
    vector<long long> scms;
    vector<long long> lcds;
    scms.assign( N + 1, 0 );
    lcds.assign( N + 1, 0 );
    REP(i,N)
    {
        scms[i] = scmall;
        scmall = scm( scmall, a[i] );
        //cout << scmall << " ";
    }
    scms[N] = scmall;


    long long lcdall = a[N-1];
    for (int i = N - 1; i >= 0; --i)
    {
        lcdall = lcd( lcdall, a[i]);
        lcds[i] = lcdall;
    }
    lcds[N] = 0;

/*
    REP(i,N+1)
        cout << lcds[i] << " ";
    cout << "\n";

    REP(i,N+1)
        cout << scms[i] << " ";
    cout << "\n";
*/
    REP(i,N+1)
    {
        if (scms[i] != 0)
        {
            if (lcds[i] % scms[i] == 0)
            {
                long long r = lcds[i] / scms[i];
                long long lr = (L - 1) / scms[i] + 1;
                long long hr = H / scms[i];
                //cout << i << " " << r << " " << lr << " " << hr <<"\n";
                for (long long j = lr; j <= hr; ++j)
                    if (r % j == 0)
                    {
                        res = j * scms[i];
                        yes = true;
                        return;
                    }
            }
        }
    }
}

void output()
{
    cout << "Case #" << testIndex << ": ";
    if (yes) cout << res;
    else cout << "NO";
    cout << "\n";
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

