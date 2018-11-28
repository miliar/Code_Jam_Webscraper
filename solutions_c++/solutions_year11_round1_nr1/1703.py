#include <cmath>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <vector>
using namespace std;

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define SETMIN(a,b) a = min(a,b)
#define SETMAX(a,b) a = max(a,b)
#define PB push_back
#define FORALL(i,v) for(typeof((v).end())i=(v).begin();i!=(v).end();++i)
#define CLR(x,a) memset(x,a,sizeof(x))
#define BEND(v) v.begin(),v.end()
#define MP make_pair
#define A first
#define B second

typedef unsigned long long int ull;
typedef long double ld;

int main() {

   freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    int t,n,pg,pd,x=0,f=0,peri,d,g;
    double per;
    cin>>t;
    while(t--)
    {
        x++;
        f=0;
        cin>>n>>pd>>pg;
        if(pd<100&&pg==100)
        {
             cout<<"Case #"<<x<<": Broken"<<endl; continue;
        }
        else if(pd>0&&pg==0)
        {
             cout<<"Case #"<<x<<": Broken"<<endl; continue;
        }
        for(int i=1;i<=n;i++)
        {
            per=((double)i*pd)/100;
            peri=(i*pd)/100;
            if(per-peri<1e-15) {f=1; d=i; break;}
        }
        if(!f) {cout<<"Case #"<<x<<": Broken\n"; continue;}
        f=0;
        for(int i=d;i<1000;i++)
        {
            per=((double)i*pg)/100;
            peri=(i*pg)/100;
            if(per-peri<1e-15)
            {
            g=i;
            double check; int p1,p2;
            p1=(d*pd)/100;
            p2=(g*pg)/100;
            if(g-p2<d-p1) {f=0; continue;}
            else {f=1; break;} }
        }
        if(!f) {cout<<"Case #"<<x<<": Broken\n"; continue;}
        else
        cout<<"Case #"<<x<<": Possible\n";

    }
    return 0;
}


