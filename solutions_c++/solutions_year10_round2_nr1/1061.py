#include <stdio.h>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>

using namespace std;
set<string> dirs;

vector<string> get(string s)
{
    int i,f;
    vector<string> adds;
    vector<string> returnt;
    i=0;
    f=s.find("/");
    while (f!=-1)
    {
        f=s.find("/",f+1,1);
        adds.push_back(s.substr(0,f));
        //printf("f=%d\n",f);
    }
    adds.push_back(s);
    //for (i=0; i<adds.size(); i++) cout<<adds[i]<<"_"<<endl;
    return adds;
}

int process(string s)
{
    int i,cnt=0;
    vector<string> adds;
    adds=get(s);
    //cout<<"s="<<adds.size();
    for (i=0; i<adds.size(); i++)
    {
        //cout<<adds[i]<<endl;
        if (dirs.find(adds[i])==dirs.end())
        {
            cnt++;
            dirs.insert(adds[i]);
        }
        //cout<<cnt<<endl;
    }
    return cnt;
}



int main()
{
    freopen("ina","r",stdin);
    freopen("outa","w",stdout);
    int t,cas,i,n,m,ans,j;
    scanf("%d",&t);

    for (cas=1; cas<=t; cas++)
    {
        scanf("%d%d",&n,&m);
        vector<string> adds;
        string s;
        dirs.clear();
        for (i=0; i<n; i++)
        {
            cin>>s;
            adds=get(s);
            for (j=0; j<adds.size(); j++)
            {
                dirs.insert(adds[j]);
            }
        }
        set<string> :: iterator it;
        //for (it=dirs.begin(); it!=dirs.end(); it++) cout<<(*it)<<endl;
        ans=0;
        for (i=0; i<m; i++)
        {
            cin>>s;
            int z;
            z=process(s);
            ans+=z;
            //printf("%d\n",z);
            //for (it=dirs.begin(); it!=dirs.end(); it++) cout<<(*it)<<endl;
        }
        printf("Case #%d: %d\n",cas,ans);
    }

	return 0;
}
