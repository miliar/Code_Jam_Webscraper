#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <vector>
#include <list>
#include <queue>
#include <algorithm>

using namespace std;


string score[105];
int win[105], all[105];
double wp[105], owp[105], oowp[105];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    for(int ti = 0; ti < t; ++ti)
    {
        int n;
        cin >> n;
        for(int i = 0; i < n; ++i)
        {
            cin >> score[i];
            win[i] = 0;
            all[i] = 0;
            for(int j = 0; j < n; ++j)
            {
                if(score[i][j] == '1')
                {
                    ++ win[i];
                    ++ all[i];
                }
                else if(score[i][j] == '0')
                    ++ all[i];
            }
            wp[i] = win[i] * 1.0 / all[i];
        }

        for(int i = 0; i < n; ++i)
        {
            owp[i] = 0;
            int count = 0;
            for(int j = 0; j < n; ++j)
            {
                if(score[i][j] != '.')
                {
                    if(score[i][j] == '1')
                        owp[i] += (win[j] * 1.0 / (all[j] - 1));
                    else
                        owp[i] += ((win[j] - 1) * 1.0 / (all[j] - 1));
                    ++ count;
                }
            }
            owp[i] /= count;
        }

        for(int i = 0; i < n; ++i)
        {
            oowp[i] = 0;
            int count = 0;
            for(int j = 0; j < n; ++j)
            {
                if(score[i][j] != '.')
                {
                    oowp[i] += owp[j];
                    ++ count;
                }
            }
            oowp[i] /= count;
        }

        printf("Case #%d:\n", ti + 1);
        for(int i = 0; i < n; ++i)
        {
            printf("%.8lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] );
        }
    }

    return 0;
}
