#include<iostream>
#include<cstdio>
#include<math.h>
using namespace std;

  int main()
    {
         freopen("input.txt","r",stdin);
         freopen("output.txt","w",stdout);

         int tc=1,t,l,j;
         long long int a,b,n,r,count;
         cin>>t;
         for(;tc<=t;tc++)
          {
              cin>>a>>b;
              count = 0;
              for(long long int i = a ;i<=b;i++)
               {   
                   n = i;
                  // j = 0;
                   l = (int)(log((double)n)/log((double)10));
                   do
                   {
                   r = n%10;
                   n = n/10;
                   n = (long long int)pow(10,(double)(l))*r+n;
                   
                   if(n>=a&&n<=b&&n!=i)
                     { count++;
                     //cout<<"\n"<<n<<" "<<i;
                     }    
                  // j++
                   }while(n!=i);    
                   
               }          
              
              cout<<"Case #"<<tc<<": "<<count/2<<"\n";
                            
          }   
                //system("PAUSE");
                return 0;
    }    

    
