#include<iostream>
#include<cmath>
using namespace std;
int arr[31]={0};
int main()
{
 
    for(int i=1;i<=30;i++)
    {
            arr[i]=pow(2.0,double(i));
                        
            }       
   long r=0;         
   cin>> r;
   long i=1;
   while(r--)
   {
          long long n,k;
          cin>>n>>k;
          int set=arr[n];
          int remain=k%set;
          int flag=0;
          
          if(remain==set-1)    flag=1;
          else flag=0;
          cout<<"Case #"<<i++<<": ";
          if(flag==1) cout<<"ON"<<endl;
          else cout<<"OFF"<<endl;
          
           
           }
   // getchar();
    return 0;
}
