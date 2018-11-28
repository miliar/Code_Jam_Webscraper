#include <iostream>
#include <fstream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <time.h>
#include <stdlib.h>
using namespace std;

#define mp make_pair
#define pb push_back
#define vi vector <int>
#define rep(i,n) for(int i = 0; i < n; i++)
#define read(a) rep(i, a.size()) cin >> a[i];
#define write(a) rep(i, a.size()) cout << a[i] << ' '; cout << endl;
#define fi first
#define se second
#define ll long long
const int inf = 2000000000, mod = 1000000007;
const double eps = 0.000001;

int main()
{
    ifstream cin ("input.txt");
    ofstream cout ("output.txt");
    int t;
    cin >> t;
    for (int count = 1; count <= t; count++)
    {
        cout << "Case #" << count << ": " << endl;
        int n;
        cin >> n;
        char c[100][100];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                cin >> c[i][j];
                
        double wp[100][100];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++)
            {
                wp[i][j] = 0;
                double cur_w = 0, cur_g = 0;
                for (int k = 0; k < n; k++)
                    if (k != j && c[i][k] != '.')
                    {
                       cur_w += double(c[i][k] - '0');
                       cur_g += 1;
                    }
                if (cur_g == 0) wp[i][j] = 0;
                else wp[i][j] = cur_w / cur_g;
                //cout << wp[i][j] << ' ';
            }
            //cout << endl;
        }
        
        vector <double> owp(n, 0);
        for (int i = 0; i < n; i++)
        {
            double cur_w = 0, cur_g = 0;
            for (int j = 0; j < n; j++)
            {
                if (i == j || c[i][j] == '.') continue;
                cur_w += wp[j][i];
                cur_g += 1;
            }
            if (cur_g != 0)
               owp[i] = cur_w / cur_g;
        }
        
        vector <double> oowp(n, 0);
        for (int i = 0; i < n; i++)
        {
            double cur_w = 0, cur_g = 0;
            for (int j = 0; j < n; j++)
                if (c[i][j] != '.')
                {
                   cur_w += owp[j];
                   cur_g += 1;
                }
            if (cur_g != 0)    
               oowp[i] = cur_w / cur_g;
        }
        cout.precision(10);
        for (int i = 0; i < n; i++)
            cout << fixed << 0.25 * wp[i][i] + 0.5 * owp[i] + 0.25 * oowp[i] << endl;
            //cout << fixed << wp[i][i] << ' ' << owp[i] << ' ' << oowp[i] << endl;
        
    }
    return 0;
}








