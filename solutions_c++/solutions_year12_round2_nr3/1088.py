#include<iostream>
#include<map>
#include<cmath>
using namespace std;

int num[25];

int value(int n){
    int i=0,ans=0;
    while(n){
        if(n%2)
            ans+=num[i];
        n/=2;
        i++;
    }
    return ans;
}

void print(int n){
    int i=0;
    while(n){
        if(n%2)
            printf("%d ",num[i]);
        n/=2;
        i++;
    }
    printf("\n");
}

int main(){
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int cas,c;
    int n,i;
    scanf("%d",&cas);
    for(c=1;c<=cas;c++){
        printf("Case #%d:\n",c);
        scanf("%d",&n);
        for(i=0;i<n;i++)
            scanf("%d",num+i);
        map <int,int> qq;
        bool f=1;
        for(i=1;i<1048576;i++){
            int t=value(i);
            if(qq[t]!=0){
                print(i);
                print(qq[t]);
                f=0;
                break;
            }
            else
                qq[t]=i;
        }
        if(f)
            printf("Impossible\n");
    }
    return 0;
}
