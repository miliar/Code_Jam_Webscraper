#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>

using namespace std;

int num[1000+10];
int num2[1000+10];

int main(void)
{
    freopen("D:/D-small-attempt2.in", "r", stdin);
    freopen("D:/testd.out", "w", stdout);
    int t, n;
    int ca = 0;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &n);
        for(int i = 0; i < n; ++i)
        {
            scanf("%d", &num[i]);
            num2[i] = num[i];
        }
        sort(num2, num2 + n);
        int cnt = 0;
        for(int i = 0; i < n; ++i)
        {
            if(num2[i] != num[i])
                cnt++;
        }
        printf("Case #%d: %.6lf\n", ++ca, cnt * 1.0);
    }
    return 0;
}