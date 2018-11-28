#include <iostream>

using namespace std;

int T;

int main(){
    freopen("A-small.in","r",stdin);
    freopen("A-small.out","w",stdout);
    cin>>T;
    for (int i=1;i<=T;i++)
    {
        int N,K;
        scanf("%d%d",&N,&K);
        if (!((K+1)&((1<<N)-1))) cout<<"Case #"<<i<<": ON\n";
        else cout<<"Case #"<<i<<": OFF\n";
    }
    return 0;
}
