#include<stdio.h>
#include<iostream>
using namespace std;
int main(){
    int C,n,l,h,Case=1,ans;
    long long a[10001];
    scanf("%d",&C);
    while(C--){
        scanf("%d%d%d",&n,&l,&h);
        for(int i=0;i<n;i++)
            cin>>a[i];
        int flag;
        for(int i=l;i<=h;i++){
            flag=1;
            for(int j=0;j<n;j++)
                if(i%a[j]!=0&&a[j]%i!=0){
                    flag=0;
                    break;
                }
            if(flag){
                ans=i;
                break;
            }
        }
        printf("Case #%d: ",Case++);
        if(flag)
            cout<<ans<<endl;
        else puts("NO");
    }
}
