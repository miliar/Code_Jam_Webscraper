#include<iostream>
using namespace std;
int power(int a,int n)
{
  int pro=1;
  for(int i = 0;i<n;i++)
        pro = pro * a ;
  return pro;
}
int main()
{
  long int t,oindex=0,min,n,sum,val[15],bin[20],i,j,soln=0,output[100];
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  cin>>t;
  while(t > 0)
     {
       min = 0;
       soln = 0;
       sum = 0;
       for(i=0;i<20;i++)
         {
                bin[i] = 0 ;                 
         }   
       cin>>n;
       for(i=0;i<n;i++)
          {
                cin>>val[i];
          }
       for(i=0;i<n;i++)
          {
                for(j=0;j<20;j++)
                  {
                        if(power(2,j)&val[i])
                            bin[j]++;
                  }
          }
       for(i=0;i<n;i++)
          {
                if(bin[i]%2 == 1)
                   soln = -1;      
          }
       if(soln == -1)
          {
                output[oindex++]=-1  ;        
          }
       else
          {
                sum = val[0];
                min = val[0];
                for(i=1;i<n;i++)
                   {
                     sum = sum + val[i];
                     if(min>val[i])
                        {
                                    min = val[i];                
                        }
                   }    
                sum = sum - min;
                output[oindex++] = sum;
          }
       t--;
     }    
    for(i=0;i<oindex;i++)
    {
       if(output[i] > 0)
             cout<<"Case #"<<i+1<<": "<<output[i]<<endl;                     
       else
             cout<<"Case #"<<i+1<<": NO"<<endl;
    
    }
}
