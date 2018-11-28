#include<stdio.h>
int checkp(int sc,int p)
{
    while(sc++%3!=0);
    return --sc/3>=p?1:0;
}
int checks(int sc,int p)
{
    if(sc<2||sc>28)return 0;
    if(sc-1%3==0)return 0;
    while(sc++%3!=0);
    return --sc/3+1>=p?1:0;
}
int main()
{
    int t,s,n,p,i,j,score,ans;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        printf("Case #%d: ",i);   
        
        ans=0;
        scanf("%d%d%d",&n,&s,&p);
        for(j=0;j<n;j++)
        {
            scanf("%d",&score);
            if(checkp(score,p))ans++;
            else if(checks(score,p)&&s>0)
            {
                s--;
                ans++;   
            }
        }
        
        printf("%d\n",ans);
    } 
    
}
