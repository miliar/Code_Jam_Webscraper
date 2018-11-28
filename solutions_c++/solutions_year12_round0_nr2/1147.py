#include<iostream>
long long min(long long a,long long b)
{
     if(a<b)
            return a;
     else
         return b;
 }
using namespace std;
int main()
{   
    long long n,s,p;
    int test;
    cin>>test;
    int ctr=1;
    while(test--)
    {
    cin>>n>>s>>p;
    int count=0;
    int counts=0;
    for(int i=0;i<n;i++)
    {
            long long num;
            cin>>num;
            if(num/3>p)
            {
               count++; // cout<<"ASdasD"<<" "<<num<<endl;      
            }
            else
            {
                num=num-p;
                if((num/2)>=(p-1) && num>=0)
                    count++;
                else if((num/2)>=p-2 && num>=0)
                     counts++;
            }
              //  cout<<counts<<" "<<count<<" "<<num<<endl;
                    
            
    } 

     cout<<"Case #"<<ctr<<": "<<min(counts,s)+count<<endl;       
            ctr++;
}
    
    return 0;
}
