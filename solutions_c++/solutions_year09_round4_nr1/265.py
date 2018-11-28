/**********************************************************************
Author: Xay
Created Time:  2009-9-27 0:06:59
File Name: contest\gcj09r2\a.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
using namespace std;

const int maxint = 0x7FFFFFFF;
const int maxn = 40 + 10;

int t, n;
char s[maxn * 2];
int a[maxn];

int main()
{
    freopen("a.out", "w", stdout);
    scanf("%d", &t);
    int ca = 0;
    while (t--) {
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%s", s);
            a[i] = 0;
            for (int j = 0; j < n; ++j) {
                if (s[j] == '1') a[i] = j;
            }
        }
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i; j < n; ++j) {
                if (a[j] <= i) {
                    ans += j - i;
                    for (int k = j; k > i; --k) {
                        a[k] = a[k - 1];
                    }
                    break;
                }
            }
        }
        printf("Case #%d: %d\n", ++ca, ans);
    }
    return 0;
}

