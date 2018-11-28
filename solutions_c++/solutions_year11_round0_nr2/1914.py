
#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<vector>
#include<cmath>
#include<map>
#include<list>
#include<set>

using namespace std;

#define FOR(a,with,b) for(a=with;a<b;a++)
#define v       vector<int>
#define vs      vector<string>

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int i,j,m,n,k,kase,len,ind;
    char ar[210][210],b[220],res[200];

    vs com;
    vs opps;
    map<char,int>mp1;
    vector<int>list[200];
    string tar;

    cin>>kase;

    string input="QWERASDF";

    FOR(i,0,8)list[input[i]].clear();

    k=1;

    while(kase--)
    {   FOR(i,0,8)list[input[i]].clear();

        memset(ar,0,sizeof(ar));
        memset(b,0,sizeof(b));
        mp1.clear();

        cin>>n;
        string ss;

        FOR(i,0,n)
        {    cin>>ss;
             com.push_back(ss);
             ar[ss[0]][ss[1]]=ss[2];
             ar[ss[1]][ss[0]]=ss[2];
        }
        cin>>m;

        FOR(i,0,m)
        {   cin>>ss;
            opps.push_back(ss);
            list[ss[0]].push_back(ss[1]);
            list[ss[1]].push_back(ss[0]);
        }

        char ch,valu;
        cin>>len>>tar;
        ind=0;

        FOR(i,0,len)
        {
              if(ind>0)
              {   if(ar[res[ind-1]][tar[i]])
                  {   mp1[res[ind-1]]--;
                      res[ind-1]=ar[res[ind-1]][tar[i]];
                      mp1[res[ind-1]]++;
                  }
                  else
                  {   int check=0;
                      FOR(j,0,list[tar[i]].size())
                      {     if(check==1)break;
                            if(mp1[list[tar[i]][j]]){check=1;break;}
                      }
                      if(check==1){mp1.clear();ind=0;continue;}
                      res[ind]=tar[i];
                      mp1[tar[i]]++;
                      ind++;
                  }
              }
              else
              {     res[ind]=tar[i];
                    mp1[tar[i]]++;
                    ind++;
              }
        }
      //  cout<<ind<<endl;
        cout<<"Case #"<<k<<": [";

        for(i=0;ind && i<ind-1;i++)
            cout<<res[i]<<", ";
        if(ind)
        cout<<res[ind-1];
        cout<<"]"<<endl;
        k++;
    }
    return 0;
}
