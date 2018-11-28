/* 
 * File:   newmain.cpp
 * Author: wintokk
 *
 * Created on June 5, 2010, 11:20 PM
 */

#include <stdlib.h>
#include <iostream>
using namespace std;

#define easy 1
#define MAX_P 10

int P, M[1<<MAX_P], price[MAX_P][1<<MAX_P];

int solve_easy(int k, int s, int t)
{
    if (k < 0) return 0;
    int ret = 0;
    for (int i = s; i < t; i++)
        if (M[i] > 0)
        {
            for (int j = i; j < t; j++)
                if (M[j] > 0)
                    --M[j];
            ret = 1;
            break;
        }
    if (ret == 0) return 0;
    return ret + solve_easy(k - 1, s, s + (1<<k)) + solve_easy(k - 1, s + (1<<k), t);
}

int main(int argc, char** argv) {
    int task;
    cin >> task;
    for (int tt = 1; tt <= task; tt++)
    {
        cout << "Case #" << tt << ": ";
        cin >> P;
        for (int i = 0; i < (1<<P); i++)
        {
            cin >> M[i];
            M[i] = P - M[i];
        }
        for (int i = P -1 ; i >= 0; i--)
            for (int j = 0; j < (1<<i); j++)
                cin >> price[i][j];
        if (easy)
        {
            int ret = solve_easy(P - 1, 0, (1<<P));
            cout << ret;
        }
        else
        {
        }
        cout << endl;
    }
    return (EXIT_SUCCESS);
}

