#include<iostream>
using namespace std;

long long gp(long long a, long long b)
{
     long long p = a*b, mid;
     while(b>=a)
     {

         mid = (a+b)/2;
         cerr<<a<<' '<<b<<' '<<mid<<' '<<p<<endl;
         if(mid*mid >=p && (mid-1)*(mid-1) < p) return mid;
         else if (mid*mid > p) b = mid-1;
         else a = mid+1;
     }
     return mid+1;
}
             
    
int main()
{
    long long L,C,P,b,oldb;
    int T,t,a;
    
    cin>>T;
    for(t=1;t<=T;t++)
    {
        cin>>L>>P>>C;
        
        int a = 0;
        while(L*C<P)
        {
            cerr<<L<<' '<<P<<endl;
            P = gp(L,P);
            a++;
        }
        cout<<"Case #"<<t<<": "<<a<<endl;
    }
}
        
