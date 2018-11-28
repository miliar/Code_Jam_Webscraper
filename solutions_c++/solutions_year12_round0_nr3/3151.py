#include<stdio.h>
int main()
{
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        int A,B;
        int count=0,n=0,temp,p=0,num;
        char str1[50];
        scanf("%d %d",&A,&B);
        temp=A;
        while(temp)
        {
            temp/=10;
            n++;
        }
        for(int j=A;j<B;j++)
        {
            p=0;
            temp=j;
            while(temp)
            {
                str1[n-p-1]=(temp%10+48);
                p++;
                temp/=10;
            }
            int l;
            for(l=0;l<n;l++)
            {
                str1[n+l]=str1[l];
            }
            int len=2*l;
            for(int k=0;k<len-n;k++)
            {
                num=0;
                for(int x=0;x<n;x++)
                {
                    num=(num*10) + (str1[x+k]-48);
                }
                if((num<=B)&&(j<num))
                {
                    count++;
                    //printf("%d  %d\n",num,j);
                }
            }
        }
        printf("Case #%d: %d\n",i+1,count);
    }
    return 0;
}
