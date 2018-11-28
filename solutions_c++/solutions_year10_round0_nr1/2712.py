#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
int main()
{    
     long long temp,i,n,k,t;
        long long flag=0,temp2,temp3;
             cin>>t;
     for(i=1;i<=t;i++)
     {
               temp=0;flag=0,temp2=0,temp3=0;
               cin>>n>>k;
               
               temp=((pow(2,n))-1);
               temp2=pow(2,n);
               temp3=k%temp2;
               if(temp3==temp)
               flag=1;
               else
               flag=0;
               
              
                if(flag)
                cout<<"Case #"<<i<<": "<<"ON"<<endl;
                else
              cout<<"Case #"<<i<<": "<<"OFF"<<endl;
     }
    
   return 0;
}
