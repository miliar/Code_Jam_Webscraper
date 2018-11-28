#include<iostream>

using namespace std;

void deal(void)
{
    int r,c;
    char a[101][101];
    scanf("%d%d",&r,&c);
    for(int i=0;i<r;i++)
        scanf("%s",a[i]);
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            if(a[i][j]=='#'){
                if(i+1<r && j+1<c && a[i][j+1]=='#' && a[i+1][j]=='#' && a[i+1][j+1]=='#'){
                    a[i][j]=a[i+1][j+1]='/';
                    a[i][j+1]=a[i+1][j]='\\';
                }
                else{
                    printf("Impossible\n");
                    return ;
                }
            }
        }
    }
    for(int i=0;i<r;i++)
        printf("%s\n",a[i]);
    return ;
}

int main(void)
{
    int num=0;
    scanf("%d",&num);
    for(int i=1;i<=num;i++){
        printf("Case #%d:\n",i);
        deal();
    }
    return 0;
}
/* vim: set expandtab ts=4 sw=4 sts=4 tw=100: */
