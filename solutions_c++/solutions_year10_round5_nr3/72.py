
//Tomasz Kulczyński
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
using namespace std;

#define X first
#define Y second
#define MP make_pair
#define PB push_back
typedef long long ll;
typedef double D;
typedef long double ld;
typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))
int cond = 1;
#define db(x) {if(cond){cerr << __LINE__ << " " << #x << " " << x << endl; } }
#define dbv(x) {if(cond){cerr << __LINE__ << " " << #x << ": "; FORE(__i,x) cerr << *__i << " "; cerr << endl;} }

multiset<pair<int,int> > q;
map<int,int> ma;

void test()
{
    int c;
    scanf("%d",&c);
    q.clear();
    ma.clear();
    REP(i,c)
    {
        int x,y;
        scanf("%d %d",&x,&y);
        q.insert(MP(y,x));
        ma[x] = y;
    }
    int ret = 0;
    while(1)
    {
        multiset<pair<int,int> >::iterator p = q.end();
        p--;
        int a = p->X;
        if(a==1) break;
        int b = p->Y;
//        printf("%d %d :: \n",a,b);
  //      fflush(stdout);
        q.erase(p);
        ma[b] = a%2;
        if(a%2) q.insert(MP(1,b));
        ret += a/2;
        if(ma[b-1]) q.erase(MP(ma[b-1],b-1));
        q.insert(MP(ma[b-1] += a/2, b-1));
        if(ma[b+1]) q.erase(MP(ma[b+1],b+1));
        q.insert(MP(ma[b+1] += a/2, b+1));
    }
    printf("%d\n",ret);
}

int main()
{
    int dd,cas;
    scanf("%d",&dd);
    FOR(cas,1,dd)
    {
        printf("Case #%d: ",cas);
        test();
    }
    return 0;
}
