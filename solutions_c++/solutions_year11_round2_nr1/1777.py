/*
	author:  hnu0314
	type :  C/C++
*/

#include <iostream>
#include <stdio.h>
#include <cstring>
#include <algorithm>
#define MAXN 0

using namespace std;

typedef long long LL;

char map[110][110];
double wp[110], owp[110], oowp[110];
double t[110][2];
int main()
{
    int test, n, cas(1);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&test);
    while(test--)
    {
        scanf("%d",&n);
        for(int i = 0; i < n; ++i)
            scanf("%s",&map[i]);

        for(int i = 0; i < n; ++i)
        {
            t[i][0] = 0.0;  t[i][1] = 0.0;
            for(int j = 0; j < n; ++j)
            {
                if(map[i][j] == '.')    continue;
                if(map[i][j] == '1')    t[i][0] += 1.0;
                else t[i][1] += 1.0;
            }
            if(t[i][0] + t[i][1] == 0.0)  wp[i] = 0;
            else wp[i] = t[i][0] / (t[i][0] + t[i][1]);
           // printf("%.6lf\n",wp[i]);
        }
        for(int i = 0; i < n; ++i)
        {
            double t1(0.0), t2(0.0);
            for(int j = 0; j < n; ++j)
            {
                if(map[i][j] == '.')    continue;
                if(map[j][i] == '1')
                {
                    t1 += (t[j][0] - 1) / (t[j][0]+t[j][1]-1);
                }
                else t1 += t[j][0] / (t[j][0] + t[j][1]-1);
                t2 += 1.0;
            }
            if(t2 == 0)   owp[i] = 0.0;
            else  owp[i] = t1 / t2;
        }
        for(int i = 0; i < n; ++i)
        {
            double t1(0.0), t2(0.0);
            for(int j = 0; j < n; ++j)
            {
                if(map[i][j] == '.')    continue;
                t1 += owp[j];
                t2 += 1.0;
            }
            if(t2 == 0.0)   oowp[i] = 0.0;
            else oowp[i] = t1 / t2;
        }
        printf("Case #%d:\n",cas++);
        for(int i = 0; i < n; ++i)
            printf("%.8lf\n",0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
    }

	return 0;
}
