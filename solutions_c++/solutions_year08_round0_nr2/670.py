#include<iostream>
using namespace std;
struct data
{
       int s,t,sta;
}tim[105];
bool cmp(data a,data b)
{
     if (a.s<b.s)return true;
     else return false;
} 
int main()
{
    int casen,na,nb,hh,mm;
    int staa[1505],stab[1505]; 
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout); 
    scanf("%d",&casen);
    for (int casei=1;casei<=casen;casei++)
    {
        int t; 
        scanf("%d",&t); 
        scanf("%d %d",&na,&nb);
        for (int i=1;i<=na;i++)
        {
            scanf("%d:%d",&hh,&mm);
            tim[i].s=hh*60+mm;
            scanf("%d:%d",&hh,&mm);
            tim[i].t=hh*60+mm;
            tim[i].sta=1; 
        }
        for (int i=1;i<=nb;i++)
        {
            scanf("%d:%d",&hh,&mm);
            tim[i+na].s=hh*60+mm;
            scanf("%d:%d",&hh,&mm);
            tim[i+na].t=hh*60+mm;
            tim[i+na].sta=2;
        }
        sort(tim+1,tim+na+nb+1,cmp);
        int ra=0,rb=0; 
            memset(staa,0,sizeof(staa));
            memset(stab,0,sizeof(stab));
        for (int i=1;i<=na+nb;i++)
        {
            if (tim[i].sta==1)
            {
                              if (staa[tim[i].s]>0)
                              {
                                                   for (int j=tim[i].s;j<=1500;j++)
                                                     staa[j]--;
                              }else ra++;
                              for (int j=tim[i].t+t;j<=1500;j++)
                                stab[j]++;
            }
            else
            {
                if (stab[tim[i].s]>0)
                {
                                     for (int j=tim[i].s;j<=1500;j++)
                                       stab[j]--;
                }else rb++;
                for (int j=tim[i].t+t;j<=1500;j++)
                  staa[j]++;
            }
        }
        printf("Case #%d: %d %d\n",casei,ra,rb); 
    }
    return 0;
}
             
        
