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
    //freopen("B-large.in", "r", stdin);
    freopen("a-out.out", "w", stdout);
    int _, tt = 1;
    scanf("%d", &_);

    while(_--){
        int a, b, ans = 0;
        scanf("%d%d", &a, &b);
        if(a / 10 == 0) ans = 0;
        else if(a / 100 == 0){
            for(int i = a; i <= b; i++){
                int j = (i % 10) * 10 + (i / 10);
                if(j >= a && j <= b && j > i) ans++;
            }
        }
        else{
            for(int i = a; i <= b; i++){
                int j = (i % 100) * 10 + (i / 100);
                int t = (j % 100) * 10 + (j / 100);
                if(j >= a && j <= b && j > i) ans ++;
                if(t >= a && t <= b && t > i) ans ++;
            }
        }
        printf("Case #%d: %d\n", tt++, ans);
    }

    return 0;
}
