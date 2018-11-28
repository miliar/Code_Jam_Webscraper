#include<iostream>
#include<string>
#include<cstring>
#include<map>
#include<queue>
#include<deque>
#include<vector>
#include<algorithm>
#include<cmath>
#include<cstdio>
#include<cstdlib>
using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;

#define PI 2*acos(0.0)
#define ERR 1e-9
#define gcd(a,b) __gcd(a,b)
#define lcm(a,b) ((a)*((b)/gcd(a,b)))
#define area(x1,y1,x2,y2,x3,y3) ( x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2) )
#define sqr(x) ((x)*(x))
#define distSqr(x1,y1,x2,y2) ( sqr(x1-x2) + sqr(y1-y2) )
#define Wait system("pause")
#define Time printf("time=%.3lf sec.\n",(double) (clock())/CLOCKS_PER_SEC);

#define pb push_back
#define all(x) (x).begin(),(x).end()
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define SETB(a) memset(a,true,sizeof(a))
#define print(cse,x) printf("Case %d: %d\n",cse++,x)
#define print1(cse) printf("Case %d:\n",cse++)
#define printn(a) printf("%ld\n",a)
#define tin(x) scanf("%d",&x)
#define tin2(x,y) scanf("%d%d",&x,&y)
#define tin3(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define rep(i,n) for(int i=0;i<n;i++)
#define Mod 10000000007
#define INF 1<<30
#define Max 500010

template<class T1> void deb(T1 e){cerr<<e<<endl;}
template<class T1,class T2> void deb(T1 e1,T2 e2){cerr<<e1<<" "<<e2<<endl;}
template<class T1,class T2,class T3> void deb(T1 e1,T2 e2,T3 e3){cerr<<e1<<" "<<e2<<" "<<e3<<endl;}
template<class T1,class T2,class T3,class T4> void deb(T1 e1,T2 e2,T3 e3,T4 e4){cerr<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<endl;}
template<class T1,class T2,class T3,class T4,class T5> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5){cerr<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<endl;}
template<class T1,class T2,class T3,class T4,class T5,class T6> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5,T6 e6){cerr<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<" "<<e6<<endl;}

//int dx[]={1,0,-1,0}; int dy[]={0,1,0,-1}; ///4 ways
//int dx[]={1,1,0,-1,-1,-1,0,1}; int dy[]={0,1,1,1,0,-1,-1,-1}; ///8 ways
//int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1}; ///knight moves

int main()
{
    int t;
    tin(t);
    int h=1;
    while(t--)
    {
        vector<int> v;
        int n,p,s;
        tin3(n,s,p);
        int ans=0;
        int s1=0;
        for(int i=0;i<n;i++)
        {
            int x;
            tin(x);
            v.pb(x);
            int av=x/3;
            if(x==0&&p==0) {ans++;continue;}
            else if(x==0&&p!=0) continue;
            if(x==1)
            {
                if(p==1) {ans++;goto pre;}
                else if(p>1) goto pre;
            }
            if(av>=p) {ans++; pre: continue;}
            else
            {
               int df=x-(3*av);
               if(df==0)
               {
                   if(av+1>=p&&s1<s) {ans++;s1++;goto pre;}
               }
               else if(df==1)
               {
                   if(av+1>=p) {ans++;goto pre;}
                   //else if(av+2>=p&&s1<s) {ans++;s1++;goto pre;}
               }
               else if(df==2)
               {
                    if(av+1>=p) {ans++;goto pre;}
                    else if(av+2>=p&&s1<s) {ans++;s1++;goto pre;}
               }
            }
        }
        printf("Case #%d: %d\n",h++,ans);
    }
}
