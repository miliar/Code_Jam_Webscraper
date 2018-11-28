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

map<string,int> m;

int t[1000];
int t2[1000];

int main()
{
        string s;
        int n;
        cin>>n;
        REP(nn,n)
        {
                //cout<<'a'<<nn<<endl;
                int S;
                m.clear();
                cin>>S;
                getline(cin,s);
                //cout<<S<<"x"<<s<<endl;
                REP(i,S)
                {
                        getline(cin,s);
                        //cout<<s<<endl;
                        m[s]=i;
                }
                //break;
                int M;
                cin>>M;
                getline(cin,s);
                REP(i,S)
                        t2[i]=0;
                REP(tmp,M)
                {
                        getline(cin,s);
                        //cout<<tmp<<' '<<s<<endl;
                        REP(i,S)
                                t[i]=10000;
                        REP(i,S)
                                REP(j,S)
                                        t[i]=min(t2[j]+(i!=j),t[i]);
                        t[m[s]]=100000;
                        REP(i,S)
                                t2[i]=t[i];
                }
                int res=100000;
                REP(i,S)
                        res=min(res,t[i]);
                printf("Case #%d: %d\n",nn+1,res);
        }
                return 0;
}
