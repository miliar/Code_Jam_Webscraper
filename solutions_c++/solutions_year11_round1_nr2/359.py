#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <queue>
using namespace std;
#define   sqr(a)         ((a)*(a))
#define   rep(i,a,b)  for(int i=(a);i<(int)(b);i++)
#define   per(i,a,b)  for(int i=((a)-1);i>=(int)(b);i--)
#define   PER(i,n)     per(i,n,0)
#define   REP(i,n)     rep(i,0,n)
#define   FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define   clr(a)      memset((a),0,sizeof (a))
#define   SZ(a)         ((int)((a).size()))
#define   CLEAR(a, v)    memset((a), (v), sizeof(a))
#define   ALL(v)          (v).begin(), (v).end()
#define   mabs(a)       ((a)>0?(a):(-(a)))
#define   inf         1000000001
#define  MAXN     10061
#define  eps      1e-6
#define   PB push_back
#define   FI 		first
#define   SE 		second
#define   MP 		make_pair
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
typedef long long int64;
int N,M;
string s[MAXN];
int ms[MAXN][30];
char gs[30];
typedef struct node
{
    int cnt;
    map<pair<int,int >,node> mpn;
    int msk;
}node;
map<int,node> mroot;
void tclear(node &a)
{
    FOREACH(it,a.mpn) tclear(it->second);
    a.mpn.clear();
    a.cnt=0;a.msk=0;
}
void inserttree(node &root,int idx)
{
    node *u=&root;
    REP(i,26)
    {
        pair<int,int> key=make_pair(gs[i]-'a',ms[idx][gs[i]-'a']);
        if(key.second>0) u->msk|=(1<<key.first);
        if(u->mpn.count(key)>0)
        {
            u=&u->mpn[key];
            u->cnt++;
        }
        else
        {
            node tmp;tmp.cnt=1;u->mpn[key]=tmp;tmp.msk=0;
            u=&u->mpn[key];
        }
    }
}
int solve(node &root,int idx)
{
    node *u=&root;
    if(u->cnt==1) return 0;
    int ans=0;
    REP(i,26)
    {
        pair<int,int> key=make_pair(gs[i]-'a',ms[idx][gs[i]-'a']);
        if(ms[idx][gs[i]-'a']==0&&(u->msk&(1<<(gs[i]-'a') ))) ans++;
        u=&u->mpn[key];
        if(u->cnt==1) return ans;
    }
    return ans;
}
int main()
{
    int T;scanf("%d",&T);
    REP(roud,T)
    {
        printf("Case #%d: ",roud+1);
        scanf("%d%d",&N,&M);
        char cs[15];
        REP(i,N)
        {
            scanf("%s",cs);s[i]=string(cs);
        }
        REP(i,N) REP(j,26)
        {
            int t=0;
            REP(k,s[i].length()) if(s[i][k]-'a'==j) t|=(1<<k);
            ms[i][j]=t;
        }
        REP(i,M)
        {
            int mv=-1;
            string res;
            scanf("%s",gs);
            FOREACH(it,mroot) tclear(it->second);
            mroot.clear();
            REP(j,N)
            {
                int len=s[j].length();
                if(mroot.count(len)==0)
                {
                    node tmp;tmp.cnt=1;tmp.msk=0;
                    mroot[len]=tmp;
                }
                else mroot[len].cnt++;
                inserttree(mroot[len],j);
            }
            REP(j,N)
            {
                int len=s[j].length();
                int tv=solve(mroot[len],j);
                if(tv>mv) mv=tv,res=s[j];
           //     printf("%s %d\n",s[j].c_str(),tv);
            }
            if(i<M-1)printf("%s ",res.c_str());
            else printf("%s\n",res.c_str());
        }
    }
    return 0;
}
