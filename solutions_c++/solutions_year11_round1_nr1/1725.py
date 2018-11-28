//kunal10

#include<stdio.h>
#include<math.h>
using namespace std;
int main()
{
    int i,j,k,t,gcd,m,n,temp,max,min,d,count;
    float Pd,Pg;
    long long int N;
    scanf("%d",&t);
    j=1;
    while(j<=t)
    {
          scanf("%lld %f %f",&N,&Pd,&Pg);
          if (Pg==100 && Pd!=100){printf("Case #%d: Broken\n",j);j++;continue;}
          if (Pg==0 && Pd!=0){printf("Case #%d: Broken\n",j);j++;continue;}

          Pd = Pd/100;
          count=0;
          while( (Pd-(int)Pd) != 0){Pd = Pd*10;count++;}
          m=1;i=0;
          while(i<count){m=m*10;i++;}
          n=(int)Pd;
            //printf("m=%d n=%d count=%d\n",m,n,count);
          if (m>n){max=m;min=n;}
          else {max=n;min=m;}

                        //finding GCD
                        while(min!=0)
                        {
                                temp=min;
                                min=max%min;
                                max=temp;
                        }

                        gcd=max;

        d = m/gcd;

        if (d<= N){
            printf("Case #%d: Possible\n",j);
        }

        else {printf("Case #%d: Broken\n",j);}

        j++;
    }

    return 0;
}

