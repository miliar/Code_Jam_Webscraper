#include<iostream>

using namespace std;

void deal(void)
{
    int n,l,h,ok;
    int a[20000];
    scanf("%d%d%d",&n,&l,&h);
    for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
    for(int ans=l;ans<=h;ans++){
        ok=1;
        for(int i=0;i<n;i++){
            if(ans%a[i]==0 || a[i]%ans==0){
            }
            else{
                ok=0;
                break;
            }
        }
        if(ok==1){
            printf("%d\n",ans);
            return ;
        }
    }
    printf("NO\n");
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
