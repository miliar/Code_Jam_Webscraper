#include<stdio.h>
#include<stdlib.h>
struct match{
    int price;
    int s,e;
};

int main(){
    int t;
    freopen("B-small-attempt3.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&t);
    for(int time=1;time<=t;time++){
        int p;
        scanf("%d",&p);
        int team=1<<p;
        int m[1200];
        for(int i=0;i<team;i++){
            scanf("%d",&m[i]);
        }
        int tick[12][600];
        int now=team/2;
        //printf("now =%d ",now);
        int ans=0;
        for(int i=0;i<p;i++,now/=2){
            int s=0;
            int e=1<<(i+1);
            for(int j=0;j<now;j++){
                scanf("%d",&tick[i][j]);
                //printf("s= %d e = %d ",s,e);
                int miss=1;
                for(int q=s;q<e;q++){
                    if(m[q]==0)miss=0;
                }
                if(miss==0)ans++;
                else{
                    for(int q=s;q<e;q++){
                        m[q]--;
                    }
                }

                s+=1<<(i+1);
                e+=1<<(i+1);
            }
        }
        printf("Case #%d: %d\n",time,ans);


    }
}
