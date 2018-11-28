#include<stdio.h>
int main()
{
    int n,s,p,m,l,i,t,count=0,j=1;
    int a[102];
    scanf("%d",&t);
    while(t--){
        count=0;
    scanf("%d%d%d",&n,&s,&p);
    for(i=1;i<=n;i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=1;i<=n;i++)
    {
        m=a[i]%3;
        l=a[i]/3;
        if(l>=p)
        count++;
        else if((((p-l)==2)&&(m==2)&&(s!=0)))
        {
            count++;
            s--;
        }
        else if((((p-l)==1)&&(m>=1))||(((p-l)==0)&&(m>=0)))
        {
            count++;
        }
        else if((((p-l)==1)&&(m==0)&&(s!=0)&&(a[i]!=0)))
        {
            s--;
            count++;
        }
    }
    printf("Case #%d: %d\n",j,count);
    j++;
    }
    return 0;
}
