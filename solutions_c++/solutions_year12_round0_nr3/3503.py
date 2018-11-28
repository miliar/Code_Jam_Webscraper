#include<stdio.h>
#include<math.h>
int main()
{
    int i=0,j=0,a=0,b=0,tmp=0;
    int t=0,nm[3],k=0,count=0,dig=0;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d %d",&a,&b);
        printf("Case #%d: ",i);
        count=0;
        for(j=a;j<b;j++)
        {
            if((j/10)!=0)
            {
                tmp=j;
	        dig=0;
                for(k=0;k<3;k++)
                {
                    if(tmp/1!=0)
                    {
                        dig++;
                        nm[k]=tmp%10;
                        tmp/=10;
                    }
                }
                if(dig==2)
                {
                    if(((nm[dig-1]*pow(10,dig-2)+nm[dig-2]*pow(10,dig-1))>j)&&((nm[dig-1]*pow(10,dig-2)+nm[dig-2]*pow(10,dig-1))<=b))
                        {
                            count++;
                        }
                }
                if(dig==3)
                {
                    if(((nm[dig-3]*pow(10,dig-1)+nm[dig-1]*pow(10,dig-2)+nm[dig-2]*pow(10,dig-3))>j)&&((nm[dig-3]*pow(10,dig-1)+nm[dig-1]*pow(10,dig-2)+nm[dig-2]*pow(10,dig-3))<=b))
                        count++;
                    if(((nm[dig-2]*pow(10,dig-1)+nm[dig-3]*pow(10,dig-2)+nm[dig-1]*pow(10,dig-3))>j)&&((nm[dig-2]*pow(10,dig-1)+nm[dig-3]*pow(10,dig-2)+nm[dig-1]*pow(10,dig-3))<=b))
                        count++;
                }


            }
        }
        printf("%d\n",count);
    }
    return 0;
}
