#include <stdio.h>
#include <string.h>
long Abs(long x){
    if(x<=0)
        return -x;
    return x;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    long test,turn,n,i,dif;
    long mn[200],cur[200],h[200];
    char b,ch,r[10];
    scanf("%ld",&test);
    for(turn=1;turn<=test;turn++){
        printf("Case #%ld: ",turn);
        scanf("%ld",&n);
        mn['B']=mn['O']=0;
        h['B']='O',h['O']='B';
        cur['B']=cur['O']=1;
        for(i=0;i<n;i++){
            scanf("%s%ld",r,&b);
            ch=r[0];
            dif=Abs(b-cur[ch])+1;
            //printf("%c %ld dif %ld mn[%c] %ld mn[%c] %ld\n",r[0],b,dif,ch,mn[ch],h[ch],mn[h[ch]]);
            if(dif+mn[ch]<=mn[h[ch]]){
                mn[ch]=mn[h[ch]]+1;
                cur[ch]=b;
            }
            else{
                mn[ch]+=dif;
                cur[ch]=b;
            }
        }
        printf("%ld\n",mn['B']>=mn['O']?mn['B']:mn['O']);
    }
    return 0;
}
