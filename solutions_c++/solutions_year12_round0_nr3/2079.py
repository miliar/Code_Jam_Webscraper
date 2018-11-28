
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


int solve(int N, int B) {
    int x = N;
    int len = 0;
    int dig[10];
    map<int,int> vis;
    int pw = 1;
    while (x){
        dig[len++] = x%10;
        x/=10;
        pw*=10;
    }
    pw/=10;
    x = N;
    rep(i, len-1) {
        x = dig[i]*pw + x/10;
        if (dig[i]>0 && x > N && x<=B){
            vis[x] = 1;
        }
    }
    return si(vis);
}


/*int go(int N, int B){
    char ch[50];
    map<int,int> vis;
    sprintf(ch, "%d", N);
    S s(ch);
    int l = si(s);
    int ans = 0;
    fori(i, 1, l) {
        if (s[l-i]!='0'){
            int permuted = s2i(s.substr(l-i, i) + s.substr(0, l-i));
            if (permuted > N && permuted <= B) {
                vis[permuted] = 1;
            }
        }
    }
    return si(vis);
}*/


int main()
{
    freopen("in.in", "r", stdin);
    freopen("o.txt", "w", stdout);

    int T = SS;
    rep(t, T) {
        int A = SS, B = SS, ans = 0;
        fori(i, A, B) {
            ans += solve(i, B);
        }
        printf("Case #%d: %d\n", t+1, ans);
    }
    return 0;
}











