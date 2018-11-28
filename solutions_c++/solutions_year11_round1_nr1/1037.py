#include<iostream>
#include<fstream>
using namespace std;
long long yf(long long &big,long long &small)
{
     while(big%2==0 && small%2==0)
     {
        big/=2;small/=2;
     }
     while(big%5==0 && small%5==0)
     {
        big/=5;small/=5;
     }
}
bool isPoss(long long n,long long pg,long long pd)
{
     if(pg==0 && pd!=0){return false;}
     if(pd==0 && pg!=0){return false;}
     if(pd==100 && pg!=100){return false;}
     if(pd!=100 && pg==100){return false;}
     long long big=100;
     yf(big,pg);
     if(big>n){return false;}
     
     return true;
}
int main()
{
    int t;
    ifstream cin("p1.in");
    ofstream cout("p2.out");
    cin>>t;
    
    for(int j=1;j<=t;j++)
    {
            long long n,pg,pd;
            cin>>n>>pg>>pd;
            bool flag=isPoss(n,pg,pd);
            if(flag){
                     cout<<"Case #"<<j<<": Possible"<<endl;
            }
            else{
                 cout<<"Case #"<<j<<": Broken"<<endl;
            }
    }
                     
}
