#include <iostream>
#include <cstdio>
#include <memory.h>
using namespace std;

void solve(){
     int r, c;
     char buf[100][100];
     memset(buf, 0, sizeof buf);
     scanf("%d%d\n", &r, &c);
     for (int i=0; i<r; ++i)
         gets(buf[i]);
     for (int i=0; i<r; ++i)
         for (int j=0; j<c; ++j){
             if (buf[i][j]=='#'){
                if (buf[i+1][j+1]!='#' || buf[i][j+1]!='#' || buf[i+1][j]!='#'){
                   printf("Impossible\n");
                   return;
                }
                buf[i][j]=buf[i+1][j+1]='/';
                buf[i][j+1]=buf[i+1][j]='\\';
             }
         }
     for (int i=0; i<r; ++i)
         puts(buf[i]);
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t;
    scanf("%d\n", &t);
    for (int i=0; i<t; ++i){
        printf("Case #%d:\n", i+1);
        solve();
    }
}
