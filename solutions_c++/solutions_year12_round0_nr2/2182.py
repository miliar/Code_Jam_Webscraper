using namespace std;
#include<stdio.h>
//#include<conio.h>
int a[105],ns[105],s[105];
int max(int i,int j,int k)
{
    if(i>=j&&i>=k)
    return(i);
    else if(j>=i&&j>=k)
    return(j);
    else
    return(k);
}
int min(int i,int j,int k)
{
    if(i<=j&&i<=k)
    return(i);
    else if(j<=i&&j<=k)
    return(j);
    else
    return(k);
}
int min2(int i,int j)
{
    if(i<j)
    return(i);
    else return(j);
}
int main()
{
    int n,sur,p,i,j,k,x,y,sum,survalue,tem,nonvalue,rep,ans,t,tem2;
    scanf("%d",&t);
    for(x=1;x<=t;x++)
    {
        scanf("%d%d%d",&n,&sur,&p);

        for(i=0;i<n;i++)
        scanf("%d",&a[i]);

        for(i=0;i<n;i++)
        {ns[i]=0;s[i]=0;}

        for(y=0;y<n;y++)
        {
            for(i=10;i>=0;i--)
            for(j=10;j>=0;j--)
            for(k=10;k>=0;k--)
            {
                sum=i+j+k;
                if(sum==a[y])
                {
                    tem=max(i,j,k);
                    if(tem>=p)
                    {
                        tem2=tem-min(i,j,k);
                        if(tem2==2)
                        {
                            s[y]=1;
//                            printf("i=%d j=%d k=%d\n",i,j,k);
//                            printf("tem=%d min=%d tem2=%d a[%d]=%d\n",tem,min(i,j,k),tem2,y,a[y]);
//                            getch();
                        }
                        else if(tem2==1||tem2==0)
                        {
                            ns[y]=1;
                            s[y]=1;
//                            printf("i=%d j=%d k=%d\n",i,j,k);
//                            printf("tem=%d min=%d tem2=%d a[%d]=%d\n",tem,min(i,j,k),tem2,y,a[y]);
//                            getch();
                        }
                    }

                }
            }
        }

        nonvalue=0;
        survalue=0;
        rep=0;
        for(i=0;i<n;i++)
        {
            if(ns[i]==1)
            {
                nonvalue++;
                if(s[i]==1)
                {
                    survalue++;
                    rep++;
                }
            }
            else if(s[i]==1)
            survalue++;
        }
        ans=0;
        ans=(nonvalue-rep);

        if(sur>=survalue)
        ans+=survalue;
        else
        {
            ans=ans+sur+min2(rep,survalue-sur);
        }

//        for(i=0;i<n;i++)
//        printf("%d ",ns[i]);
//        printf("\n");
//        for(i=0;i<n;i++)
//        printf("%d ",s[i]);
//        printf("\n");
//        printf("non=%d survalue=%d rep=%d sur=%d\n",nonvalue,survalue,rep,sur);

        printf("Case #%d: %d\n",x,ans);
    }
}
