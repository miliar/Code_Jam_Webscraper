/*
 * File:   main.cpp
 * Author: smirnovboris
 *
 * Created on 21 Май 2011 г., 16:51
 */
#include<stdio.h>
#include<iostream>
#include<string>
#include<vector>

using namespace std;
/*
 *
 */

typedef long double ld;

const double Eps = 1e-6;




int main(int argc, char ** argv) {

    int T;

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;

    for (int t = 0; t < T; ++ t)
    {
        bool T_T= false;
        int n, left, right;
        cin >> n >> left >> right;

        vector<int> a(n);
        for (int i = 0; i < n; ++ i)
            cin >> a[i];

        int ans = 0;
        for (int i = left; i <= right; ++ i)
        {
            bool T_T = false;
            for (int j = 0; j < n; ++ j)
                if (a[j] % i != 0 && i % a[j] != 0)
                    T_T = true;
            if (!T_T && ans == 0)
                ans = i;
        }
        cout << "Case #" << t + 1 << ": ";
        if (ans == 0)
            cout << "NO";
        else
            cout << ans;
        cout << '\n';
    }

    return 0;


}

