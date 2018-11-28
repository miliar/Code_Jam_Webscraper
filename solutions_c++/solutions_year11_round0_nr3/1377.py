#include<iostream>

using namespace std;

void deal(void)
{
    int a,n,sum=0,min=1000001,add=0;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%d",&a);
        sum+=a;
        add^=a;
        if(min>a){
            min=a;
        }
    }
    if(add==0){
        printf("%d\n",sum-min);
    }
    else{
        printf("NO\n");
    }
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
