#include<stdio.h>
#include<stdlib.h>
int main(){
    long t;
    long n,s,p,ans;
    scanf("%ld",&t);
    for(long i=0;i<t;i++){
        ans=0;
        scanf("%ld %ld %ld",&n,&s,&p);
        for(long j=0;j<n;j++){
            long score;
            scanf("%ld",&score);
            long temp=score/3;
            if(score%3==2){
                if(temp>=p)ans++;
                else if(temp+1>=p)ans++;
                else if(temp+2>=p&&s>0){
                    ans++;
                    s--;
                }
            }
            else if(score%3==1){
                if(temp>=p)ans++;
                else if(temp+1>=p)ans++;
            }
            else{
                if(temp>=p)ans++;
                else if(temp+1>=p&&s>0&&temp>0){
                    ans++;
                    s--;
                }
            }
        }
        printf("Case #%ld: %ld\n",i+1,ans);

    }
    return 0;
}
