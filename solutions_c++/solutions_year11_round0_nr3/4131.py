#include <iostream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <cmath>
using namespace std;

#define sqr(a) ((a)*(a))


int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int T,N,C[1000];
    cin>>T;
    for(int t=1; t<=T; t++)
    {
        memset(C,0,sizeof(C));
        cin>>N;
        for(int n=0; n<N; n++) cin>>C[n];
        sort(C,C+N);
        bool yes=true;
        int sum=0;
        for(int i=0; i<24; i++)
        {
            sum=0;
            for(int j=0; j<N; j++)
            {
                if((C[j]>>i)&1)sum++;
            }
            if(sum%2==0)continue;
            else
            {
                yes=false;
                break;
            }
        }
        sum=0;
        for(int i=0;i<N;i++)sum+=C[i];
        if(yes)
        {
            cout<<"Case #"<<t<<": "<<sum-C[0]<<endl;
        }
        else
        {
            cout<<"Case #"<<t<<": NO"<<endl;
        }
    }
    return 0;
}






