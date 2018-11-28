#include<iostream>

using namespace std;

int main()
{
    long long int t,N,K,i,j;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin>>t;
    for(int test=1;test<=t;test++)
    {
        int ans=0;
        cin>>N;
        cin>>K;
        int y=(1<<N);
        int temp=K%y;
       
        //cout<<p;
        if(temp==(1<<N)-1)
            ans=1;
        else
            ans=0;
        
        if(ans==0)
             cout<<"Case #"<<test<<": OFF\n";
        else
            cout<<"Case #"<<test<<": ON\n";
    }
    return 0;
}
