#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    ifstream cin("f1.in");
    ofstream cout("f2.out");
    int t;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
            int n;
            cin>>n;
            long long ans;
            long long minnum;
            long long yh;
            long long tem;
            cin>>tem;
            ans=tem;
            minnum=tem;
            yh=tem;
            for(int i=1;i<n;i++)
            {
               cin>>tem;
               if(tem<minnum){minnum=tem;}
               yh^=tem;
               ans+=tem;
            }
            if(yh==0){cout<<"Case #"<<j<<": "<<(ans-minnum)<<endl;}
            else{cout<<"Case #"<<j<<": NO"<<endl;}
    }
            
}
        
        
