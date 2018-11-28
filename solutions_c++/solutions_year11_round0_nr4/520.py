#include<iostream>

using namespace std;

int t,n,temp1,sum;

int main()
{
    cin>>t;
    
    for(int q=1;q<=t;q++)
    {
        cin>>n;
        sum=0;
        for(int i=1;i<=n;i++)
        {
            cin>>temp1;
            if(temp1==i)
                continue;
            sum++;
        }
        
        cout<<"Case #"<<q<<": "<<sum<<".000000\n";
    }
}