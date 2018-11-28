#include <stdio.h>
#include <stdlib.h>

int main(){
    int a,b,c;
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int k,n,s,p,t[105],count;
    scanf("%d",&k);
    for(int z=1;z<=k;z++){
        count=0;a=0;b=0;c=0;
        scanf("%d %d %d",&n,&s,&p);
        for(int i=0;i<n;i++) scanf("%d",&t[i]);
        for(int i=0;i<n;i++){
            if(t[i]/3>=p) count++;
            else{
                a=p;
                c=(t[i]-p)/2;
                b=t[i]-a-c;
                if(a>=0&&b>=0&&c>=0){
                    if(a-c==2&&s>0){
                        s--;
                        count++;
                    }
                    else if(a-c==1){
                        count++;
                    }
                }
            }
        }
        printf("Case #%d: %d\n",z,count);
    }
    scanf(" ");
}
