#include<stdio.h>
int main()
{
    int i,j,t,n,s,p,a[105],x,count1,count2,y;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        count1=0;
        count2=0;

        scanf("%d %d %d",&n,&s,&p);
        for(j=0;j<n;j++)
            scanf("%d",&a[j]);

        for(j=0;j<n;j++)
        {
            if(a[j]==0 && p==0){
                count1++;
                continue;
            }

            if(a[j]==0)
                continue;


            x=a[j]%3;
            if(x==2)
                y=(a[j]/3)+1;
            else
                y=(a[j]/3)+x;
            switch(x)
            {
                case 0:
                if(p-y<=0)
                    count1++;
                else if(p-y==1)
                {
                    count1++;
                    count2++;
                }
                break;

                case 1:
                    if(p-y<=0)
                    count1++;
                break;

                case 2:
                    if(p-y==1)
                    {
                        count1++;
                        count2++;
                    }
                    else if(p-y<=0)
                        count1++;
            }

        }
        //printf("%d %d ",count1,count2);
        x = s-count2;
        if(x<0)
            printf("Case #%d: %d\n",i+1,count1+x);
        else
            printf("Case #%d: %d\n",i+1,count1);
    }
    return 0;
}
