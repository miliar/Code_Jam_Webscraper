#include<iostream>
#include<string.h>
#include<vector>
#include<math.h>
#include<limits.h>
using namespace std;




class Snapper 
{
    public:
    string solve(long long int n, long long int k);
};


string Snapper::solve(long long int n, long long int k)
{
    if(((k+1)%(1<<n))==0)
        return "ON";
    else
        return "OFF";

}

int main()
{

    Snapper sn;
//    string ans = sn.solve(1,0);
//    cout<<"the ans is "<<ans;
    long long int t,n,k;
    cin>>t;
    for(long long int i=0;i<t;i++)
    {
        cin>>n;
        cin>>k;
        cout<<"Case #"<<(i+1)<<": "<<sn.solve(n,k)<<endl;
    }

}


