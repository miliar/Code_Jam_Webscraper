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
#define print1(a)    cout<<a<<endl
#define print2(a,b) cout<<a<<" "<<b<<endl
#define print3(a,b,c) cout<<a<<" "<<b<<" "<<c<<endl
#define oo          (1<<30)
#define PI          3.141592653589793
#define pi          2*acos(0)
#define ERR         1e-5
#define PRE         1e-8
#define SZ          size()
#define LL          long long
#define ISS         istringstream
#define OSS         ostringstream
#define VS          vector<string>
#define VI          vector<int>
#define VD          vector<double>
#define VLL         vector<long long>
#define SII         set<int>::iterator
#define SI          set<int>
#define mem(a,b)    memset(a,b,sizeof(a))
#define fr(i,a,b)   for(i=a;i<=b;i++)
#define frn(i,a,b)  for(i=a;i>=b;i--)
#define fri(a,b)    for(i=a;i<=b;i++)
#define frin(a,b)   for(i=a;i>=b;i--)
#define frj(a,b)    for(j=a;j<=b;j++)
#define frjn(a,b)   for(j=a;j>=b;j--)
#define frk(a,b)    for(k=a;k<=b;k++)
#define frkn(a,b)   for(k=a;k>=b;k--)
#define frl(a,b)    for(l=a;l<=b;l++)
#define frln(a,b)   for(l=a;l>=b;l--)

#define EQ(a,b)     (fabs(a-b)<ERR)
#define all(a,b,c)  for(int I=0;I<b;I++)    a[I] = c
#define CROSS(a,b,c,d) ((b.x-a.x)*(d.y-c.y)-(d.x-c.x)*(b.y-a.y))
#define sqr(a)      ((a)*(a))
#define FORE(i,a)   for(typeof((a).begin())i=(a).begin();i!=(a).end();i++)
#define BE(a)       a.begin(),a.end()
#define rev(a)      revera))
#define pb          push_back
#define popb        pop_back
#define round(i,a)  i = ( a < 0 ) ? se(BE(a));
#define sorta(a)    sort(BE(a - 0.5 : a + 0.5;
#define makeint(n,s)  istringstream(s)>>n


int main()
{
    int t,kas=0;
    freopen("A-large.in","r",stdin);
    freopen("Aoutput.out","w",stdout);
    cin>>t;
    int n;
    while(t--)
    {
        char c;
        int p,poso=1,posb=1,o=0,b=0,t=0;
        cin>>n;
        while(n--)
        {
            cin>>c>>p;
            if(c=='O')
            {
                if(b)
                {
                    o=max(0,abs(p-poso)-b)+1;
                    t+=b;
                    b=0;
                    poso=p;
                }

                else
                {
                    o+=abs(p-poso)+1;
                    poso=p;
                }
            }

            else
            {
                 if(o)
                {
                    b=max(0,abs(p-posb)-o)+1;
                    t+=o;
                    o=0;
                    posb=p;
                }

                else
                {
                    b+=abs(p-posb)+1;
                    posb=p;
                }
            }
        }

        t+=o;
        t+=b;

        cout<<"Case #"<<++kas<<": "<<t<<endl;
    }
    return 0;
}
