#include <iostream>
#include <algorithm>

using namespace std;

int T,N,val[2000];
int tmp,m;

bool ck()
{
    tmp=0;
    m=1<<30;
    int sum=0;
    for(int i=0;i<N;i++)
    {
        sum^=val[i];
        tmp+=val[i];
        m=min(m,val[i]);
    }
    return sum==0;
}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    cin>>T;
    for(int cnt=1;cnt<=T;cnt++)
    {
        cin>>N;
        for(int i=0;i<N;i++)
            cin>>val[i];
        if(ck())
        {
            cout<<"Case #"<<cnt<<": "<<tmp-m<<endl;
        }
        else
        {
            cout<<"Case #"<<cnt<<": NO"<<endl;
        }
    }
    return 0;
}
