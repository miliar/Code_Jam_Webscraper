#include <iostream>
using namespace std;
int n,k;
int main()
{

    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    int K=1;
    cin>>t;
    while(t--)
    {
        cin>>n>>k;
        if(k%(1<<n)==(1<<n)-1)
            cout<<"Case #"<<K<<": ON\n";
        else
            cout<<"Case #"<<K<<": OFF\n";
        K++;
    }
    return 0;
}
