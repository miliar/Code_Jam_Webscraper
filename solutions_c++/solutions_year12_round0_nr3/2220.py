using namespace std;
#include<stdio.h>
#include<math.h>
int a[2000005];
int power(int a,int b)
{
    int i,prod=1;
    for(i=1;i<=b;i++)
    prod=prod*a;
    return(prod);
}
int main()
{
    int t,x,y,i,p,len,tem,j,last,zerolen,factor,store;
    long long count,localcount;
    scanf("%d",&t);
    for(p=1;p<=t;p++)
    {
        scanf("%d%d",&x,&y);
        len=0;
        tem=x;
        while(tem!=0)
        {
            len++;
            tem=tem/10;
        }

        for(i=0;i<2000003;i++)
        a[i]=0;
        count=0;

        for(i=x;i<y;i++)
        {
            if(a[i]!=1)
            {
                localcount=0;
                //printf("i=%d len=%d\n",i,len);
                a[i]=1;
                store=i;
                for(j=1;j<=len-1;j++)
                {
                    last=store%10;
                    if(last!=0)
                    {
                        tem=(store-last)/10+(last*power(10,len-1));
                        if(tem<=y&&tem>i&&a[tem]!=1)
                        {
                            localcount++;
                            a[tem]=1;
                            //printf("11111tem=%d\n",tem);
                        }
                        //printf("tem=%d\n",tem);
                        store=tem;
                    }
                    else
                    {
                        zerolen=0;
                        tem=store;
                        while(tem!=0&&tem%10==0)
                        {
                            zerolen++;
                            tem=tem/10;
                        }

                        if(!(len-zerolen<=1))
                        {
                            factor=power(10,zerolen+1);
                            last=store%factor;

                            //printf("factor=%d last=%d",factor,last);
                            tem=(store-last)/factor+(last*power(10,len-zerolen-1));

                            j+=(zerolen);
                            if(tem<=y&&tem>i&&a[tem]!=1)
                            {
                                localcount++;
                                a[tem]=1;
                                //printf("222222tem=%d\n",tem);
                            }
                            //printf("tem=%d\n",tem);
                            store=tem;
                        }
                    }
                }
                if(localcount>1)
                count=count+((localcount+1)*localcount)/2;
                else
                count+=localcount;
            }
        }
        if(len==1)
        printf("Case #%d: 0\n",p);
        else
        printf("Case #%d: %lld\n",p,count);
    }
    return(0);
}
