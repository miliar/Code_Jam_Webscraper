#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<iomanip>
using namespace std;
bool possible(int n,int pd,int pg)
{
    bool ret=false;
    for(int i=1;i<=n;i++)
    {
        if((i*pd)%100==0)
        {
            if(pg>=1&&pg<100)
            {
                ret=true;
                break;
            }
            else if((pg==100&pd==100)||(pg==0&&pd==0))
            {
                ret=true;
                break;
            }
        }
    }
    return ret;
}

int main()
{
    int t,n,pd,pg;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cin>>n>>pd>>pg;
        cout<<"Case #"<<i<<": ";
        if(possible(n,pd,pg))
            cout<<"Possible"<<endl;
        else
            cout<<"Broken"<<endl;
    }
    return 0;
}
