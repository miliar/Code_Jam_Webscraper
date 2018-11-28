#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
int main()
{    
     double temp,i,n,k,t;
        int flag=0;
             cin>>t;
     for(i=1;i<=t;i++)
     {
               temp=0;flag=0;
               cin>>n>>k;
               
               temp=((pow(2,n))-1);
               while(temp<=k)
               {
                             if(k==temp)
                              {
                                        flag=1;
                                        break;
                              }
                            else
                             temp=temp+pow(2,n);
                }
                if(flag)
                cout<<"Case #"<<i<<": "<<"ON"<<endl;
                else
              cout<<"Case #"<<i<<": "<<"OFF"<<endl;
     }
     
   return 0;
}
