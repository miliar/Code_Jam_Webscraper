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
        int n, m;
        cin >> n >> m;
        vector< vector<char> > a(n, vector<char>(m));
        for (int i = 0; i < n; ++ i)
        {
            for (int j = 0; j < m; ++ j)
                cin >> a[i][j];
        }

        for (int i = 0; i < n; ++ i)
            for (int j = 0; j < m; ++ j)
            {
                if (a[i][j] != '#')
                    continue;
                if (i + 1 == n || j + 1 == m ||
                    a[i + 1][j] != '#' || a[i][j + 1] != '#' ||
                    a[i + 1][j + 1] != '#' )
                    T_T = true;
                else
                {
                    a[i][j] = '/';
                    a[i][j + 1] = '\\';
                    a[i + 1][j] = '\\';
                    a[i + 1][j + 1] = '/';
                }

            }

        cout << "Case #" << t + 1 << ":\n";
        if (T_T)
            cout << "Impossible\n";
        else
        {
            for (int i = 0; i < n; ++ i)
            {
                for (int j = 0; j < m; ++ j)
                    cout << a[i][j];
                cout << '\n';
            }
        }
    }

    return 0;


}

