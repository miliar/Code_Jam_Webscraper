#include<cstdio>
#include<cstring>
#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<map>
#include<set>
using namespace std;

char a[10][10];
int ans;

int main()
{
  //  freopen("A.in", "r", stdin);
  //  freopen("A.out", "w", stdout);
    bool full, bo;
    int ks, ts, i, j;
    scanf("%d", &ts);
    for (ks = 0; ks < ts; ks++){
        ans = 0;
        full = true;
        for (i = 0; i < 4; i++){
            scanf("\n");
            for (j = 0; j < 4; j++){
                scanf("%c", &a[i][j]);
                if (a[i][j] == '.') full = false;
            }
        }
        //if (ks < ts - 1) scanf("\n");
        
        for (i = 0; i < 4; i++){
            bo = true;
            for (j = 0; j < 4; j++)
                if (a[i][j] == 'O' || a[i][j] == '.') bo = false;
            if (bo) ans = 1;
            bo = true;
            for (j = 0; j < 4; j++)
                if (a[j][i] == 'O' || a[j][i] == '.') bo = false;
            if (bo) ans = 1;
            
            bo = true;
            for (j = 0; j < 4; j++)
                if (a[i][j] == 'X' || a[i][j] == '.') bo = false;
            if (bo) ans = -1;
            bo = true;
            for (j = 0; j < 4; j++)
                if (a[j][i] == 'X' || a[j][i] == '.') bo = false;
            if (bo) ans = -1;
        }
        bo = true;
        for (i = 0; i < 4; i++)
            if (a[i][i] == 'O' || a[i][i] == '.') bo = false;
        if (bo) ans = 1;
        
        bo = true;
        for (j = 0; j < 4; j++)
            if (a[j][j] == 'X' || a[j][j] == '.') bo = false;
        if (bo) ans = -1;
        
        bo = true;
        for (i = 0; i < 4; i++)
            if (a[3 - i][i] == 'O' || a[3 - i][i] == '.') bo = false;
        if (bo) ans = 1;
        
        bo = true;
        for (j = 0; j < 4; j++)
            if (a[3 - j][j] == 'X' || a[3 - j][j] == '.') bo = false;
        if (bo) ans = -1;
        
        if (ans == 1){
           printf("Case #%d: X won\n", ks + 1); 
        }
        else if (ans == -1){
                printf("Case #%d: O won\n", ks + 1); 
             }
             else if (full){
                     printf("Case #%d: Draw\n", ks + 1); 
                  }
                  else {
                       printf("Case #%d: Game has not completed\n", ks + 1); 
                  }
    }
    return 0;
}
