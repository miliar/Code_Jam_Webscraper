#include<iostream>


using namespace std;
#include<math.h>
int main()
{
    freopen ("out.txt","w",stdout);
    freopen("A-large.in", "r", stdin);

    int ntest;
    cin>>ntest;
    
    for(int i=1;i<=ntest;i++)
    {
    long long int N,K;
    cin>>N>>K;
    
    long long int mod = 1;  // 2^N
    
    for(int I=0;I<N;I++)
    {
            mod*=2;
    }
    K++;
    
    if( K%mod == 0) 
    {
    cout<<"Case #"<<i<<": "<<"ON"<<endl;
    }
    else
    cout<<"Case #"<<i<<": "<<"OFF"<<endl;
    
    }
  //  system("pause");
    return 0;
    
}
