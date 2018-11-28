#include<iostream>
using namespace std;

int main()
{
    int T, N, K, c;
    cin>>T;
    for(c=1; c<=T; c++)
    {
        cin>>N>>K;
        K++;
        if(K%(1<<N))
            cout<<"Case #"<<c<<": OFF\n";
        else
            cout<<"Case #"<<c<<": ON\n";
    }
}
