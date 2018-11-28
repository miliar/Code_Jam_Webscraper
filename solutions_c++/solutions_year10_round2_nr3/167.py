/* 
 * File:   pure.cpp
 * Author: wintokk
 *
 * Created on May 23, 2010, 12:45 AM
 */

#include <stdlib.h>
#include <iostream>
using namespace std;

#define MAX_N 501
#define MOD 100003

int n;
int F[MAX_N];
int G[MAX_N][MAX_N];
long long binom[MAX_N][MAX_N];

inline void addup(int &sum, int mul, int total, int choose)
{
    if (total < choose || choose < 0) return;
    sum += (mul * binom[total][choose]) % MOD;
    if (sum >= MOD) sum -= MOD;
}

int main(int argc, char** argv) {

    binom[0][0] = 1;
    for (int i = 1; i < MAX_N; i++)
    {
        binom[i][0] = 1;
        for (int j = 1; j <= i; j++)
        {
            if ((binom[i][j] = binom[i-1][j] + binom[i-1][j-1]) >= MOD)
                binom[i][j] -= MOD;
        }
    }

    F[2] = 1;
    G[2][1] = 1;
    
    for (n = 3; n < MAX_N; n++)
    {
        F[n] = 1;
        G[n][1] = 1;
        for (int rank = 2; rank <= n; rank ++)
        {
            G[n][rank] = 0;
            for (int i = 1; i < rank; i++)
                addup(G[n][rank], G[rank][i], n - rank - 1, rank - i - 1);
            F[n] += G[n][rank];
            if (F[n] >= MOD) F[n] -= MOD;
        }
    }

    int task;
    freopen("b.in", "r", stdin);
    freopen("b.out", "w",stdout);
    cin >> task;
    for (int tt = 1; tt <= task; tt++)
    {
        cin >> n;
        cout << "Case #" << tt << ": " << F[n] << endl;
    }
    return (EXIT_SUCCESS);
}

