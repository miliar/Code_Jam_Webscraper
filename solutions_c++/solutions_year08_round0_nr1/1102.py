#include <vector>
#include <map>
#include <limits>
#include <cstdlib>
#include <algorithm>
using namespace std;

int main()
{
    int n,s,q;
    vector<string> engines;
    vector<string> queries;
    map<string,int> first_query;
    string tmp;
    getline(cin,tmp);
    n=atoi(tmp.c_str());
    for(int i=1;i<=n;i++)
    {
        cout<<"Case #"<<i<<": ";
        engines.clear();
        queries.clear();
        first_query.clear();
        getline(cin,tmp);
        s=atoi(tmp.c_str());
        for(int j=1;j<=s;j++)
        {
            getline(cin,tmp);
            engines.push_back(tmp);
        }
        getline(cin,tmp);
        q=atoi(tmp.c_str());
        for(int j=1;j<=q;j++)
        {
            getline(cin,tmp);
            queries.push_back(tmp);
        }
        int start=0;
        int ans=0;
        while(start!=numeric_limits<int>::max())
        {
            for(int j=0;j<s;j++)
                first_query[engines[j]]=numeric_limits<int>::max();

            for(int j=start;j<q;j++)
            {
                if(first_query[queries[j]]==numeric_limits<int>::max())
                    first_query[queries[j]]=j;
            }

            for(map<string,int>::iterator it=first_query.begin();it!=first_query.end();it++)
            {
                if(it->second>start) start=it->second;
            }
            ans++;
        }
        cout<<ans-1<<endl;
    }
    return 0;
}
