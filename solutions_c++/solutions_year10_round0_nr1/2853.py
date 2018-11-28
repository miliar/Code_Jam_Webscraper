#include<iostream>
#include<string>

using namespace std;

int main()
{
    int T; cin>>T;
    for(int t = 1; t <= T; ++t){
        int N,K;
        cin>>N>>K;

        if((K+1)%(1<<N) == 0) cout<<"Case #"<<t<<": ON"<<endl;
        else cout<<"Case #"<<t<<": OFF"<<endl;
    }

    return 0;
}
