#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

bool isRecycled(int n, int m)
{
    int i,cnt,mcnt,mod;

    if(n<100)
    {
        cnt=1;
        mod=10;
    }
    else if(n<1000)
    {
        cnt=2;
        mod=100;
    }
    else if(n<10000)
    {
        cnt=3;
        mod=1000;
    }
    if(m<100) mcnt=1;
    else if(m<1000) mcnt=2;
    else if(m<10000) mcnt=3;

    if(cnt!=mcnt)
        return false;

    for(i=0; i<cnt; i++)
    {
        n=((n%mod)*10)+(n/mod);
        if(n==m)
            return true;
    }
    return false;
}

main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("op.txt","w",stdout);

    int t,tc,a,b,i,j,cnt;

    vector < pair<int,int> > v;


    for(i=1; i<3001; i++)
    {
        for(j=i+1; j<3001; j++)
            if(isRecycled(i,j))
                v.push_back(make_pair(i,j));
    }

    j=v.size();

    cin>>t;
    for(tc=1; tc<=t; tc++)
    {
        cin>>a>>b;

        cnt=0;
        for(i=0; i<j && v[i].first<=b; i++)
            if(v[i].first>=a && v[i].second<=b)
                cnt++;

        printf("Case #%d: %d\n",tc,cnt);
    }


    //for(i=0; i<j; i++)
        //cout<<v[i].first<<' '<<v[i].second<<endl;

//    if(isRecycled(12,21))
//        cout<<"Yes"<<endl;
//    else
//        cout<<"No"<<endl;

    return 0;
}
