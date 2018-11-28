#include<iostream>
#include<algorithm>
using namespace std;
struct TRAIN
{
       int b,e;
       int pos;                     //pos=-2,-1,0,1,2
}train[220],res[220];
bool cmp(TRAIN a,TRAIN b)
{
     if(a.b!=b.b)return a.b<b.b;
     else return a.e<b.e;
}
int ansa,ansb;
int main()
{
    int cases,tn;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&cases);
    for(tn=1;tn<=cases;++tn)
    {
        ansa=0,ansb=0;
        int i,j,k;
        int h,m;
        int t,na,nb;
        scanf("%d",&t);
        scanf("%d",&na);
        scanf("%d",&nb);
        for(i=0;i<na;++i)
        {
           scanf("%d:%d",&h,&m);
           train[i].b=h*60+m;
           scanf("%d:%d",&h,&m);
           train[i].e=h*60+m;
           train[i].pos=1;
        }
        for(;i<na+nb;++i)
        {
           scanf("%d:%d",&h,&m);
           train[i].b=h*60+m;
           scanf("%d:%d",&h,&m);
           train[i].e=h*60+m;
           train[i].pos=2;
        }
        sort(train,train+na+nb,cmp);
        memset(res,0,sizeof(res));
        for(i=0;i<na+nb;++i)
        {
           for(j=0;j<ansa+ansb;++j)
           {
               if(res[j].pos==train[i].pos&&train[i].b>=res[j].b)
               {
                   res[j].pos=3-train[i].pos;
                   res[j].b=train[i].e+t;
                   break;
               }
           }
           if(j==ansa+ansb)
           {
               if(train[i].pos==1)
               {
                   res[ansa+ansb].b=train[i].e+t;
                   res[ansa+ansb].pos=2;
                   ++ansa;
               }
               else if(train[i].pos==2)
               {
                   res[ansa+ansb].b=train[i].e+t;
                   res[ansa+ansb].pos=1;
                   ++ansb;
               }
           }
        }
        printf("Case #%d: %d %d\n",tn,ansa,ansb);
    }
   // while(1);
    return 0;
}