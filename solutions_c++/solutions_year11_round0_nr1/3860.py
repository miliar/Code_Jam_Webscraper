#include <iostream>
#define MAX 10000
using namespace std;

void solve()
{
    int i,j,N;
    int O,B;
    cin>> N;
    O=B=1;
    
    
    
    int time,timeO,timeB,use;
    time=timeO=timeB=0;
    
    for(i=0;i<N;i++)
    {
        string who;
        int x;
        cin>>who>>x;
        if(who[0]=='O')
        {
            timeO -= abs(O-x);
            O = x;
            
            if(timeO<0)
                use = 1-timeO;
            else
                use = 1;
            timeO = 0;
            timeB += use;
            time += use;
        }
        else
        {
            timeB -= abs(B-x);
            B = x;

            if(timeB<0)
                use = 1-timeB;
            else
                use = 1;
            timeB = 0;
            timeO += use;
            time += use;
        }    
    }
    cout<<time<<endl;
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
