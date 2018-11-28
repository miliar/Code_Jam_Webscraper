#include <iostream>

using namespace std;

int main()
{
    int i,T,N,suma,xr=0,j=10000000,k,l;
    cin>>T;
    for(i=0;i<T;i++)
    {
        j=10000000;
        xr=0;
        suma=0;
        cin>>N;
        for(k=0;k<N;k++)
        {
            cin>>l;
            if(l<j)j=l;
            suma+=l;
            xr=xr^l;
        }
        if(xr==0) cout<<"Case #"<<i+1<<": "<<suma-j<<endl;
        else cout<<"Case #"<<i+1<<": NO"<<endl;
    }
    return 0;
}
