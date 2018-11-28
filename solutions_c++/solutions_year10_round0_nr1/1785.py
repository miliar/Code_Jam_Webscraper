#include<iostream>
using namespace std;
int main()
{
    int T,K,N;
    cin>>T;
    for(int i=1;i<=T;i++)
    {
        cin>>N>>K;
        int sum=1<<N;
        if((K+1)%sum==0)
        printf("Case #%d: ON\n",i);
        else printf("Case #%d: OFF\n",i);
    }
}
