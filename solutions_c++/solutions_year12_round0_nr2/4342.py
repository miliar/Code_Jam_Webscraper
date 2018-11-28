#include<stdio.h>

int main(){
    int t;
    scanf("%d",&t);
    int i;
    for(i=0;i<t;i++){
        int n,s,p;
        scanf("%d %d %d",&n,&s,&p);
        int num[n];
        int j;
        int max=0;
        for(j=0;j<n;j++){
            scanf("%d",&num[j]);
            int m=num[j]%3;
            int x=num[j]/3;
            if((m==0&&x>=p)||(m!=0&&x+1>=p)){
                max++;
            }else if(s>0){
                if(num[j]-2<0)continue;
                s--;
                x=(num[j]-2)/3;
                if(x+2>=p)max++;
                else s++;
            }
        }
        printf("Case #%d: %d\n",i+1,max);
    }
}


