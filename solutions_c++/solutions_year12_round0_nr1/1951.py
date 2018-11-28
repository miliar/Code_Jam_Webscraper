
/* Author: Mahesh */

#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <string.h>
#include <memory.h>
#include <cassert>
#include <climits>
#include <cfloat>
#include <sstream>

using namespace std;

#define ford(i, a, b, c)        for(int i=(a); i<(b); i+=(c))
#define fori(i, a, b)           ford(i,a,b,1)
#define rep(i, n)               fori(i,0,n)
#define ifor(i, a, b)           for(int i=(a); i>=(b); i--)
#define iter(i, a)              for(typeof((a).begin()) i=(a).begin(); i!=(a).end(); i++)
#define si(x)                   ((int)x.size())
#define SS                      ({int x;scanf("%d",&x);x;})
#define pb                      push_back
#define mp                      make_pair
#define all(a)                  a.begin(),a.end()
#define SORT(v)                 sort(all(v))
#define fill(a, v)              memset(a, v, sizeof(a))
#define inf                     (int)1e9
#define linf                    (long long)1e18
#define V                       vector
#define S                       string
#define XX                      first
#define YY                      second
#define P(v)                    rep(i, si(v)) cout<<v[i]<<" "; puts("")

typedef V<int> vi;
typedef V<S> vs;
typedef long long ll;
typedef pair<int,int> pii;

/* Program Body starts here */
S s;
S I[] = {"qzejp mysljylc kd kxveddknmc re jsicpdrysi",
        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
        "de kr kd eoya kw aej tysr re ujdr lkgc jv"};

S O[] = { "zqour language is impossible to understand",
          "there are twenty six factorial possibilities",
          "so it is okay if you want to just give up"
        };

char m[26]={};

void preprocess() {
    rep(i, 3) {
        rep(j, si(I[i])){
            if (isalpha(I[i][j])){
                m[I[i][j]-'a'] = O[i][j];
            }
        }
    }
    rep(i, 26) {
       // cout<<char(i+'a')<<" "<<m[i]<<endl;

    }

}

int main ()
{
    freopen("in.in", "r", stdin);
    freopen("o.txt", "w", stdout);
    preprocess();
    int t = SS;
    getchar();
    rep (i, t) {
        getline(cin, s);
        S ans = "";
        rep(j, si(s)) {
            if (isalpha(s[j]))
                ans += m[s[j]-'a'];
            else
                ans += " ";
        }
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }
}


