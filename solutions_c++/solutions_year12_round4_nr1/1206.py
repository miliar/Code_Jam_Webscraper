
/* Author: Mahesh */

/// Takes around 5.1s :)

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

int l[200000], d[200000];
int D;
int N;
int ans[200000];

int solve(int c, int r){
    if (d[c]+r>=D) return 1;
    fori(i, c+1, N){
        if(d[c]+r>=d[i]){
            int rr = min(l[i], d[i]-d[c]);
            if (ans[i]!=-1 && rr>=ans[i]) return 1;
        }
        else{
            break;
        }
    }
    return 0;
}



int main()
{
    freopen("large.in", "r", stdin);
    freopen("o.txt", "w", stdout);
    int T=SS;

    rep(t, T){
        N=SS;
        rep(i, N){
            d[i] = SS;
            l[i] = SS;
        }
        D = SS;
        ifor(i, N-1, 0){
            int lo = 1, hi = l[i];
            while (lo<hi){
                int mid = (lo+hi)/2;
                if (solve(i, mid)){
                    hi = mid;
                }
                else{
                    lo = mid+1;
                }
            }
            if (solve(i, lo)){
                ans[i] = lo;
            }
            else{
                ans[i] = -1;
            }
        }
        if (ans[0]!=-1 && d[0]>=ans[0])
        {
            printf("Case #%d: YES\n", t+1);
        }
        else{
            printf("Case #%d: NO\n", t+1);
        }
    }
    return 0;
}


