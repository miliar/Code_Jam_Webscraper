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

int main()
{
    freopen("1.txt","r",stdin);
    freopen("2.txt","w",stdout);

    int kase, tCase = 0; scanf ("%d",&kase);

    while (kase--)
    {
        int c, d, n, i; scanf ("%d",&c);
        char just[10000];
        string ret, one, two, test, ans;
        map<string,char>combine;
        map<char,char>oppose;
        FOR(i,0,c)
        {
            scanf ("%s",just);
            one += just[0]; one += just[1]; two += just[1]; two += just[0];
            combine[one] = just[2]; combine[two] = just[2];
        }
        scanf ("%d",&d);
        FOR(i,0,d)
        {
            scanf ("%s",just);
            oppose[just[0]] = just[1]; oppose[just[1]] = just[0];
        }
        scanf ("%d",&n);
        scanf ("%s",just);
        ret = just[0];
        FOR(i,1,n)
        {
            ret += just[i];
            test = ret[ret.size()-1]; test += ret[ret.size()-2];
            if (combine.find(test) != combine.end())
            {
                ret = ret.substr(0,ret.size()-2);
                ret += combine[test];
            }
            else if (oppose.find(ret[ret.size()-1]) != oppose.end() && ret.find(oppose[ret[ret.size()-1]]) != -1) ret = "";
        }
        ans += '[';
        FOR(i,0,ret.size())
        {
            if (i==0) ans += ret[i];
            else { ans += ", "; ans += ret[i]; }
        }
        ans += ']';
        printf ("Case #%d: %s\n",++tCase,ans.c_str());
    }

    return 0;
}
