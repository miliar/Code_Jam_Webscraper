/* 
 * File:   chicks.cpp
 * Author: wintokk
 *
 * Created on May 23, 2010, 1:38 AM
 */

#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, K, B, T;
/*
 * 
 */
int main(int argc, char** argv) {
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    int task;
    cin >> task;
    for (int tt = 1; tt <= task; tt++)
    {
        cout << "Case #" << tt << ": ";
        cin >> N >> K >> B >> T;
        vector<int> X(N), V(N);
        for (int i = 0; i < N; i++)
        {
            cin >> X[i];
        }
        for (int i = 0; i < N; i++)
            cin >> V[i];

        int sum = 0;
        vector<bool> can(N);
        vector<int> count;
        for (int i = 0; i < N; i++)
        {
            can[i] = X[i] + T * V[i] >= B;
            sum += (int)can[i];
        }
        if (sum < K)
        {
            cout << "IMPOSSIBLE\n";
            continue;
        }
        for (int i = 0; i < N; i++)
            if (can[i])
            {
                int tmp = 0;
                for (int j = 0; j < N; j++)
                    if (!can[j] && X[j] >= X[i])
                        ++tmp;
                count.push_back(tmp);
            }
        sort(count.begin(), count.end());
        sum = 0;
        for (int i = 0; i < K; i++)
            sum += count[i];
        cout << sum << endl;
    }
    

    return (EXIT_SUCCESS);
}