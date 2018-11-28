#include<iostream>
using namespace std;
int GCD(int diff[])
{
            int a=diff[0],b=diff[1],c=diff[2];
            while(a%b != 0)
                 {
                      a = a%b;
                      a = a^b;
                      b = a^b;
                      a = a^b;
                 }
                 a = c;
                 while(a%b != 0)
                 {
                      a = a%b;
                      a = a^b;
                      b = a^b;
                      a = a^b;
                 } 
            return b;
}             
int main()
{
    int test_cases,i,n;
    int x[3],diff[3],gcd;
    cin>>test_cases;
    for(i=0;i<test_cases;i++) 
    {
               cin>>n;
               for(int j=0;j<n;j++)
                 cin>>x[j];   
               if(n==2)
               {
                       gcd = x[1]-x[0];
                       gcd *= (gcd < 0)? -1 : 1;
               }
               else
               {
                   int u=0;
                   diff[u] = x[1] - x[0];
                   if(diff[u]!=0)
                   u++;
                   diff[u] = x[2] - x[0];
                   if(diff[u]!=0)
                   u++;
                   diff[u] = x[1] - x[2];
                   if(diff[u]==0)
                   u--;
                   if(u==-1)
                   {
                            gcd =0;
                   }
                   else
                   {
                       if(u<2)
                       {
                              gcd = diff[0];
                              gcd *= (gcd < 0)? -1 : 1;
                       }
                       else
                       {
                           diff[0] *= (diff[0] < 0)? -1 : 1;
                           diff[1] *= (diff[1] < 0)? -1 : 1;
                           diff[2] *= (diff[2] < 0)? -1 : 1;
                           gcd = GCD(diff);
                       }
                   }
                   
                   
               } 
               int temp = 0;
               if(gcd !=0)
                 temp = x[0]%gcd;
               if(temp!=0)
                          temp = gcd - temp;
               cout<<"Case #"<<(i+1)<<": "<<temp<<"\n";
               
    }
    return 0;
}
