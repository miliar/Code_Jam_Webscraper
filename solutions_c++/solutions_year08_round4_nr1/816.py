#include <stdio.h>
int m,op[10001],val[10001],ch[10001];
int change(int,int);
void getval();
int min(int x,int y){return x<y?x:y;}
int main(){
    int t,lp,v,chg,i;
    scanf("%d",&t);
    for(lp=1;lp<=t;lp++){
        scanf("%d %d",&m,&v);
        for(i=1;i*2<m;i++) scanf("%d %d",op+i,ch+i);
        for(;i<=m;i++) scanf("%d",val+i);
        getval();
        chg=change(1,v);
        if(chg==m) printf("Case #%d: IMPOSSIBLE\n",lp);
        else printf("Case #%d: %d\n",lp,chg);
    }
    return 0;
}
void getval(){
     int i;
     for(i=(m-1)/2;i>0;i--) val[i]=op[i]?val[i*2]&val[i*2+1]:val[i*2]|val[i*2+1];
}
int change(int i,int v){
    if(val[i]==v) return 0;
    else if(i*2>m) return m;
    else{
         int chg,;
         if(op[i]){
             if(v){
                   chg=change(i*2,1)+change(i*2+1,1);
                   if(ch[i]) chg=min(chg,1+min(change(i*2,1),change(i*2+1,1)));
                   chg=min(m,chg);
             }
             else chg=min(m,min(change(i*2,0),change(i*2+1,0)));
         }
         else{
              if(v) chg=min(m,min(change(i*2,1),change(i*2+1,1)));
              else{
                   chg=change(i*2,0)+change(i*2+1,0);
                   if(ch[i]) chg=min(chg,1+min(change(i*2,0),change(i*2+1,0)));
                   chg=min(m,chg);
              }
         }
         return chg;
    }
}
                    
