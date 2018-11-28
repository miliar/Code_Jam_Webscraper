#include <stdio.h>
#include <iostream>
#include <map>
using namespace std;

map<string, int> record;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    string s;
    int ca, i,n,m,l,ans,cas=0;
    cin>>ca;
    while (ca--)
    {
        cin>>n;
        getline(cin, s);
        record.clear();
        for (i=0;i<n;++i)
        {
            getline(cin, s);
            record[s]=0;
        }
        cin>>m;
        getline(cin,s);
        for (l=n,ans=i=0;i<m;++i)
        {
            getline(cin,s);
            if (record.find(s)==record.end()) continue;
            if (record[s]==0) 
            {
                if (l==1)
                {
                    ++ans;
                    for (map<string, int>::iterator idx=record.begin(); idx!=record.end(); ++idx)
                        idx->second=0;
                    l=n;
                }
                record[s]=1;
                --l;                
            }
        }
        cout<<"Case #"<<++cas<<": "<<ans<<endl;
    }
    return 0;
}
