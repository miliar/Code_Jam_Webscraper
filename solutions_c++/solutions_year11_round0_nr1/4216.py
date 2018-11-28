//**If I knew that pain is the worst thing in the world then I would have never made those sins**\\
#include <stdio.h>
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

typedef long long LL;

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

int main()
{
    freopen("1.txt","r",stdin);
    freopen("2.txt","w",stdout);

    int kase, tCase = 0; cin>>kase;

    while (kase--)
    {
        pair<int,int> resO[103], resB[103]; // <point,value>
        int n, i, serial[103], first, second, ret = 0, currO = 1, currB = 1; cin>>n;
        CL(serial,0);
        first = second = 0;
        resO[0] = resB[0] = MK(1,1);

        FOR(i,0,n)
        {
            char a; int b;
            cin>>a>>b;
            if (a=='B')
            {
                resB[++first] = MK(b,1+resB[first-1].second+abs(resB[first-1].first-b));
                serial[i] = 1;
            }
            else resO[++second] = MK(b,1+resO[second-1].second+abs(resO[second-1].first-b));
        }
        first = second = 0;
        FOR(i,0,n)
        {
            if (serial[i] == 0 && currO < resO[++second].second)
            {
                currB += (resO[second].second-currO);
                ret += (resO[second].second-currO);
                currO = resO[second].second;
            }
            else if (serial[i] == 0)
            {
                currB++;
                ret++;
                currO = resO[second].second;
            }
            else if (serial[i] == 1 && currB < resB[++first].second)
            {
                currO += (resB[first].second-currB);
                ret += (resB[first].second-currB);
                currB = resB[first].second;
            }
            else
            {
                currO++;
                ret++;
                currB = resB[first].second;
            }
        }
        printf ("Case #%d: %d\n",++tCase,ret);
    }

    return 0;
}
