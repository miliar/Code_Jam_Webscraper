#include<stdio.h>
int min,max;
inline void fastread(int *a)
{
    register char c=0;
    while (c<33) c=getchar();
    *a=0;
    while (c>33)
    {
        *a=*a*10+c-'0';
        c=getchar();
    }
}
inline int find(int n)
{
    int t=0;
    while(n){n/=10;t++;}
    return --t;
}
int main()
{
    int t,k,i,j,sum,f,t1,t2;
    fastread(&t);k=t;
    while(t--)
    {
              fastread(&min);
              fastread(&max);
              f=find(max);
              t1=1;
              sum=f;
              while(sum--)
              t1*=10;
              sum=0;
              for(i=min;i<=max;i++)
              {
              t2=(i%t1)*10+(i/t1);
              while(t2!=i)
              {
              if(i<t2&&t2<=max)  sum++;
              t2=(t2%t1)*10+(t2/t1);
              }
              }
              printf("Case #%d: %d\n",k-t,sum);
    }
    return 0;
}
