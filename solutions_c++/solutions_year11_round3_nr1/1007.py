#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
using namespace std;
int T,k,i,j,r,c;
char tile[60][60];
int flag;

int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w+",stdout);
    scanf("%d",&T);getchar();
    for(k=1;k<=T;k++) {
        scanf("%d%d",&r,&c);getchar();
        for(i=0;i<r;i++) {
            for(j=0;j<c;j++) {
                scanf("%c",&tile[i][j]);
            }
            getchar();
        }
        flag=1;
        for(i=0;i<r;i++) {
            for(j=0;j<c;j++) {
                if (tile[i][j]=='#') {
                    if (tile[i+1][j]=='#' && tile[i][j+1]=='#' &&tile[i+1][j+1]=='#') {
                        tile[i][j]='/';
                        tile[i+1][j]='\\';
                        tile[i][j+1]='\\';
                        tile[i+1][j+1]='/';
                    }
                    else {
                        flag=-1;
                        break;
                    }
                }
                if (flag==-1) break;
            }
        }
        printf("Case #%d:\n",k);
        if (flag==-1) printf("Impossible\n");
        else {
            for(i=0;i<r;i++) {
                for(j=0;j<c;j++)
                    printf("%c",tile[i][j]);
                printf("\n");
            }
        }

    }
    return 0;
}
