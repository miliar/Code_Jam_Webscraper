#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <math.h>
#include <set>
#include <stdio.h>
#include <map>
#include <vector>

using namespace std;

char temp[100+10][100+10];
int mat[100+10][100+10];
double wp[100+10], owp[100+10], oowp[100+10];
int en[100+10][100+10];

int main(void)
{
    freopen("D:/A-small-attempt0.in", "r", stdin);
    freopen("D:/Asmall.out", "w", stdout);
    int t, n;
    scanf("%d", &t);
    int ca = 0;
    while(t--)
    {
        scanf("%d", &n);
        for(int i = 0; i < n; ++i)
        {
            scanf("%s", temp[i]);
        }
        for(int i = 0; i < n; ++i)
        {
            for(int j = 0; j < n; ++j)
            {
                if(temp[i][j] == '.')
                    mat[i][j] = 0;
                else if(temp[i][j] == '1')
                {
                    mat[i][j] = 1;
                }
                else
                    mat[i][j] = -1;
            }
        }
//        memset(en, 0, sizeof(en));
        memset(owp, 0, sizeof(owp));
        memset(oowp, 0, sizeof(oowp));
        memset(wp, 0, sizeof(wp));
        for(int i = 0; i < n; ++i)
        {
            int now = 0;
            int cnt = 0;
            for(int j = 0; j < n; ++j)
            {
                if(mat[i][j] != 0)
                {
                    cnt++;
                    if(mat[i][j] == 1)
                        now++;
                //    en[i][j] = 1;
                }
            }
            wp[i] = (now * 1.0) / (cnt * 1.0);
        }
        for(int i = 0; i < n; ++i)
        {
            int allcnt = 0;
            for(int j = 0; j < n; ++j)
            {
                if(mat[i][j] != 0)
                {
                    int now = 0;
                    int cnt = 0;
                    for(int k = 0; k < n; ++k)
                    {
                        if(k == i)
                            continue;
                        if(mat[j][k] != 0)
                        {
                            cnt++;
                            if(mat[j][k] == 1)
                                now++;
                        }
                    }
                    owp[i] += (now * 1.0) / (cnt * 1.0);
                    allcnt++;
                }
            }
            owp[i] /= allcnt;
        }
        for(int i = 0; i < n; ++i)
        {
            int allcnt = 0;
            for(int j = 0; j < n; ++j)
            {
                if(mat[i][j] != 0)
                {
                    oowp[i] += owp[j];
                    allcnt++;
                }
            }
            oowp[i] /= (allcnt * 1.0);
        }
        printf("Case #%d:\n", ++ca);
        for(int i = 0; i < n; ++i)
        {
            printf("%.6lf\n", wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25);
        }
    }
}