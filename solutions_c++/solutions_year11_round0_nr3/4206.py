#include<iostream>
using namespace std;
int main()
  { int t,k=1,i=0,j=0,flag=0;
    long long *c,temp;
    long long n,sum=0,max=0;
    cin>>t;
    while(k<=t)
      { flag=0;
        long long x=0,y=0;
        cin>>n;
        c=new long long[n];
        for(i=0;i<n;i++)
           { cin>>c[i];
           }
         for(i=0;i<n;i++)
            for(j=0;j<n;j++)
              { if(c[i]<c[j])
                   { temp=c[i];
                     c[i]=c[j];
                     c[j]=temp;
                   }
              }
         for(i=0;i<n;i++)
           { x=x^c[i];
             for(j=i+1;j<n;j++)
               { y=y^c[j]; sum+=c[j];
               }
             if(x==y)
               { if(max<sum)
                   {  max=sum;flag=1;
                   }
               }    
             y=0;sum=0;   
           }
        if(flag==1)  
          cout<<"Case #"<<k<<":  "<<max<<"\n";
        else
          cout<<"Case #"<<k<<":  "<<"NO\n";
        max=0;
        k++;
      }
     return 0;
   }            
                            
