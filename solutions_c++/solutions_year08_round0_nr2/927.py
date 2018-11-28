#include<stdio.h>

#define D 1440

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    
    int cases,na,nb,t,i,ii,ats[D],bts[D],t1,t2,j,aa,bb;
    char s1[22],s2[22];
    
    scanf("%d",&cases);
    for(ii=1;ii<=cases;ii++)
    {
        scanf("%d",&t);
        scanf("%d%d",&na,&nb);
        for(i=0;i<D;i++)ats[i]=bts[i]=0;
        for(i=1;i<=na;i++)
        {
            scanf("%s %s",s1,s2);
            t1=((s1[0]-'0')*10+s1[1]-'0')*60+(s1[3]-'0')*10+s1[4]-'0';
            t2=((s2[0]-'0')*10+s2[1]-'0')*60+(s2[3]-'0')*10+s2[4]-'0';
            for(j=t1;j<D;j++)ats[j]--;
            for(j=t2+t;j<D;j++)bts[j]++;
        }
        
        for(i=1;i<=nb;i++)
        {
            scanf("%s %s",s1,s2);
            t1=((s1[0]-'0')*10+s1[1]-'0')*60+(s1[3]-'0')*10+s1[4]-'0';
            t2=((s2[0]-'0')*10+s2[1]-'0')*60+(s2[3]-'0')*10+s2[4]-'0';
            for(j=t1;j<D;j++)bts[j]--;
            for(j=t2+t;j<D;j++)ats[j]++;
        }
        
        aa=bb=0;
        
        for(i=0;i<D;i++)aa<?=ats[i],bb<?=bts[i];
        
        printf("Case #%d: %d %d\n",ii,-aa,-bb);
    }
    
    return 0;
}
