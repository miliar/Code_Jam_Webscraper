#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    long long n;
    cin>>n;
    long long c=0;
    while(c<n)
    {
              long long p,k,l;
              cin>>p>>k>>l;
             
              long long str[l];
             
              for(int i=0;i<l;i++) cin>>str[i];
              
              sort(str,str+l);
              unsigned long long sum=0;
              int g=1;
              int m=1;
              for(int i=l-1;i>=0;i--)
              {
                      sum+=str[i]*m;
                      if(g%k==0)
                      m++;
                      g++;
              }
            
      cout<<"Case #"<<++c<<": "<<sum<<"\n";        
    }
}
