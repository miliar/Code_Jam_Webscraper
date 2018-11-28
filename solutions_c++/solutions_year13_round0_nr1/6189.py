#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;

int main(){
    int t;
    scanf("%d", &t);
    for(int k=0;k<t;k++){
        char g[4][4];
        int a[10],b[10];
        int flag=0,aflag=0,bflag=0;
        memset(a,0,10*sizeof(int));
        memset(b,0,10*sizeof(int));
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                cin >> g[i][j];
                if(g[i][j]=='.')
                    flag=1;
                if(g[i][j]=='X' || g[i][j]=='T'){
                    a[i]++;
                    a[j+4]++;
                }
                if(g[i][j]=='O' || g[i][j]=='T'){
                    b[i]++;
                    b[j+4]++;
                }
            }
            if(g[i][i]=='X' || g[i][i]=='T')
                a[8]++;
            if(g[i][i]=='O' || g[i][i]=='T')
                b[8]++;
            if(g[i][3-i]=='X' || g[i][3-i]=='T')
                a[9]++;
            if(g[i][3-i]=='O' || g[i][3-i]=='T')
                b[9]++;
        }
        for(int i=0;i<10;i++)
        {
            if(a[i]==4)
                aflag=1;
            if(b[i]==4)
                bflag=1;
        }
        if(aflag)
            printf("Case #%d: X won\n", (k+1));
        else if(bflag)
            printf("Case #%d: O won\n", (k+1));
        else if(flag)
            printf("Case #%d: Game has not completed\n", (k+1));
        else if(!flag)
            printf("Case #%d: Draw\n", (k+1));
    }
    return 0;
}