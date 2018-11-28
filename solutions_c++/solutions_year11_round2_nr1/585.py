#include <vector>
#include <cstdio>
#include <set>
#include <map>
#include <ctime>
#include <string>
#include <sstream>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <cstring>
#include <cctype>
#include <algorithm>

#define inputfilename "a.in"
#define outputfilename "a.out"

using namespace std;

int mat[200][200];

double v[3][200];
int wp[2][200];

int main ()
{
    //freopen(inputfilename , "r" , stdin);
	//freopen(outputfilename , "w" , stdout);
    
    int number, times;
    cin >> number;
    for (times = 0; times < number; times++)
    {
        int n;
        int i, j, k;
        cin >> n;
        for (i = 0; i < n ; i++)
        {
            string s;
            cin >> s;
            for (j = 0; j < n; j++)
            {
                char c = s[j];
                if (c == '.')
                    mat[i][j] = -1;
                else
                    mat[i][j] = c - '0';
            }
        }
        memset(v, 0 , sizeof(v));
        for (i = 0; i < n; i++)
        {
            int cnt = 0;
            int win = 0;
            for (j = 0; j < n; j++)
            {
                if (mat[i][j] != -1)
                    cnt++;
                if (mat[i][j] == 1)
                    win++;
            }
            v[0][i] = (double)win/cnt;
            wp[0][i] = win;
            wp[1][i] = cnt;
        }
        for (k = 1; k <= 2; k++)
        {
            for (i = 0; i < n; i++)
            {
                double val = 0;
                int cnt = 0;
                for (j = 0; j < n; j++)
                {
                    if (mat[i][j] != -1)
                    {
                        cnt++;
                        if (k == 2)
                            val += v[k-1][j];
                        else
                        {
                            int win = wp[0][j];
                            int tcnt = wp[1][j] - 1;
                            if (mat[i][j] == 0)
                                win--;
                            val += (double)win/tcnt;
                        }
                    }
                }
                v[k][i] = val / cnt;
            }
        }
        cout <<"Case #"<< times+1<<":"<< endl;
        for (i = 0; i < n; i++)
        {
            double res;
            res = 0.25 * v[0][i] + 0.50 * v[1][i] + 0.25 * v[2][i];
            cout << res << endl;
        }
    }


	return 0;
}

 
