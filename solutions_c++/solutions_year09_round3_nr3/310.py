#include <stdio.h>
bool outPrison[101];
bool out[6];
int n[6];
int t,p,q,min;
void clear(){
    int i;
    for(i=0;i<101;i++)
        outPrison[i]=false;
    for(i=0;i<6;i++)
        out[i]=false;
    min=3000000;
}
int findCost(int k){
    int i=k-1,j=k+1,c=0;
    while(i>0&&!outPrison[i--]){
        c++;
    }
    while(j<=p && !outPrison[j++]){c++;}
    return c;
}
void f(int d,int op,int cost){
    int i;
    if(d==q){
        if(cost<min)min=cost;
    }
    for(i=0;i<q;i++){
        if(!out[i]){
            out[i]=true;
            outPrison[n[i]]=true;
            f(d+1,n[i],cost+findCost(n[i]));
            out[i]=false;
            outPrison[n[i]]=false;
        }
    }
}
int main(){
    freopen("C-small-attempt1.in","rt",stdin);
    freopen("C-small-attempt1.out","wt",stdout);
    scanf("%d",&t);
    int i,j;
    for(i=0;i<t;i++){
        clear();
        scanf("%d %d",&p,&q);
        for(j=0;j<q;j++)
            scanf("%d",&n[j]);
        printf("Case #%d: ",i+1);
        if(q==1)printf("%d\n",p-1);
        else{
            for(j=0;j<q;j++){
                out[j]=true;
                outPrison[n[j]]=true;
                f(1 ,n[j],p-1);
                out[j]=false;
                outPrison[n[j]]=false;
            }
            printf("%d\n",min);
        }
    }

}

