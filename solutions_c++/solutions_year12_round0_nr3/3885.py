#include<iostream>
#include<queue>
#include<stdlib.h>
#include<string.h>
#include <stdio.h>
#include <math.h>
#define N 2000010
//#define N 510
#define MAX 20000000
#define MAXX(a,b) (a<b?b:a)
#include <iostream>

int t[N];

int check(int a, int b, int x)
{
    int y = x;
    int c = 0;
    int ans = 0;
    int p = 1, p1 = 1;
    int i, j;
    int z;
    int low;
    t[x] = 1;
    ///if(x < 10) return 0;
    while(x > 0) {
        x /= 10;
        c++;
        p1 *= 10;
    }
    p1/=10;
    x = y;
    low = 0;
    ans = 1;
    //printf("c---%d\n", x);
    for(i = 1; i < c; i++) {
        low += (x % 10) * p;
        x /= 10;
        y = low * p1 + x;
        p *= 10;
        p1/= 10;
       // printf("y = %d\n", y);
        if(y >= a && y <= b && t[y] == 0) {
            t[y] = 1;
            ans++;
        }
    }
    return (ans * ( ans - 1))/2;
}

int main()
{
    int c, n;
    int i, j, k, ii;
    int a, b;
    int ans = 0;
     //init();
    //freopen("in","r",stdin);freopen("out","w",stdout);
    scanf("%d", &c);
    for(ii = 1; ii <= c; ii++) {
        scanf("%d %d", &a, &b);
        ans = 0;
        for(j = a; j <= b; j++)t[j]=0;
        for(j = a; j <= b; j++) {
            if(t[j] == 1) continue;
            ans += check(a, b, j);
        }
        printf("Case #%d: %d\n", ii, ans);
    }
    return 0;
}
