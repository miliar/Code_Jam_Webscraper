#include<iostream>

using namespace std;

int main()
{
    int T;
    cin>>T;

    for(int k = 1; k <= T; k++)
    {
        unsigned long long N, K, TwoPowN;
        cin>>N>>K;
       
        TwoPowN = 1 << N;

        cout<<"Case #"<<k<<": ";
        if(K % TwoPowN == TwoPowN - 1) cout<<"ON";
        else cout<<"OFF";
        cout<<endl;

    }

    return 0;

}

