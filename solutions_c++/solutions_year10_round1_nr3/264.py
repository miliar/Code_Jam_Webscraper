#include<stdio.h>
#include<stdlib.h>


long long stat[2000000];

int main(){
    freopen("C-large.in","r",stdin);
    freopen("outc2.out","w",stdout);
    stat[2]=1;
    stat[3]=1;
    stat[4]=2;
    stat[5]=3;
    for(int i=6;i<=1000000;i++){
        int z=stat[i-1]+1;
        if(stat[z]<i-z)stat[i]=z;
        else stat[i]=z-1;
    }
    int t;
    scanf("%d",&t);
    for(int time=1;time<=t;time++){
        int a1,a2,b1,b2;
        scanf("%d %d %d %d",&a1,&a2,&b1,&b2);
        long long ans=0;
        for(int i=a1;i<=a2;i++){
            if(b1<=stat[i]){
                    if(b2<=stat[i]){
                        ans+= (b2-b1+1);
                    }
                    else{
                        ans+= (stat[i]-b1+1);
                    }
                }
        }

        for(int i=b1;i<=b2;i++){
            if(a1<=stat[i]){
                if(a2<=stat[i]){
                    ans+=(a2-a1+1);
                }
                else{
                    ans+=(stat[i]-a1+1);
                }
            }
        }
        printf("Case #%d: %lld\n",time,ans);
    }
}
