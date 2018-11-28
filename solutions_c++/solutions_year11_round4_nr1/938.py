#include<stdio.h>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<string>
#include<cmath>
#include<set>
#include<map>
#include<vector>
using namespace std;
struct node{
   int a,b,c;       
}nod[10001];
int ind;
bool operator<(node n1,node n2){
    return n1.c<n2.c;     
}
void ins(int a,int b,int c){
    nod[ind].a=a;
    nod[ind].b=b;
    nod[ind].c=c;
    ind++;     
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,x,s,r,t,n,i,j;
    scanf("%d",&T);
    for(int test=0;test<T;test++){
        scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
        ind=0;
        int a,b,c,bb=0;
        for(i=0;i<n;i++){
            scanf("%d%d%d",&a,&b,&c);
            if(a>bb){
                ins(bb,a,0);
            }
            ins(a,b,c);
            bb=b; 
        }
        if(bb!=x)ins(bb,x,0);
        sort(nod,nod+ind);
        double xt=0;
        double sum=0;
        for(i=0;i<ind;i++){
            double tr=(nod[i].b-nod[i].a)*1.0/(nod[i].c+r);
            double ts=(nod[i].b-nod[i].a)*1.0/(nod[i].c+s);
            if(xt>=t){
                sum+=ts;            
            }
            else{
               if(tr+xt>t){
                   double l=(t-xt)*(nod[i].c+r);
                   double lt=t-xt;
                   xt=t;
                   sum+=lt+(nod[i].b-nod[i].a-l)*1.0/(nod[i].c+s);
                }
                else{
                   sum+=tr;
                   xt+=tr;     
                }      
            } 
                             
        }
        printf("Case #%d: %.8lf\n",test+1,sum);
                
    }
}
