#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int main()
{
    FILE * fp1,*fp2;
    int T,out=1,A,B;
    double p[100005],ans1,ans2,ans3;
    fp1=fopen("e:\\cjin.in","r+");
    fp2=fopen("e:\\cjout.txt","w+");
    fscanf(fp1,"%d",&T);
    while(T--)
    {
        fscanf(fp1,"%d %d",&A,&B);
        for(int i=1;i<=A;i++)
            fscanf(fp1,"%lf",&p[i]);
        p[0]=1;
        for(int i=2;i<=A;i++)
            p[i]=p[i]*(p[i-1]);

        ans1=p[A]*(B-A+1)+(1-p[A])*(B+1+B-A+1);
        ans2=B+2;
        ans3=min(ans1,ans2);

        for(int i=1;i<=A;i++)
           {
               double temp=p[A-i]*(2*i+B-A+1)+(1-p[A-i])*(2*i+B-A+1+B+1);
               ans3=min(ans3,temp);
           }
        fprintf(fp2,"Case #%d: %.6lf\n",out++,ans3);
    }
    return 0;
}
