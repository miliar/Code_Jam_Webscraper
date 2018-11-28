#include<iostream>
#include<cstdio>
#include<cmath>
int jud[2000010];
using namespace std;
int main()
{
    //freopen("t.txt","r",stdin);
    //freopen("t2.txt","w",stdout);
    int t,caseno,a,b,num[7],temp,nn;
    scanf("%d",&t);
    for(caseno=1;caseno<=t;caseno++)
    {
        scanf("%d%d",&a,&b);
        int sum=0,mm;
        for(int i=0;i<=2000010;i++) jud[i]=0;
        for(int i=a;i<=b;i++)
        {
            temp=i;
            int tail=0,dd=1;
            while(temp>0)
            {
                num[tail++]=temp%10;
                temp/=10;
                dd*=10;
            }
            dd/=10;
            mm=i;
            for(int j=0;j<tail;j++)
            {
                nn=0;
                for(int k=tail-1;k>=0;k--)
                {
                    nn*=10;
                    nn+=num[(k+j)%tail];
                }
                //cout<<nn<<endl;
                if(nn/dd!=0&&nn>=a&&nn<=b)
                {
                    mm=min(mm,nn);
                }
            }
            if(mm>=a&&mm<=b)
            {
                jud[mm]++;
                sum+=jud[mm]-1;
               // if(jud[mm]>1)  cout<<mm<<"  "<<i<<endl;
            }
        }
        printf("Case #%d: %d\n",caseno,sum);
    }
    return 0;
}
