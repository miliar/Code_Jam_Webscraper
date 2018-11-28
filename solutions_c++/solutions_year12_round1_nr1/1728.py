#include<stdio.h>
#include<iostream>
#include<math.h>
using namespace std;
float A,B;
int T;
float p[100003];
main()
{
    freopen("/Users/thanardkurutach/Desktop/Round1A/A-small-attempt0.in","r",stdin);
    freopen("/Users/thanardkurutach/Desktop/Round1A/A-small-attempt0.out","w",stdout);
    scanf("%d",&T);
    float min,mult,check;
    for(int i=0;i<T;i++)
    {
        scanf("%f %f",&A,&B);
        for(int j=1;j<=A;j++)
        {
            scanf("%f",&p[j]);
            //cout<<p[i];
            //cout<<p[i];
        }
        min=B+2;
        for(int j=0;j<=A;j++)
        {
            //cout<<p[1];
            check=0;
            mult=1;
            for(int k=1;k<=A-j;k++)
            {
     //                           cout<<"$$$"<<mult<<endl;
   // printf("#%f",p[k]);
                mult*=p[k];
            }
            check+=mult*(2*j+B-A+1);
            check+=(1-mult)*(2*j+2*B-A+2);
            //cout<<check<<endl;
            if(check<min)
            {
                min=check;
            }
        }
        printf("Case #%d: %f\n",i+1,min);
    }




}
