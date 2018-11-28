#include <iostream>

using namespace std;

int main()
{
    freopen("A_input.txt","r",stdin);
    freopen("A_output.txt","w",stdout);

    int x=1,T,N,K;

    cin>>T;

    while(T--)
    {
        cin>>N>>K;
        cout<<"Case #"<<x++<<": "<<((!((K+1)%(1<<N)))?"ON":"OFF")<<endl;
    }

    return 0;
}
