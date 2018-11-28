#include <iostream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <cmath>
using namespace std;

#define sqr(a) ((a)*(a))

typedef unsigned long long UL;

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    //freopen("C-small-attempt1.in","r",stdin);
    //freopen("C-small-attempt1.out","w",stdout);
    UL N,L,H,C[10000];
    int T;
    bool yes;
    cin>>T;
    for(int t=1; t<=T; t++)
    {
        cin>>N>>L>>H;
        for(int i=0;i<N;i++)
        {
            cin>>C[i];
        }
        sort(C,C+N);
        UL i;
        for(i=L;i<=H;i++)
        {
            yes=true;
            UL j;
            for(j=0;j<N && C[j]<=i;j++)
            {
                if(i%C[j]!=0)
                {
                    yes=false;
                    break;
                }
            }
            if(!yes)continue;
            for(;j<N;j++)
            {
                if(C[j]%i!=0)
                {
                    yes=false;
                    break;
                }
            }
            if(yes)break;
        }
        if(yes)
        {
            cout<<"Case #"<<t<<": "<<i<<endl;
        }
        else
        {
            cout<<"Case #"<<t<<": NO"<<endl;
        }
    }
    return 0;
}






