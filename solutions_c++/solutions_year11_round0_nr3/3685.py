#include <iostream>
#define MAX 10000
using namespace std;

int candy[MAX];

void solve()
{
    int i,j,N;
    cin>>N;
    
    int sum=0,min=20000000;
    for(i=0;i<N;i++)
    {
        scanf("%d",&candy[i]);
        sum+=candy[i];
        if(min>candy[i])
            min=candy[i];
    }
    
    bool allzero;
    int even;
    while(1)
    {
        allzero=true;
        even = 0;
        for(i=0;i<N;i++)
        {
            even += candy[i]%2;
            candy[i]/=2;
            if(candy[i]!=0)
                allzero=false;
        }    
        if(even%2!=0)
        {
            cout<<"NO"<<endl;   
            return; 
        }
        
        if(allzero)
        {
            cout<<sum-min<<endl;    
            return;
        }
    }
}

int main()
{
    int T;
    cin>>T;
    for(int i=0;i<T;i++)
    {
        cout<<"Case #"<<i+1<<": ";
        solve();    
    }    
}
