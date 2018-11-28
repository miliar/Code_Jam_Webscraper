#include<iostream>
using namespace std;

int main()
{
    long long t,n,a,b,i,j=0,min,sum,num;
    cin>>t;
    while(t--)
    {
            cin>>n;j+=1;
            cin>>num;min=num;sum=num;a=num;
            //cout<<"a->"<<a<<"\n";
            for(i=1;i<n;i++){  
            cin>>num;
            if(num<min)min=num;
            sum+=num;
            a=a^num;//cout<<"a->"<<a<<"\n";
            }
            if(a==0)cout<<"Case #"<<j<<": "<<(sum-min)<<"\n";
            else cout<<"Case #"<<j<<": NO\n";
            
            }
    
    return 0;
}
