
# include <iostream>
# include <cmath>

using namespace std;

int main()
{
    int t,l;
    cin>>t;
    for(l=1;l<=t;l++)
    {
           int n,k,i,j,p=1,r,flag;
           cin>>n>>k;
           for(j=0;j<n;j++)
              p *= 2;
           k = k % p;
           flag=0;
           if(k == (p-1))
             flag = 1;          
           if(flag == 1)
             cout<<"Case #"<<l<<": ON\n";
           else
             cout<<"Case #"<<l<<": OFF\n";         
    }    
}
