#include<stdio.h>
//#include<conio.h>
#include<math.h>
int main()
{
        int a,b,A[4],i,t,x,c,y,j,temp[4],k,l,m,count=0,c1=0;
        scanf("%d",&t);
        while(t--)
        {
                count=0;
                scanf("%d%d",&a,&b);
                x=a;
                c=1;
                c1++;
                while(x/10!=0)
                {
                        c++;
                        x=x/10;
                }
                l=pow(10,c-1);
                for(i=a;i<=b;i++)
                {
                                x=i;
                                for(j=c-1;j>=0;j--)
                                {
                                        A[j]=x%10;
                                        x/=10;
 
                                }
                                for(k=0;k<c-1;k++)
                                {
                                        m=l;
                                        temp[k]=0;
                                        for(j=k+1;j<c;j++)
                                        {
                                                temp[k]+=(A[j]*m);
                                                m=m/10;
                                        }
 
                                        for(j=0;j<k+1;j++)
                                        {
                                                temp[k]+=(A[j]*m);
                                                m=m/10;
                                        }
 
 
                                }
                                for(k=0;k<c-1;k++)
                                {
                                        for(j=k+1;j<c-1;j++)
                                        {
                                                if(temp[j]==temp[k])
                                                temp[j]=0;
                                        }
                                        if(temp[k]>i&&temp[k]<=b)
                                        count++;
                                }
 
                }
                printf("\nCase #%d: %d",c1,count);
        }
        //getch();
        return(0);
}
