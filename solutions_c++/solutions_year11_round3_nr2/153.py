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

int L, N, C;
double t;
vector<int> a;
vector<double> d;
double total;

void printInput()
{
    cout << " " << L << " " << t << " " << N << " " << C;
    REP(i,C)
        cout << " " << a[i];
    cout << "\n";
}

void readInput()
{
    cin >> L >> t >> N >> C;
    a.assign( C, 0 );
    REP(i,C)
        cin >> a[i];
}

void init()
{

}

void compute()
{
    d.assign( N, 0 );
    total = 0;
    REP(i,N)
    {
        d[i] = a[i % C];
        total += d[i] * 2;
    }

    if (total <= t) return;

    int first = 0;
    double sum_first = d[0] * 2;
    while (sum_first <= t && first < N)
    {
        ++first;
        sum_first += d[first] * 2;
    }

    if (first >= N) return;

    d[first] = (sum_first - t) / 2;

    sort( d.begin() + first, d.end());
    REP(i,L)
        if (N - 1 - i >= first)
            total -= d[N-1-i];
}

void output()
{
    cout << "Case #" << testIndex << ": " << setprecision( 15 ) << total;
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

