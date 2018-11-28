#include<stdio.h>
#include<iostream>
#include<map>
#include<string.h>
#include<string>
#include<algorithm>
using namespace std;

int a[110];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("a-out.out", "w", stdout);
    int _, tt = 1;
    scanf("%d", &_);

    while(_--){
        int ans = 0, l = 0;
        int n, m, p;
        scanf("%d%d%d", &n, &m, &p);
        for(int i = 0; i < n; i++) scanf("%d", &a[i]);
        for(int i = 0; i < n; i++){
            if(a[i] >= 3 * p - 2) ans++;
            else if(a[i] >= 3 * p - 4 && (a[i] != 0 || p == 0)) l++;
        }
        ans += min(l, m);
        printf("Case #%d: %d\n", tt++, ans);
    }

    return 0;
}
