/*
 *      dance.cpp
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

int n, s, p;
const int MAX = 128;
int S[MAX];

struct triple
{
    int a, b, c;
    bool surprise;
}; 

vector<triple> T[32];

bool valid(int a, int b, int c)
{
    if (c < 0 || c > 10) return false;
    
    if (c - a > 2) return false;
    
    return true;
}

bool surprising(int a, int b, int c)
{
    return (c - a == 2);
}

int memo[128][128];

int solve(int cur, int sur)
{
    if (cur == n) 
    { 
        if (sur == 0) return 0;
        return -1000000;
    }
    
    int &ret = memo[cur][sur];
    if (ret != -1) return ret;
    ret = max(0, solve(cur+1, sur));

    int sum = S[cur];
    int add = 0;
    rep(i,sz(T[sum]))
    {
        add = 0;
        if (T[sum][i].c >= p) add = 1;
        
        
        if (sur > 0 && T[sum][i].surprise) 
            ret = max(ret, add + solve(cur+1, sur-1));
            
        if (!T[sum][i].surprise)
            ret = max(ret, add + solve(cur+1, sur));
    
    }
    
    return ret;
}

vector<pair<int, pair<int,int> > > v1, v2;

int main()
{
	#ifdef Local
        freopen("/home/wasi/Desktop/input.txt", "r", stdin);
        freopen("/home/wasi/Desktop/output.txt", "w", stdout);
    #endif
    
    int t;
    /*//int M = 21;
    //xrep(i,0,10) xrep(j,0,10)  if (valid(i,j,M-i-j)) cout<<i<<" "<<j<<" " << M-i-j << " " << surprising(i,j,M-i-j)<<endl;
    int c = 0;
    
    xrep(i,0,10) xrep(del, 0, 2)
    {
        if (i+2>10) continue;
        if (del == 0) cout << i << " " << i << " " << i << endl; //v1.pb(mp(i,mp(i,i)));
        if (del == 1) 
        {
            cout << i << " " << i << " " << i+1 << endl;
            cout << i << " " << i+1 << " " << i+1 << endl;
            //v1.pb(mp(i,mp(i,i+1)));
            //v1.pb(mp(i,mp(i+1,i+1)));
            c +=2;
        }
        if (del == 2) 
        {
            cout << i << " " << i << " " << i+2 << endl;
            cout << i << " " << i+1 << " " << i+2 << endl;
            cout << i << " " << i+2 << " " << i+2 << endl;
            v1.pb(mp(i,mp(i,i+2)));
            v1.pb(mp(i,mp(i+1,i+2)));
            v1.pb(mp(i,mp(i+2,i+2)));
            c += 3;
        }
    }
    //cout<<c<<endl;
    */ 
    int cnt =  0;
    rep(i,11) rep(j,11) rep(k,11) if (i<=j && j<=k && valid(i,j,k))
    {
        T[i+j+k].pb((triple) {i, j, k, surprising(i,j,k) });
    }
    
    
    
    //cout<<cnt<<endl;
      //  if (!valid(i,j,k)) cout<<i<<" "<<j<<" "<<k<<endl;
    
    scanf("%d", &t);
    xrep(caseno, 1, t)
    {
        scanf("%d %d %d", &n, &s, &p);
        rep(i,n) scanf("%d", &S[i]);
        ms(memo, -1);
        //cout<<solve(0,s)<<endl;
        int ans = max(0, solve(0,s));
        //int ans = 0;
        
        /*if (n == 3)
        {
            rep(i,sz(T[S[0]])) rep(j,sz(T[S[1]])) rep(k,sz(T[S[2]]))
            {
                int cnt = 0, curans = 0;
                if (T[S[0]][i].surprise) cnt++;
                if (T[S[1]][j].surprise) cnt++;
                if (T[S[2]][k].surprise) cnt++;
                if (cnt != s) continue;
                if (T[S[0]][i].c >= p) curans++;
                if (T[S[1]][j].c >= p) curans++;
                if (T[S[2]][k].c >= p) curans++;
                if (curans > ans) ans = curans;
                if (caseno == 48 && curans == 1)
                {
                    cout << cnt << endl;
                    cout<<T[S[0]][i].a<<" "<<T[S[0]][i].b<<" "<<T[S[0]][i].c<<endl;
                    cout<<T[S[1]][j].a<<" "<<T[S[1]][j].b<<" "<<T[S[1]][j].c<<endl;
                    cout<<T[S[2]][k].a<<" "<<T[S[2]][k].b<<" "<<T[S[2]][k].c<<endl;
                }
            }
        }
        else if (n == 2)
        {
            rep(i,sz(T[S[0]])) rep(j,sz(T[S[1]]))
            {
                int cnt = 0, curans = 0;
                if (T[S[0]][i].surprise) cnt++;
                if (T[S[1]][j].surprise) cnt++;
                if (cnt != s) continue;
                if (T[S[0]][i].c >= p) curans++;
                if (T[S[1]][j].c >= p) curans++;
                if (curans > ans) ans = curans;
            }
        }
        else if (n == 1)
        {
            rep(i,sz(T[S[0]]))
            {
                int cnt = 0, curans = 0;
                if (T[S[0]][i].surprise) cnt++;
                if (cnt != s) continue;
                if (T[S[0]][i].c >= p) curans++;
                if (curans > ans) ans = curans;
            }
        }*/
        printf("Case #%d: %d\n", caseno, ans);
    }
    
    return 0;
}
