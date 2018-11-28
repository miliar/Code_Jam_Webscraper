using namespace std;
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<vector>
int main()
{
    int t,val,rem,count,a,b,temp,ind=1;
    scanf("%d",&t);
    while(t--)
    {
              count=0;
              scanf("%d%d",&a,&b);
              for(int i=a;i<=b;i++)
              {
                      if(a<10)
                      val=1;
                      else if(a<100)
                      val=2;
                      else if(a<1000)
                      val=3;
                      else
                      val=4;
                      
                      temp=i;
                      for(int j=0;j<val;j++)
                      {
                           rem=temp%10;
                           temp/=10;
                           temp=rem*(int)pow((double)10,val-1)+temp;
                           if(temp>i && temp<=b)
                           count++;
                      }
                      
               }
               printf("Case #%d: %d\n",ind++,count);
    }
return 0;
}
