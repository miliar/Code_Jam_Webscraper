#include <iostream>
#include <stdio.h>
using namespace std;

bool pair1(int i,int j)
{
    if((i>=10)&&(i<=99)&&(j>=10)&&(j<=99))
    {
        if(i%10==j/10&&i/10==j%10) return 1;
        return 0;
    }
    else if((i>=100)&&(i<=999)&&(j>=100)&&(j<=999))
    {
        int a=j%10;
        j/=10;
        int b=j%10;
        int c=j/10;
        int a1=i%10;
        i/=10;
        int b1=i%10;
        int c1=i/10;
        if(b1==a&&c1==b&&a1==c) return 1;
        if(b1==c&&a1==b&&c1==a) return 1;
        return 0;
    }
    return 0;
}

int main()
{
    int n,A,B,cnt=0,out=1;
    FILE * fp1,*fp2;
    fp1=fopen("d:\\2.in","r+");
    fp2=fopen("d:\\2.out","w+");
    fscanf(fp1,"%d",&n);
    while(n--)
    {   cnt=0;
        fscanf(fp1,"%d %d",&A,&B);
        for(int i=A;i<=B;i++)
           for(int j=i+1;j<=B;j++)
              if(pair1(i,j))
                 cnt++;
        fprintf(fp2,"Case #%d: %d\n",out++,cnt);
    }
    fclose(fp1);
    fclose(fp2);
    return 0;
}
