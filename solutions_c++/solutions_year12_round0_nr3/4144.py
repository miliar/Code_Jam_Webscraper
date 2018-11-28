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
        int a,b;
        tin2(a,b);
        int ans=0;
        char ch[100];
        sprintf(ch,"%d",b);
        string s1=ch;
        map<string,int> m;
        for(int i=a;i<b;i++)
        {
            char c[100],c1;
            sprintf(c,"%d",i);
            string s=c;
            for(int j=s.size()-1;j>=1;j--)
            {
                string on=string(s.end()-(s.size()-j),s.end())+string(s.begin(),s.end()-(s.size()-j));
                //deb("bhitor",s,on,ans,s1);
                //if(m[on]==1||)
                if(on[0]=='0'||on<=s) continue;
                else if(on<=s1) {ans++;}
            }
            //Wait;
        }
        printf("Case #%d: %d\n",h++,ans);
    }
}
