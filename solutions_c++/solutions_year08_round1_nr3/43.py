#include	<cstdio>
#include	<cstdlib>
#include	<cstring>
#include	<string>
#include	<vector>
#include	<cmath>
#include	<algorithm>
#include	<cassert>
#include	<set>
#include	<map>
#include	<queue>
#include	<iostream>
#include <sstream>
using namespace std;
#define pb push_back
#define REP(i,n) for(int i=0;i<(n);i++ ) 

typedef long long LL;
typedef pair<int,int> piii;

int t1,t2,t3;
int res[1000];

map<int,int> m;

int main()
{
        t1=2,t2=6;
        int T;
        cin>>T;
        int max1=-1;
        REP(i,T)
        {
                int tmp;
                cin>>tmp;
                m[tmp]=i;
                max1=max(max1,tmp);
        }
        REP(i,max1+1)
        {
                if (i>=2)
                {
                        t3=(6*t2-4*t1)%1000;
                        if (m.find(i)!=m.end())
                        {
                                //cout<<'x'<<i;
                                res[m[i]]=(t3-1+1000)%1000;
                        }
                        t1=t2;t2=t3;
                }
                if (i%10000000==0)
                        cerr<<i<<endl;
        }
        REP(i,T)
        {
                ostringstream sout;
                sout<<res[i];
                string r=sout.str();
                while (r.size()!=3)
                        r="0"+r;
                cout<<"Case #"<<i+1<<": "<<r<<endl;
        }
}
