#include<iostream>

using namespace std;

int main()
{
    int t = 0;
    cin>>t;
    for(int i = 0 ; i < t ; i++)
    {
            int n;
            cin>>n;
            long long res = 0;
            long long sum = 0;
            long long min = 100000000;
            for(long j = 0 ; j < n ; j++)
            {
                    long long a;
                    cin>>a;
                    if(a < min)
                      min = a;
                    res ^= a;   
                    sum += a;
            }
             cout<<"Case #"<<i+1<<": ";
             if(res == 0)
                   cout<<sum-min<<endl;
             else
                   cout<<"NO"<<endl;  
    } 
   
             
    return 0;
}
