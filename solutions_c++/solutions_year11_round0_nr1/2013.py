#include<stdio.h>

int main() {
    char r[100],temp[2];
    int cnt,diff,i,j,k,num,n,p[100],t;
    int pos_b,pos_o,time_b,time_o,tmin;
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&t);
    for(cnt=1;cnt<=t;cnt++) {
        scanf("%d",&n);
        for(i=0;i<n;i++) {
            scanf("%s %d",&temp,&p[i]);
            r[i]=temp[0];
            //printf("%c %d\n",r[i],p[i]);
        }
        pos_b=1;pos_o=1;
        time_b=0;time_o=0;
        for(i=0;i<n;i++) {
            if(r[i]=='B') {
                //move B to new position
                diff=p[i]-pos_b;
                if(diff<0)diff=-diff;
                pos_b=p[i];time_b+=diff;
                //push button
                if(time_b<time_o)time_b=time_o;
                time_b++;
            }
            if(r[i]=='O') {
                //move O to new position
                diff=p[i]-pos_o;
                if(diff<0)diff=-diff;
                pos_o=p[i];time_o+=diff;
                //push button
                if(time_o<time_b)time_o=time_b;
                time_o++;
            }
            //printf("step=%d pos_b=%d pos_o=%d time_b=%d time_o=%d\n",i+1,pos_b,pos_o,time_b,time_o);
        }
        tmin=time_b;
        if(time_o>tmin)tmin=time_o;
        printf("Case #%d: %d\n",cnt,tmin);
    }
    //while(1);
    return 0;
}
