#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int cas=1;cas<=t;++cas)
    {
        cout<<"Case #"<<cas<<": ";
        long long n,pd,pg;
        cin>>n>>pd>>pg;
        if(pg==100)
        {
            if(pd==100)cout<<"Possible"<<endl;
            else cout<<"Broken"<<endl;
            continue;
        }
        if(pg==0)
        {
            if(pd==0)cout<<"Possible"<<endl;
            else cout<<"Broken"<<endl;
            continue;
        }
        if(n>=100)
        {
            cout<<"Possible"<<endl;
            continue;
        }
        bool flag=false;
        for(int i=1;i<=n;++i)
        {
            if((i*pd)%100==0)flag=true;
        }
        if(flag)cout<<"Possible"<<endl;
        else cout<<"Broken"<<endl;
    }
    return 0;
}
