#include <stdio.h>
inline int abs(int x){return x>0?x:-x;}
int area(int a,int b,int c,int d){
    return abs(c*a+d*b-a*b);
}
int main(){
    int t,lp,n,m,s,a,b,c,d;
    scanf("%d",&t);
    for(lp=1;lp<=t;){
casebegin:  ;
        scanf("%d %d %d",&n,&m,&s);
        for(a=0;a<=m;a++){
            for(b=0;b<=n;b++){
                for(c=0;c<=n;c++){
                    for(d=0;d<=m;d++){
                       if(area(a,b,c,d)==s){
                           printf("Case #%d: %d %d %d %d %d %d\n",lp++,0,a,b,0,c,d);
                           if(lp<=t) goto casebegin;
                           else return 0;
                       }
                    }
                }
            }
        }
        printf("Case #%d: IMPOSSIBLE\n",lp++);
    }
    return 0;
}
     
                       
