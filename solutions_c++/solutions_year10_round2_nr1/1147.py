#include <iostream>
#include <string>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <list>
#include <set>
#include <cmath>
#include <cstring>
#include <stdio.h>
#include <string.h>
#include <sstream>
#include <stdlib.h>
#include <vector>

using namespace std;

#define INF 1<<28
#define SIZE 10000

#define REP(i,n) for (int i=0; i<n; ++i)
#define FOREACH(it,x) for(__typeof((x).begin()) it=(x.begin()); it!=(x).end(); ++it)
#define FOR(i,p,k) for (int i=p; i<=k; ++i)

#define MP(a,b) make_pair(a,b)

#define CLEAR(x,with) memset(x,with,sizeof(x))
#define SZ(x) (int)x.size()
#define PB push_back

#define gcd(a,b)    __gcd(a,b)

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef vector<int> vi;
typedef vector<string> vs;
typedef map<string,int> msi;

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);

    int i,j,k,l,cnt,minv,sum,test,m,n,Case=1,t,p;
    vector<int>dict[500],store;
    string str,s;
    char ch;
    map<string,int>mp;

    scanf("%d",&test);
    while(test--)
    {
        for(i=0;i<500;i++)
            dict[i].clear();
        mp.clear();
        scanf("%d %d",&n,&m);
        k=1;
        l=0;
        for(i=0;i<n;i++)
        {
            cin>>str;
            for(j=0;j<str.size();j++)
                if(str[j]!='/')
                {
                    s.clear();
                    for(j=j;j<str.size() && str[j]!='/';j++)
                        s+=str[j];
                    //cout<<s<<endl;
                    if(mp[s]==0)
                        mp[s]=k++;
                    dict[l].push_back(mp[s]);
                }
            /*for(j=0;j<dict[l].size();j++)
                cout<<dict[l][j]<<" ";
            cout<<endl;*/
            l++;
        }
        sum=0;
        for(i=0;i<m;i++)
        {
            cin>>str;
            store.clear();
            for(j=0;j<str.size();j++)
                if(str[j]!='/')
                {
                    s.clear();
                    for(j=j;j<str.size() && str[j]!='/';j++)
                        s+=str[j];
                    //cout<<s<<endl;
                    if(mp[s]==0)
                        mp[s]=k++;
                    store.push_back(mp[s]);
                }
            /*for(j=0;j<(int)store.size();j++)
                cout<<store[j]<<" ";
            cout<<endl;*/
            minv=(int)store.size();
            //cout<<" :"<<minv<<endl;
            for(j=0;j<l;j++)
            {
                cnt=(int)store.size();
                t=0;
                for(p=0;p<dict[j].size() && p<store.size();p++)
                    if(dict[j][p]!=store[p])
                        break;
                    else t++;
                cnt=cnt-t;
                minv=min(minv,cnt);
            }
            sum+=minv;
            //cout<<sum<<" "<<l<<endl;
            dict[l++]=store;
        }
        printf("Case #%d: %d\n",Case++,sum);
    }

    return 0;
}
