#include<stdio.h>
int main(){
    int C,n,pa,pb,possible,Case=1;
    scanf("%d",&C);
    while(C--){
        scanf("%d%d%d",&n,&pa,&pb);
        possible=0;
        if(n>100)n=100;
        for(int i=1;i<=n&&possible==0;i++)
            if(i*pa%100==0){
                int a=i*pa/100;
                //printf("%d %d\n",a,i);
                if(pa==0&&pb==0)
                    possible=1;
                else if(pa==100&&pb==100)
                    possible=1;
                else if(pb!=0&&pb!=100)
                    possible=1;
            }
        printf("Case #%d: ",Case++);
        if(possible)
            puts("Possible");
        else puts("Broken");
    }
}
