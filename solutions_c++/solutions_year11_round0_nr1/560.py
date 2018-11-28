#include <iostream>
#include <cmath>
#include <algorithm>
#include <stdio.h>
using namespace std;

void test()
{
    int O=1,B=1,rO=0,rB=0,time=0;
    int i,N,x,d;
    char c;
    cin>>N;
    for(i=0;i<N;i++)
    {
        cin>>c>>x;
        //cout<<"C"<<c<<"x"<<x<<endl;
        if(c=='O')
        {
            d=(x-O);

            if(d<0) d*=-1;

            //cout<<"Od"<<d<<" ";
            if(rO<d) d-=rO;
            else d=0;
            time+=(d+1);
            rB+=d+1;
            rO=0;
            O=x;
        }
        else
        {
            d=x-B;
            if(d<0) d*=-1;

            //cout<<"Bd"<<d<<" ";

            if(rB<d) d-=rB;
            else d=0;
            time+=(d+1);
            rO+=d+1;
            rB=0;
            B=x;
        }
    }
    cout<<time;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int i,T;
    cin>>T;
    for(i=0;i<T;i++)
    {
      cout<<"Case #"<<i+1<<": ";
      test();
      cout<<endl;
    }
    return 0;
}
