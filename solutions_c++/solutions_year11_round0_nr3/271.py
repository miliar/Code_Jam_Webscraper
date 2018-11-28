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

int main(void)
{
    freopen("D:/C-small-attempt0.in", "r", stdin);
    freopen("D:/testc.out", "w", stdout);
    int t, n;
    int ca = 0;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &n);
        scanf("%d", &num[0]);
        int sum = num[0];
        int ans = num[0];
        int nowmin = num[0];
        for(int i = 1; i < n; ++i)
        {
            scanf("%d", &num[i]);
            if(num[i] < nowmin)
                nowmin = num[i];
            sum ^= num[i];
            ans += num[i];
        }
      //  printf("%d>>", sum);
        if(sum == 0)
        {
            printf("Case #%d: %d\n", ++ca, ans - nowmin);
        }
        else
            printf("Case #%d: NO\n", ++ca);
    }
    return 0;
}