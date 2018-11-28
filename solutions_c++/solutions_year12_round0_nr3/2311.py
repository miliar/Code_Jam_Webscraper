#include <iostream>
#include <stdio.h>
#include <set>
#define Y second

using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    int f[7];
    f[0] = 1;
    for (int i = 1; i <= 6; i++) f[i] = f[i - 1] * 10;
    for (int cases = 1; cases <= t; cases++) {
        int a, b;
        scanf("%d%d", &a, &b);
        int ans = 0;
        for (int i = a; i <= b; i++) {
            int temp = a, len = 0;
            while (temp > 0) temp /= 10, len++;
            set<int> S;
            for (int j = 1; j < len; j++) {
                temp = i % f[j] * f[len - j] + i / f[j];
                if (temp > i && temp >= a && temp <= b) {
                    if (!S.insert(temp).Y) continue;
                    ans++;
                }
            }
        }
        printf("Case #%d: %d\n", cases, ans);
    }
    return 0;
}
