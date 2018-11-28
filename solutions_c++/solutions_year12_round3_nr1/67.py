#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <cctype>
#include <set>
#include <bitset>
#include <algorithm>
#include <list>
#include <vector>
#include <sstream>
#include <iostream>

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> paii;


#define PI (2*acos(0))
#define ERR 1e-5
#define mem(a,b) memset(a,b,sizeof a)
#define pb push_back
#define popb pop_back
#define all(x) (x).begin(),(x).end()
#define mp make_pair
#define SZ(x) (int)x.size()
#define oo (1<<25)
#define FOREACH(it,x) for(__typeof((x).begin()) it=(x.begin()); it!=(x).end(); ++it)
#define Contains(X,item)        ((X).find(item) != (X).end())
#define popc(i) (__builtin_popcount(i))
#define fs      first
#define sc      second
#define EQ(a,b)     (fabs(a-b)<ERR)
#define MAX 1010

template<class T1> void deb(T1 e){cout<<e<<endl;}
template<class T1,class T2> void deb(T1 e1,T2 e2){cout<<e1<<" "<<e2<<endl;}
template<class T1,class T2,class T3> void deb(T1 e1,T2 e2,T3 e3){cout<<e1<<" "<<e2<<" "<<e3<<endl;}
template<class T1,class T2,class T3,class T4> void deb(T1 e1,T2 e2,T3 e3,T4 e4){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<endl;}
template<class T1,class T2,class T3,class T4,class T5> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<endl;}
template<class T1,class T2,class T3,class T4,class T5,class T6> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5,T6 e6){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<" "<<e6<<endl;}


template<class T> T Abs(T x) {return x > 0 ? x : -x;}
template<class T> inline T sqr(T x){return x*x;}
ll Pow(ll B,ll P){      ll R=1; while(P>0)      {if(P%2==1)     R=(R*B);P/=2;B=(B*B);}return R;}
int BigMod(ll B,ll P,ll M){     ll R=1; while(P>0)      {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return (int)R;} /// (B^P)%M

///int rrr[]={1,0,-1,0};int ccc[]={0,1,0,-1}; //4 Direction
///int rrr[]={1,1,0,-1,-1,-1,0,1};int ccc[]={0,1,1,1,0,-1,-1,-1};//8 direction
///int rrr[]={2,1,-1,-2,-2,-1,1,2};int ccc[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
///int rrr[]={2,1,-1,-2,-1,1};int ccc[]={0,1,1,0,-1,-1}; //Hexagonal Direction
///int month[]={31,28,31,30,31,30,31,31,30,31,30,31}; //month


int n;
vector<int>v[MAX];
int go[MAX][MAX];

int dfs(int node,int end)
{
    if(node==end) return 1;

    int &ret=go[node][end];
    if(ret!=-1) return ret;
    ret=0;
    for(int i=0;i<SZ(v[node]);i++)
    {
        go[node][v[node][i]]=1;
        ret=dfs(v[node][i] ,end );
    }
    return ret;
}
int main(void)
{
    freopen("inA.txt","r",stdin);
    freopen("outA.txt","w+",stdout);
    int cas,loop=0,e,val,ok;
    scanf("%d",&cas);
    while(cas--)
    {
        scanf("%d",&n);
        for(int i=0;i<=n;i++) v[i].clear();
        for(int i=1;i<=n;i++)
        {
            scanf("%d",&e);
            for(int t=0;t<e;t++) {scanf("%d",&val);v[i].pb(val);}
        }
        mem(go,-1);
//        for(int i=1;i<=n;i++) dfs(i);

        ok=0;
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=n;j++)
            {
                if(i==j) continue;
//                deb("calc",i,j,SZ(v[i]));
                if(SZ(v[i])<2) continue;
                int match=0;
//                deb("connection",i,j);
                for(int p=0;p<SZ(v[i]);p++)
                {
                    if( dfs(v[i][p],j)  ) match++;
                }
//                deb("match",match);
                if(match>1) {ok=1;break;}
            }
        }
        if(ok==0) printf("Case #%d: No\n",++loop);
        else printf("Case #%d: Yes\n",++loop);
    }
    return 0;
}

