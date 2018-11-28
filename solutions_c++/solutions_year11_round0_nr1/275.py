#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string.h>

using namespace std;

int ora[10000+10];
int blu[10000+10];
int step[20000+10];

int main(void)
{
    freopen("D:/A-large.in", "r", stdin);
    freopen("D:/test1Large.out", "w", stdout);
    int t, n;
    char temp[10];
    int pla;
    scanf("%d", &t);
    int ca = 0;
    while(t--)
    {
        scanf("%d", &n);
        int cnt1, cnt2;
        cnt1 = cnt2 = 1;
        for(int i = 0; i < n; ++i)
        {
            scanf("%s %d", temp, &pla);
            if(temp[0] == 'O')
            {
                step[i] = cnt1;
                ora[cnt1++] = pla;
            }
            if(temp[0] == 'B')
            {
                step[i] = cnt2 * -1;
                blu[cnt2++] = pla;
            }
        }
        int nowPO, nowPB;
        nowPO = nowPB = 1;
        int ans = 0;
        cnt1 = cnt2 = 1;
        for(int i = 0; i < n; ++i)
        {
            if(step[i] > 0)
            {
                int now = abs(ora[cnt1] - nowPO) + 1;
                if(abs(nowPB - blu[cnt2]) <= now)
                {
                    nowPB = blu[cnt2];
                }
                else
                {
                    if(nowPB < blu[cnt2])
                    {
                        nowPB += now;
                    }
                    else
                        nowPB -= now;
                }
                nowPO = ora[cnt1];
                cnt1++;
                ans += now;
            }
            else
            {
                int now = abs(blu[cnt2] - nowPB) + 1;
                if(abs(nowPO - ora[cnt1]) <= now)
                {
                    nowPO = ora[cnt1];
                }
                else
                {
                    if(nowPO < ora[cnt1])
                        nowPO += now;
                    else
                        nowPO -= now;
                }
                nowPB = blu[cnt2];
                cnt2++;
                ans += now;
            }
        }
        printf("Case #%d: %d\n", ++ca, ans);
    }
    return 0;
}