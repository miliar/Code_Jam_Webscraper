#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

#define tiao system("pause")

bool a[111][111];
bool b[111][111];
int cnt = 0;
int t;
int r;

int main(void)
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    
    int i,j,k,ci,cici,cicici;
    scanf("%d", &t);
    for (cicici=1;  cicici<=t; cicici++)
    {
        memset(a, 0, sizeof(a));
        
        scanf("%d", &r);
        for (cici=1; cici<=r; cici++)
        {
            int x, xx;
            int y, yy;
            
            scanf("%d%d%d%d", &x, &y, &xx, &yy);
            if (x > xx) swap(x, xx);
            if (y > yy) swap(y, yy);
            
            for (i=x; i<=xx; i++)
                for (j=y; j<=yy; j++)
                    a[i][j] = true;
        }        
        
        int time = 0;
        while(1)
        {
            bool ok = true;
            for (i=1; i<=100; i++)
                for (j=1; j<=100; j++)
                    if (a[i][j])
                    {
                        ok = false;
                    }
            if (ok) break;
                    
            memcpy(b, a, sizeof(b));
            for (i=1; i<=100; i++)
                for (j=1; j<=100; j++)
                {
                    if (a[i-1][j] && a[i][j-1]) b[i][j] = true;
                    if (!a[i-1][j] && !a[i][j-1]) b[i][j] = false;
                }
                   
            time++;  
            memcpy(a, b, sizeof(b));
        }
        
        printf("Case #%d: %d\n", cicici, time);
    }    
        
//    tiao;
    return 0;
}
