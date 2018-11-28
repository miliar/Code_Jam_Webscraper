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

//#include <conio.h>
//#define wait getch()
int n,s,p;
int arr[MAX];
int dp[MAX][MAX];

int max_surprise(int total)
{
    int mod=total%3;
    total-=mod;
    int player=total/3;
    if(mod==2 ) player+=2;
    if(mod==1 || mod==0 ) player++;
    player=min(player,10);
    return player;
}

int max_score(int total)
{
    int mod=total%3;
    total-=mod;
    int player=total/3;
    if(mod==1 || mod==2 ) player++;
    player=min(player,10);
    return player;
}

int rec(int pos, int surprise)
{
    if(pos>=n)
    {
        if(surprise==0) return 0;
        else return -1*oo;
    }
    int &ret=dp[pos][surprise];
    if(ret!=-1) return ret;

    ret=0;int count1=0,count2=0;int pt_s=0,pt=0;
    if(surprise && arr[pos]<=28  && arr[pos]>=2 ) pt_s=max_surprise(arr[pos]);
    pt=max_score(arr[pos]);

    if(pt_s>=p) count1++;
    if(pt>=p) count2++;

    if(surprise && arr[pos]<=28  && arr[pos]>=2 ) ret=max(ret,rec(pos+1,surprise-1) + count1 );
    ret=max(ret,rec(pos+1,surprise) +  count2);
    return ret;
}
int main(void)
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w+",stdout);

    int cas,loop=0;
    scanf("%d",&cas);
    while(cas--)
    {
        mem(dp,-1);
        scanf("%d %d %d",&n,&s,&p);
        for(int i=0;i<n;i++) scanf("%d",&arr[i]);

        int ans=rec(0,s);
//        deb(ans);
        printf("Case #%d: %d\n",++loop,ans);
    }
    return 0;
}

