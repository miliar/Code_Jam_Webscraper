#include<iostream>
using namespace std;
int gcd(int a,int b)
{
     if(b==0)
     return a;
     return gcd(b,a%b);
}
string isitpossible()
{
       long long n;
            int d,g;
            cin>>n>>d>>g;
            if(g==100 && d!=100)
            return "Broken";
            if(g==0 && d!=0)
            return "Broken";
            int f=100/gcd(100,d);
            if(f>n)
            return "Broken";
            
            return "Possible";
}
            
int main()
{
    int T;
    cin>>T;
    for(int i=1;i<=T;i++)
    {
           string ret=isitpossible();
           cout<<"Case #"<<i<<": "<<ret<<endl;
    }
    return 0;
}
               
