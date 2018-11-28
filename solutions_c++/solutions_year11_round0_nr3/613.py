#include <iostream>

using namespace std;

int main()
{
    int T,N,a,b,min,i,total;
    cin>>T;
    for(i=1;i<=T;i++)
    {
        cin>>N;
        cin>>a;
        min=a;
        total=a;
        N--;
        while(N--)
        {
            cin>>b;
            total+=b;
            if(b<min)
            {
                min=b;
            }
            a=a^b;
        }
        if(a==0)
        {
            cout<<"Case #"<<i<<": "<<total-min<<endl;
        }
        else
        {
            cout<<"Case #"<<i<<": NO"<<endl;
        }
    }
    return 0;
}
