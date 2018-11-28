#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    int T,n,cnt1=0,cnt2,out=1,s,p,ans;
    int a[101];
    FILE * fp1,*fp2;
    fp1=fopen("d:\\3.in","r+");
    fp2=fopen("d:\\3.out","w+");

    fscanf(fp1,"%d",&T);
    while(T--)
    {
        cnt1=cnt2=0;ans=0;
        fscanf(fp1,"%d %d %d",&n,&s,&p);
        for(int i=1;i<=n;i++)
           {
           fscanf(fp1,"%d",&a[i]);
           if((a[i]==3*p-4&&(3*p-4>=0))||(a[i]==3*p-3&&(3*p-3>0))) cnt1++;
           else if(a[i]>=3*p-2)         cnt2++;
           }
        if(cnt1>s)
        ans=s+cnt2;
        else
        {
            ans=cnt1+cnt2;
        }
        fprintf(fp2,"Case #%d: %d\n",out++,ans);
    }

    fclose(fp1);
    fclose(fp2);
    return 0;
}
