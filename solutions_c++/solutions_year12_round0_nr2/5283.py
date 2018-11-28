#include<iostream>
using namespace std;
int main()
{
    int t,i,j,n,s,a,temp,ans,sur,p;
    cin>>t;
    for(i=1;i<=t;i++)
    {
         cin>>n>>s>>p;
         sur = s;
         temp = 3*p;
         ans = 0;
         while(n >0)
         {
             cin>>a;
             if( a == 0)
             { if(p == 0)
                     ans++;
             }
             else if( a ==1 )
             {  if(p <=1)
                     ans++;
             }
             
             else if(a>=(temp-2)) {ans++;}
             else if((a >= temp -4) && sur >0) {ans++; sur--;}    
             n--;   
         }
         cout<<"Case #"<<i<<": "<<ans<<endl;            
    }
    return 0;
}
