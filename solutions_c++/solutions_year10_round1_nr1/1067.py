#include <iostream>
#include <string>
#include <stdio.h>
#include <string.h>
using namespace std;

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    const int maxn = 60;
    char temp[maxn], map[maxn][maxn], map1[maxn][maxn];
    int tot[maxn];
    int t, n, k;
    bool red, blue;
    cin >>t;
    for (int tt = 0; tt < t; ++ tt)
    {
        red = blue = false;
        cin >>n >>k;
        for (int i = 0; i < n; ++ i)
            cin >> map[i];
        for (int i = 0; i < n; ++ i)
            for (int j = n - 1; j >= 0; -- j)
                if (map[i][j] != '.')
                {
                    int y = j;
                    while (y < n - 1 && map[i][y + 1] == '.') y ++;
                    if (y != j)
                    {
                        map[i][y] =  map[i][j];
                        map[i][j] = '.';
                    }
                }
        /*for (int i = 0; i < n; ++ i)
        {
            for (int j = 0; j < n; ++ j)
                cout <<map[i][j];
            cout <<endl;
        }
        cin.get();*/
        //case 1
        for (int i = 0; i < n; ++ i)
        {
            tot[0] = 1;
            for (int j = 1; j < n; ++ j)
                if (map[i][j] == map[i][j - 1])
                {
                    tot[j] = tot[j - 1] + 1;
                    if (tot[j] >= k)
                    {
                        if (map[i][j] == 'R') red = true;
                        else if (map[i][j] == 'B') blue = true;
                    }
                }
                else tot[j] = 1;
            //for (int j = 0; j < n; ++ j) cout <<tot[j];cout <<endl;
        }//cout <<red <<blue <<endl;
        //case 2
        for (int i = 0; i < n; ++ i)
        {
            tot[0] = 1;
            for (int j = 1; j < n; ++ j)
                if (map[j][i] == map[j - 1][i])
                {
                    tot[j] = tot[j - 1] + 1;
                    if (tot[j] >= k)
                    {
                        if (map[j][i] == 'R') red = true;
                        else if (map[j][i] == 'B') blue = true;
                    }
                }
                else tot[j] = 1;
            //for (int j = 0; j < n; ++ j) cout <<tot[j];cout <<endl;
        }//cout <<red <<blue <<endl;
        //case 3
        for (int i = 0; i < n - k + 1; ++ i)
        {
            tot[0] = 1;
            for (int j = 1; j < n - i; ++ j)
                if (map[i + j][j] == map[i + j - 1][j - 1])
                {
                    tot[j] = tot[j - 1] + 1;
                    if (tot[j] >= k)
                    {
                        if (map[i + j][j] == 'R') red = true;
                        else if (map[i + j][j] == 'B') blue = true;
                    }
                }
                else tot[j] = 1;
            //for (int j = 0; j < n - i; ++ j) cout <<tot[j];cout <<endl;
        }
        for (int i = 0; i < n - k + 1; ++ i)
        {
            tot[0] = 1;
            for (int j = 1; j < n - i; ++ j)
                if (map[j][i + j] == map[j - 1][i + j - 1])
                {
                    tot[j] = tot[j - 1] + 1;
                    if (tot[j] >= k)
                    {
                        if (map[j][i + j] == 'R') red = true;
                        else if (map[j][i + j] == 'B') blue = true;
                    }
                }
                else tot[j] = 1;
            //for (int j = 0; j < n - i; ++ j) cout <<tot[j];cout <<endl;
        }//cout <<red <<blue <<endl;
        //case 4
        for (int i = k - 1 ; i < n; ++ i)
        {
            tot[0] = 1;
            for (int j = 1; j < i + 1; ++ j)
                if (map[j][i - j] == map[j - 1][i - j + 1])
                {
                    tot[j] = tot[j - 1] + 1;
                    if (tot[j] >= k)
                    {
                        if (map[j][i - j] == 'R') red = true;
                        else if (map[j][i - j] == 'B') blue = true;
                    }
                }
                else tot[j] = 1;
            //for (int j = 0; j < i + 1; ++ j) cout <<tot[j];cout <<endl;
        }
        for (int i = 0; i < n - k + 1; ++ i)
        {
            tot[0] = 1;
            for (int j = 1; j < n - i; ++ j)
                if (map[i + j][n - 1 - j] == map[i + j - 1][n - 1 - j + 1])
                {
                    tot[j] = tot[j - 1] + 1;
                    if (tot[j] >= k)
                    {
                        if (map[i + j][n - 1 - j] == 'R') red = true;
                        else if (map[i + j][n - 1 - j] == 'B') blue = true;
                    }
                }
                else tot[j] = 1;
             //for (int j = 0; j < n - i; ++ j) cout <<tot[j];cout <<endl;
       }//cout <<red <<blue <<endl;
        cout <<"Case #" << tt + 1 << ": ";
        if (red && blue) cout <<"Both\n";
        else if (red) cout <<"Red\n";
        else if (blue) cout <<"Blue\n";
        else cout <<"Neither\n";
    }
    return 0;
}
