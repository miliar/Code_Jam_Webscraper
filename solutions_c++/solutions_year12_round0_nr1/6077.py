#include<iostream>
#include<sstream>
#include<string>
#include<cstdlib>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<cmath>
#include<cctype>
#include<set>
#include<bitset>
#include<algorithm>
#include<list>

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<ctype.h>

using namespace std;

#include <cstring>
#define deb(a...)          {cout<<" #--> ";dbg,a; cout<<endl;}
struct debugger
{
    ///Collected from rudradevbasak
    template<typename T> debugger& operator , (const T v)
    {
        cout<<v<<" ";
        return *this;
    }
} dbg;

#define FR(i,N)   for(i=0;i<N;i++)
#define BFR(i,N)  for(i=N;i>=0;i--)

#define SZ(a)       (int)a.size()
#define ll          long long
#define ull         unsigned long long
#define ISS         istringstream
#define OSS         ostringstream
#define VS          vector<string>
#define vi          vector<int>
#define vd          vector<double>
#define vll         vector<long long>
#define SII         set<int>::iterator
#define SI          set<int>
#define mem(a,b)    memset(a,b,sizeof(a))
#define fs          first
#define sc          second
#define pii         pair < int , int >

#define EQ(a,b)     (fabs(a-b)<ERR)
#define all(a,b,c)  for(int I=0;I<b;I++)    a[I] = c
#define CROSS(a,b,c,d) ((b.x-a.x)*(d.y-c.y)-(d.x-c.x)*(b.y-a.y))
#define sqr(a)      ((a)*(a))
#define FORE(i,a)   for(typeof((a).begin())i=(a).begin();i!=(a).end();i++)
#define ALL(a)       a.begin(),a.end()
#define rev(a)      reverse(ALL(a));
#define sorta(a)    sort(ALL(a))
#define pb          push_back
#define popb        pop_back
#define round(i,a)  i = ( a < 0 ) ? a - 0.5 : a + 0.5;
#define makeint(n,s)  istringstream(s)>>n
#define read()      freopen("test.txt","r",stdin)

//ll Pow(ll B,ll P){      ll R=1; while(P>0)      {if(P%2==1)     R=(R*B);P/=2;B=(B*B);}return R;}
//int BigMod(ll B,ll P,ll M){     ll R=1; while(P>0)      {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return (int)R;} /// (B^P)%M
//ll Gcd(ll a,ll b){ if(b==0)return a; Gcd(b,a%b); return;}

///int rrr[]={1,0,-1,0};int ccc[]={0,1,0,-1}; //4 Direction
///int rrr[]={1,1,0,-1,-1,-1,0,1};int ccc[]={0,1,1,1,0,-1,-1,-1};//8 direction
///int rrr[]={2,1,-1,-2,-2,-1,1,2};int ccc[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
///int rrr[]={2,1,-1,-2,-1,1};int ccc[]={0,1,1,0,-1,-1}; //Hexagonal Direction
///int month[]={31,28,31,30,31,30,31,31,30,31,30,31}; //month

int kkaass=1;
#define KAS()       printf("Case %d: ",kkaass++)
#define oo          (1<<30)
#define PI          3.141592653589793
#define pi          2*acos(0)
#define ERR         1e-5
#define PRE         1e-8
#define MAX         1000009

map<char,char>amap;

void makeMap()
{
    vector<string> a1,a2;
    a1.pb("ejp mysljylc kd kxveddknmc re jsicpdrysi");
    a1.pb("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
    a1.pb("de kr kd eoya kw aej tysr re ujdr lkgc jv");

    a2.pb("our language is impossible to understand");
    a2.pb("there are twenty six factorial possibilities");
    a2.pb("so it is okay if you want to just give up");

    for(int i=0;i<3;i++)
    {
        for(int j=0;j<SZ(a1[i]);j++)
        {
            amap[a1[i][j]]=a2[i][j];
        }
    }

    amap['z']='q';
    amap['q']='z';

    return;
}

int main()
{
    makeMap();
    freopen("goog.txt","w",stdout);
    int t;
    scanf("%d",&t);
    getchar();
    string ch;
    int k;
    for(k=1;k<=t;k++)
    {
        getline(cin,ch);
        printf("Case #%d: ",k);
        for(int i=0;i<SZ(ch);i++)
        {
            printf("%c",amap[ch[i]]);
        }
        printf("\n");
    }
    return 0;
}
