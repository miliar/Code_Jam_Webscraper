#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>

using namespace std;

int main()
{
    int a, b;
    int n, m;
    int t;
    
    //freopen("inputc.in", "r", stdin);
    //freopen("outputc.out", "w", stdout);
    
    scanf("%d", &t);
    for(int i = 1; i <= t; i++) {
        int ans = 0;
        scanf("%d%d", &a, &b);
        int digit = 0;
        int tmp = a;
        while(tmp) {
            tmp /= 10;
            digit++;
        }
        for(n = a; n < b; n++) {
            tmp = n;
            for(int j = 1; j < digit; j++) {
                m = tmp / 10;
                int power = 1;
                for(int k = 1; k < digit; k++)
                    power *= 10;
                m += (tmp % 10) * power;
                if(m > n && m <= b)
                    ans++;
                tmp = m;
            }
        }
        
        printf("Case #%d: %d\n", i, ans);
    }
    
    return 0;
}

