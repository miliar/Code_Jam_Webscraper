/* 
 * File:   r2_c.cpp
 * Author: yujw
 *
 * Created on May 22, 2010, 10:13 AM
 */

#include <stdlib.h>
#include <iostream>
using namespace std;

inline void swap(int &a, int &b)
{
    int c = a;
    a = b;
    b = c;
}

void ext_gcd(int a, int b, int &c)
{
    while (1)
    {
        if (a < b) swap(a, b);
        if (a / b > 1) return;
        if (a == b)
        {
            c = 1 - c;
            return;
        }
        c = 1 - c;
        a = a % b;
    }
}

/*
 * 
 */
int main(int argc, char** argv) {
    int task, a1, a2, b1, b2;
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    cin >> task;
    for (int tt = 1; tt <= task; tt++)
    {
        cin >> a1 >> a2 >> b1 >> b2;
        long long count = 0;
        for (int a = a1; a <= a2; a++)
            for (int b = b1; b <= b2; b++)
            {
                int c = 0;
                ext_gcd(a, b, c);
                count += (c==0);
            }
        cout << "Case #" << tt << ": " << count << endl;
    }

    return (EXIT_SUCCESS);
}

