#include<iostream>
#include<vector>
#include<cstdio>
#include<string>

using namespace std;

int main()
{   
    int a,s;
    cin>>a;
    for(int q=0;q<a;q++)
    {
           cin>>s;
           long int x=0;
           long int sum=0;
           long int min=1000000;
           vector<long int> arr(s);
           for(int i=0;i<s;i++)
               {
                   cin>>arr[i];
                   x=x^arr[i];
                   sum+=arr[i];
                   if(arr[i]<min)
                     min=arr[i];
               }
            
   
            if(x==0)
             cout<<"Case #"<<q+1<<": "<<sum-min<<endl;
            else
             cout<<"Case #"<<q+1<<": "<<"NO"<<endl;
     }
     return 0;
}             
