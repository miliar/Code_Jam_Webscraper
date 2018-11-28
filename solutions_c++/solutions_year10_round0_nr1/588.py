#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    
    int T;
    cin>>T;
    for (int i=1; i<=T; ++i)
    {
        int N,K;
        cin>>N>>K;
        int prog=1<<N;
        cout<<"Case #"<<i<<": ";
        if (K%prog==prog-1) cout<<"ON"<<endl;
        else cout<<"OFF"<<endl;
    }   
    return 0;
}
