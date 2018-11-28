#include<iostream>

    using namespace std;

int main()
{
    int T,N,i,j;
    long int K,a,d;
    cin>>T;
    for(i=0;i<T;i++)
    {
        cin>>N>>K;
        a=1;
        for(j=0;j<N;j++)
            a*=2;
        a--;
        d=a+1;
        if((K-a)%d==0)
            cout<<"Case #"<<i+1<<": ON\n";
        else
            cout<<"Case #"<<i+1<<": OFF\n";

    }
    return 0;
}
