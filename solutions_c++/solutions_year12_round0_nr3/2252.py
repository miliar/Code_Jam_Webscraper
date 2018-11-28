#include<fstream>
#include<math.h>
#include<iostream>
using namespace std;
int digits(int x)
{
    int d=0;
    while(x>0)
    {
    x=x/10;
    d++;
    }
    return d;
}

int power(int n)
{
    int i, res=1;
    if (n==0)
       return 1;
    for (i=1;i<=n;i++)
       res=10*res;
    return res;
}

int recycle(int x, int k)
{
    int num,d,y;
    num=x%power(k);
    y=x/power(k);
    d=digits(y);
    num=num*power(d)+y;
    return num;
}

main()
{
      fstream fout;
      fout.open("barsha.txt");
      int t,i,j,a,b,d,k,count=0,rec,arr[15], flag=0,f=0,x;
      scanf("%d", &t);
      for(j=1;j<=t;j++)
         {
         count=0;
         scanf("%d",&a);
         scanf("%d",&b);
         d=digits(a);
         fout<<"Case #"<<j<<": ";
         for(i=a;i<=b;i++)
            {
            flag=0;
            for(k=1;k<d;k++)
               {
               f=0;
               rec=recycle(i,k);
               if(rec>i && rec<=b)
                  {
                  for(x=0;x<flag;x++)
                     if(arr[x]==rec)
                       {f++;break;}      
                  if (f==0)
                  {
                  arr[flag++]=rec;
                  count++;
                  }
                  }
               }
         }
         fout<<count<<"\n";
         }
}
