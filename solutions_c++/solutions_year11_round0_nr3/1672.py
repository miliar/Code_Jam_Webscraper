#include<iostream>
#include<math.h>
#include<string.h>
using namespace std;


int main()
{
    freopen("C:\\Users\\Administrator\\Downloads\\C-large.in", "r", stdin);
    freopen("C:\\Users\\Administrator\\Downloads\\out", "w", stdout);
   int T;
   int i;
   cin>>T;
   for(i=0;i<T;i++)
   {
       int n,count[100];
       memset(count,0,sizeof(count));
       cin>>n;
       int j;
       int min = 1000000,sum=0;
       for(j=0;j<n;j++)
       {
           int a;
           cin>>a;
           sum+=a;
           if(min>a)
             min=a;
           int k=0;
           while(a!=0)
           {
               if(a%2==1)
                 count[k]++;
               k++;
               a>>=1;
           }
       }
        bool sign = true;
       for(j=0;j<100;j++)
          if(count[j]%2!=0)
          {
           //   cout << j << "   " <<count[j] << endl;
              sign = false;
              break;
          } 
       if(sign)
       {
           cout<<"Case #"<<i+1<<": "<<sum-min<<endl;
       }
       else
           cout<<"Case #"<<i+1<<": "<<"NO"<<endl;
   }
 //  system("pause");
   return 0;
}
