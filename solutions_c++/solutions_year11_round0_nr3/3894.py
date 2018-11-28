#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <algorithm>
#include <sstream>
using namespace std;

#define chkB(a,n) (a[n>>3]&(1<<(n&7))) //char array
#define setB(a,n) (a[n>>3]|=(1<<(n&7))) //char array
#define UN(v) { SORT(v); v.erase(unique(v.begin(), v.end()),v.end()); }
#define SORT(c) sort((c).begin(),(c).end());
#define FOR(i,a,b) for (i=a; i<b; i++)
#define FORu(i,a,b) for (i=a; i>=b; i--)
#define FORstr(i,a,b) for (i=a; b[i]!=NULL; i++)
#define CL(a,b) memset(a, b, sizeof (a))
#define pb push_back
#define MK make_pair
#define inf (1<<30)
#define infL ((1<<63)-1)LL
#define pi double(2.0*acos(0))

int f(int a, int b, int n)
{
    int ret = 0, i, p = 1;
    FOR(i,0,n)
    {
        if ( (((1<<i) & a) && !((1<<i) & b)) || (!((1<<i) & a) && ((1<<i) & b)) )
        ret += (int)pow(2.,double(i));
    }
    return ret;
}

int main()
{
    freopen("1.txt","r",stdin);
    freopen("2.txt","w",stdout);
    int kase, tCase = 0; scanf ("%d",&kase);

    while (kase--)
    {
        int ans = 0, n, cok[20], i, j, total = 0; scanf ("%d",&n);
        CL(cok,0);
        FOR(i,0,n) { scanf ("%d",&cok[i]); total += cok[i]; }
        FOR(i,1,(1<<n))
        {
            int a = 0, b = 0, flagA = 0, flagB = 0, limit = 0;
            FOR(j,0,n)
                if ( ((1<<j) & i) ) { a = f(a,cok[j],n); limit += cok[j]; flagA = 1; }
                else { b = f(b,cok[j],n); flagB = 1; }

            if (a==b && flagA && flagB) ans = max(ans,max(limit,total-limit));
        }
        if (ans == 0) printf ("Case #%d: NO\n",++tCase);
        else printf ("Case #%d: %d\n",++tCase,ans);
    }

    return 0;
}
