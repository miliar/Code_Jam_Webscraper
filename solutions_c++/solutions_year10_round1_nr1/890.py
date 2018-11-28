#include <iostream>
#include <iomanip>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;

char b[50][50];
void fun(int n, int k)
{
    for(int h = 0; h < n; h++)
    for(int j = n - 2; j >= 0; j--)
    {
        for(int i = 0; i < n; i++)
        {
            if(b[i][j + 1] == '.') swap(b[i][j + 1], b[i][j]);
        }
    }

    bool red = false;
    bool blue = false;
    for(int i = 0; i < n; i++)
    {
        char now = '.';
        int nc = 0;
        for(int j = 0; j < n; j++)
        {
            if(b[i][j] == now)
            {
                nc++;
                if(nc >= k)
                {
                    if(now == 'R') red = true;
                    else if(now == 'B') blue = true;
                }
            }
            else
            {
                now = b[i][j];
                nc = 0;
                j--;
            }
        }
    }
    for(int i = 0; i < n; i++)
    {
        char now = '.';
        int nc = 0;
        for(int j = 0; j < n; j++)
        {
            if(b[j][i] == now)
            {
                nc++;
                if(nc >= k)
                {
                    if(now == 'R') red = true;
                    else if(now == 'B') blue = true;
                }
            }
            else
            {
                now = b[j][i];
                nc = 0;
                j--;
            }
        }
    }
    for(int i = 0; i < n; i++)
    {
        char now = '.';
        int nc = 0;
        int ii = i;
        for(int j = 0; j <= i; j++, ii--)
        {
            if(b[ii][j] == now)
            {
                nc++;
                if(nc >= k)
                {
                    if(now == 'R') red = true;
                    else if(now == 'B') blue = true;
                }
            }
            else
            {
                now = b[ii][j];
                nc = 0;
                j--;
                ii++;
            }
        }
        now = '.';
        nc = 0;
        ii = n - 1;
        for(int j = 0; j <= i; j++, ii--)
        {
            if(b[ii][j + n - i - 1] == now)
            {
                nc++;
                if(nc >= k)
                {
                    if(now == 'R') red = true;
                    else if(now == 'B') blue = true;
                }
            }
            else
            {
                now = b[ii][j + n - i - 1];
                nc = 0;
                j--;
                ii++;
            }
        }
    }
    for(int i = 0; i < n; i++)
    {
        char now = '.';
        int nc = 0;
        int ii = n - i - 1;
        for(int j = 0; j <= i; j++, ii++)
        {
            if(b[ii][j] == now)
            {
                nc++;
                if(nc >= k)
                {
                    if(now == 'R') red = true;
                    else if(now == 'B') blue = true;
                }
            }
            else
            {
                now = b[ii][j];
                nc = 0;
                j--;
                ii--;
            }
        }
        now = '.';
        nc = 0;
        ii = 0;
        for(int j = 0; j <= i; j++, ii++)
        {
            if(b[ii][j + n - i - 1] == now)
            {
                nc++;
                if(nc >= k)
                {
                    if(now == 'R') red = true;
                    else if(now == 'B') blue = true;
                }
            }
            else
            {
                now = b[ii][j + n - i - 1];
                nc = 0;
                j--;
                ii--;
            }
        }
    }
    if(red && blue) cout << "Both";
    else if(red) cout << "Red";
    else if(blue) cout << "Blue";
    else cout << "Neither";
}
int main(int argc, char *argv[])
{
    int T, N, K;
    cin >> T;
    string str;
    for(int ci = 1; ci <= T; ci++)
    {
        cin >> N >> K;
        getline(cin, str);
        for(int i = 0; i < N; i++)
        {
            getline(cin, str);
            for(int j = 0; j < N; j++)
            {
                b[i][j] = str.at(j);
            }
        }
        cout << "Case #" << ci << ": ";
        fun(N, K);
        cout << endl;
    }
    return 0;
}
