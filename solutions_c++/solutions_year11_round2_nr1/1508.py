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
int main(int argc, char ** argv) {

    int T;

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;

    for (int t = 0; t < T; ++ t)
    {
        int n;
        cin >> n;
        vector<string> a(n);
        for (int i = 0; i < n; ++ i)
            cin >> a[i];

        vector<ld> WP(n);

        for (int i = 0; i < n; ++ i)
        {
            int m = 0;
            ld Sum = 0.;
            for (int j = 0; j < n; ++ j)
            {
                if (a[i][j] == '.')
                    continue;
                ++ m;
                Sum += (a[i][j] == '1') ? 1. : 0.;
            }
            WP[i] = Sum / m;
        }

        vector<ld> OWP(n);
        for (int i = 0; i < n; ++ i)
        {
            int m = 0;
            ld Sum = 0.;

            for (int j = 0; j < n; ++ j)
            {
                if (a[i][j] == '.')
                    continue;
                m ++;
                int m1 = 0;
                ld Sum1 = 0.;
                for (int k = 0; k < n; ++ k)
                {
                    if (k == i || a[k][j] == '.')
                        continue;
                    m1 ++;
                    Sum1 += (a[j][k] == '1') ? 1. : 0.;
                }
                Sum += Sum1 / m1;
            }
            OWP[i] = Sum / m;
            cerr << "owp " << i << " " << OWP[i] << '\n';

        }

        vector<ld> OOWP(n);
        for (int i = 0; i < n; ++ i)
        {
            int m = 0;
            ld Sum = 0.;
            for (int j = 0; j < n; ++ j)
                if (a[i][j] != '.')
                {
                    Sum += OWP[j];
                    ++ m;
                }
            OOWP[i] = Sum / m;
        }

        vector<ld> ans(n);
        for (int i = 0; i < n; ++ i)
            ans[i] = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];

        cout << "Case #" << t + 1 << ":\n";
        for (int i = 0; i < n; ++ i)
            printf("%.6llf\n", ans[i]);
    }

    return 0;


}

