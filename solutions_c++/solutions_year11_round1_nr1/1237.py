#include<iostream>

using namespace std;

void deal(void)
{
    int n,pd,pg;
    scanf("%d%d%d",&n,&pd,&pg);
    if(pg==0||pg==100){
        if(pd!=pg){
            printf("Broken\n");
        }
        else{
            printf("Possible\n");
        }
        return ;
    }
    if(n>=100){
        printf("Possible\n");
        return ;
    }
    for(int i=1;i<=n;i++){
        if(i*pd%100==0){
            printf("Possible\n");
            return ;
        }
    }
    printf("Broken\n");
    return ;
}

int main(void)
{
    int num=0;
    scanf("%d",&num);
    for(int i=1;i<=num;i++){
        printf("Case #%d: ",i);
        deal();
    }
    return 0;
}
/* vim: set expandtab ts=4 sw=4 sts=4 tw=100: */
