#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

#define tiao system("pause")

int t;
int n;
int a[222][222];
bool row[222];
bool col[222];

int main(void)
{
//    freopen("A-small-attempt0.in", "r", stdin);
//    freopen("A-small-attempt0.out", "w", stdout);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
    int i,j,k,ci,cici,cicici;
    int x,y;
    
    scanf("%d", &t);
    for (cicici=1; cicici<=t; cicici++)
    {
        scanf("%d", &n);
        memset(a, -1, sizeof(a));
        for (i=1; i<=n; i++)
        {
            for (j=1, x=n-i+1; j<=i; j++, x+=2)
                scanf("%d", &a[i][x]);
        }
        
        for (i=n-1; i>=1; i--)
        {
            for (j=1, x=n-i+1; j<=i; j++, x+=2)
                scanf("%d", &a[2*n-i][x]);
        }
        
//        for (i=1; i<=2*n-1; i++)
//        {
//            for (j=1; j<=2*n-1; j++)
//                printf("%2d", a[i][j]);
//            printf("\n");
//        }

        memset(row, 0, sizeof(row));
        memset(col, 0, sizeof(col));
        
        
        int all = 2 * n - 1;
        for (i=1; i<=all; i++)
        {
            row[i] = true;
            
            for (int dx=1; ; dx++)
            {
                if (i - dx < 1 || i + dx > all) break;
                
                for (j=1; j<=all; j++)
                {
                    int cb = a[i-dx][j];
                    int wb = a[i+dx][j];
                    
                    if (cb != -1 && wb != -1 && cb != wb)
                    {
                        row[i] = false;
                        break;
                    }
                }
                
                if (!row[i]) break;
            }
        }
        
        
        for (j=1; j<=all; j++)
        {
            col[j] = true;
            
            for (int dy=1; ; dy++)
            {
                if (j-dy < 1 || j+dy > all) break;
                
                for (i=1; i<=all; i++)
                {
                    int cb = a[i][j-dy];
                    int wb = a[i][j+dy];
                    
                    if (cb != -1 && wb != -1 && cb != wb) 
                    {
                        col[j] = false;
                        break;
                    }
                }
                
                if (!col[j]) break; 
            }
        }
    
        int ans = 1 << 29;
        int tmp = n * n;
        for (i=1; i<=all; i++)
            if (row[i])
            for (j=1; j<=all; j++)
                if (col[j])
                {
                    int pu = abs(i - n) + abs(j - n) + n;
                    ans = min(ans, pu * pu - tmp);
                }
                
        printf("Case #%d: %d\n", cicici, ans);
    }    
//    tiao;
    return 0;
}
