#include<iostream>
using namespace std;
int main()
{int t,n,cop=1;
cin>>t;
  while(t--)
  {int a[1000]={0};
  int b[1000]={0};
  long counter=0;
  cin>>n;
  for(int i=0;i<n;i++)
      cin>>a[i]>>b[i];
      for(int i=0;i<n;i++)
          for(int j=i+1;j<n;j++)
             {if(a[j]<a[i])
                 {int temp1;
                    temp1=a[i];
                    a[i]=a[j];
                    a[j]=temp1;
                    temp1=b[j];
                    b[j]=b[i];
                    b[i]=temp1;
                 }
             }
             
             
    for(int i=0;i<n;i++)
         {if(b[i]>=a[i])
             { for(int j=0;j<n;j++)
                    if((b[j]<b[i])&&(a[j]>a[i]))
                       counter++;
             }
           else 
               {
                       for(int j=0;j<n;j++)
                    if((b[j]>b[i])&&(a[j]<a[i])&&(b[j]<a[j]))
                       counter++;
               }   
         }
       cout<<"Case #"<<cop<<": "<<counter<<endl; 
       cop++; 
  }
 
}         
                 
    
