/**********************************************************************
Author: Xay
Created Time:  2009-9-13 1:12:04
File Name: b.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
using namespace std;

const int maxint = 0x7FFFFFFF;
const int maxn = 20 + 5;

char s[maxn];
int t, n;
int main()
{
    freopen("b.out", "w", stdout);
    int ca = 0;
    scanf("%d", &t);
    while (t--) {
        scanf("%s", s);
        int n = strlen(s);
        printf("Case #%d: ", ++ca);
        if (next_permutation(s, s + n)) {
            printf("%s\n", s);
        } else {
            sort(s, s + n);
            int k;
            for (int i = 0; i < n; ++i) {
                if (s[i] != '0') {
                    k = i;
                    break;
                }
            }
            putchar(s[k]);
            for (int i = 0; i <= k; ++i) putchar('0');
            printf("%s\n", s + k + 1);
        }
    }
    return 0;
}

