#include<stdio.h>
#include<string.h>
int n,s,p,t;
int ans;
int main(){
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int ca,i,j,sum;
    int a,b,c,cc=0;
    scanf("%d",&ca);
    while (ca--){
        cc++;
        scanf("%d%d%d",&n,&s,&p);
        ans=sum=0;
        for (i=0;i<n;i++){
            scanf("%d",&a);
            b=a/3;c=a%3;
            if (c==0){
                if (b>=p) ans++;
                else if (b==p-1&&sum<s&&b>0){
                    ans++;
                    sum++;
                }
            }else if (c==1){
                b++;
                if (b>=p) ans++;
            }else {
                b++;
                if (b>=p) ans++;
                else if (b==p-1&&sum<s){
                    ans++;
                    sum++;
                }
            }
        }
        printf("Case #%d: ",cc);
        printf("%d\n",ans);
    }
    return 0;
} 
