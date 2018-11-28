#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <malloc.h>
#include <algorithm>
using namespace std;
#define N 1001

int cmp(int a, int b)
{
    return a < b;
}

int main()
{
    int i, j;
    int T;
    int len;
    char str[100];
    int num[100];
    int rt[100];
    int t, ti;
    int min;
    int flag;
    int cnt;
    int tmp;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
    int cases = 1;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%s", str);
        len = strlen(str);
        for (i = 0; i < len; i++)
            num[i] = str[i] - '0';
        printf("Case #%d: ", cases++);
        if (len == 1)
        {
            printf("%d0\n", num[0]);
        }
        else
        {
            flag = 0;
            t = -1;
            for (i = len-1; i >= 0; i--)
            {
                min = num[i];
                for (j = i-1; j >= 0; j--)
                {
                    if (min > num[j] && t < j)
                    {
                        t = j;
                        ti = i;
                        flag = 1;
                        break;
                    }
                }
            }
            if (flag == 1)
            {
                cnt = 0;
                for (j = t; j < len; j++)
                {
                    if (j == ti) continue;
                    rt[cnt++] = num[j];
                }
                sort(rt, rt+cnt, cmp);
                for (j = 0; j < t; j++)
                {
                    printf("%d", num[j]);
                }
                printf("%d", num[ti]);
                for (j = 0; j < cnt; j++)
                {
                    printf("%d", rt[j]);
                }
                printf("\n");
            }
            if (flag == 0)
            {
                sort(num, num+len, cmp);
                for (i = 0; i < len; i++)
                {
                    if (num[i] != 0)
                    {
                        t = i;
                        break;
                    }
                }
                printf("%d", num[t]);
                printf("0");
                for (i = 0; i < len; i++)
                {
                    if (t == i) continue;
                    printf("%d", num[i]);
                }
                printf("\n");
            }
        }
    }
    return 0;
}
