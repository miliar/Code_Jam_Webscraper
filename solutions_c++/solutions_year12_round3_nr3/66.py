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
typedef pair<ll,ll> paii;


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
#define MAX 120

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

int n,m;

paii box[MAX];
paii toys[MAX];
ll dp[MAX][MAX];

//ll rec(int b,int t, int new_b,int new_t)
//{
//    deb(b,t,new_b,new_t);
//    if(b>=n || t>=m) return 0;
//    ll &ret=dp[b][t][new_b][new_t];
//    if(ret!=-1) return ret;
//    ret=0;
//    if(box[b].sc!=toys[t].sc)
//    {
//        ret=max(ret,rec(b+1,t,1,new_t));
//        ret=max(ret,rec(b,t+1,new_b,1) );
//    }
//    else
//    {
//        ll actual_box;
//        ll actual_toy;
//        if(new_b==0 && new_t==1)
//        {
//            actual_toy=toys[t].fs;
//            for(int x=t-1;x>=0;x--)
//            {
//                if(toys[x].sc==box[b].sc)
//                {
//                    actual_box=box[b].fs-toys[x].fs;
//                    break;
//                }
//            }
//        }
//        else if( new_b==1 && new_t==0)
//        {
//            actual_box=box[b].fs;
//            for(int x=b-1;x>=0;x--)
//            {
//                if(toys[t].sc==box[x].sc)
//                {
//                    actual_toy=toys[t].fs-box[x].fs;
//                    if(actual_toy==0)
//                    {
//                        for(int y=t-1;y>=0;y--)
//                        {
//                            if(toys[t].sc==toys
//                        }
//                    }
//                    break;
//                }
//            }
//        }
//        else if( new_b==1 && new_t==1)
//        {
//            actual_box=box[b].fs;
//            actual_toy=toys[t].fs;
//        }
//        deb("box",actual_box,"toy",actual_toy);
//        if(actual_box>actual_toy)
//        {
//            ret=max(ret,rec(b,t+1,0,1) + actual_toy );
//        }
//        else if(actual_toy>actual_box)
//        {
//            ret=max(ret,rec(b+1,t,1,0) + actual_box );
//        }
//        else if(actual_box==actual_toy)
//        {
//            ret=max(ret,rec(b+1,t+1,1,1) + actual_box );
//        }
//
//    }
//    return ret;
//
//}

ll rec(int b,int t)
{
    if(b>=n || t>=m)  return 0;
    ll &ret=dp[b][t];
    if(ret!=-1) return ret;
    ret=0;
    ret=max(ret,rec(b+1,t) );

    ll tot_box=0;
    for(int i=b;i<n;i++)
    {
        if(box[b].sc==box[i].sc) tot_box+=box[i].fs;
        ll tot_toy=0;
        for(int j=t;j<m;j++)
        {
            if(toys[j].sc==box[b].sc) tot_toy+=toys[j].fs;
            ret=max(ret,rec(i+1,j+1) + min( tot_toy,tot_box  ) );
        }
    }
    return ret;

}

int main(void)
{
    freopen("inC.txt","r",stdin);
    freopen("outC.txt","w+",stdout);
    ll ans=0;
    ll cas,loop=0,a,b;
    scanf("%lld",&cas);
    while(cas--)
    {
        scanf("%d %d",&n,&m);
        for(int i=0;i<n;i++) {scanf("%lld %lld",&a,&b);box[i]=mp(a,b);}
        for(int i=0;i<m;i++) {scanf("%lld %lld",&a,&b);toys[i]=mp(a,b);}

        mem(dp,-1);
        ans=rec(0,0);

        printf("Case #%lld: %lld\n",++loop,ans);
//        deb(ans);
    }
    return 0;
}


