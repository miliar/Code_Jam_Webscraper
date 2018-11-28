#include<stdio.h>
#include<math.h>
int T,A,B,count=0;


int numDigits(const int n) {
    if (n < 10) return 1;
    return 1 + numDigits(n / 10);
}

void pairs(int j,int B)
{
    int temp,dig,num,diglen=numDigits(j),c=1;
    temp=j;
    
    while(c<=diglen)
    {
        dig=temp%10;
        temp=temp/10;
        temp=temp+(pow(10,diglen-1)*dig);
        if(temp<=B && temp>j)
        {
                count++;
                //printf("%d-%d \n",j,temp);
        }
         c++;
    }
}


int main()
{
    int i=1,j,res;
    scanf("%d",&T);
    for(;i<=T;i++)
    {
        scanf("%d %d",&A,&B);
        count=0;
        for(j=A;j<=B;j++)
        {
            pairs(j,B);
        }
        printf("Case #%d: %d\n",i,count);
    }
    return 1;
}

        