/*
 *      recycle.cpp
 */

using namespace std;

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#define EPS 1e-11
#define inf ( 1LL << 31 ) - 1
#define LL long long

#define _rep( i, a, b, x ) for( __typeof(b) i = ( a ); i <= ( b ); i += x )
#define rep( i, n ) _rep( i, 0, n - 1, 1 )
#define rrep( i, a, b ) for( __typeof(b) i = ( a ); i >= ( b ); --i )
#define xrep( i, a, b ) _rep( i, a, b, 1 )
#define foreach(it,a) for( typeof(( a ).begin()) it=( a ).begin();it!=( a ).end();it++)

#define abs(x) (((x)< 0) ? (-(x)) : (x))
#define all(x) (x).begin(), (x).end()
#define ms(x, a) memset((x), (a), sizeof(x))
#define mp make_pair
#define pb push_back
#define sz(k) (int)(k).size()

typedef vector <int> vi;

int p[10];
char length[10000010];
vector< pair<int,int> > pairs;

int main()
{
    p[0] = 1;
    xrep(i,1,6) p[i] = p[i-1] * 10;
    
    xrep(i,1,2000000) length[i] = floor(log10(i)+1);
    
    xrep(i,1,2000000)
    {
        int len = length[i], cur = i, last;
        set<int> S;
        rep(j,len)
        {
            last = cur % 10;
            cur /= 10;
            cur = p[len-1] * last + cur;
            if (length[cur] != len) continue;
            if (S.find(cur) != S.end()) continue;
            S.insert(cur);
            if (cur < i) 
            {
                pairs.pb(mp(cur, i));
            }
        }
    }
    
	#ifdef Local
        freopen("/home/wasi/Desktop/input.txt", "r", stdin);
        freopen("/home/wasi/Desktop/output.txt", "w", stdout);
    #endif
    
    
    
    int ans = 0, a, b, t;
    scanf("%d", &t);
    xrep(caseno, 1, t)
    {
        scanf("%d %d", &a, &b);
        ans = 0;
        rep(i,sz(pairs))
        {
            if (pairs[i].second > b) break;
            if (a <= pairs[i].first && pairs[i].second <= b) 
                ans++;
        }
        printf("Case #%d: %d\n", caseno, ans);
    }

    
    return 0;
}
