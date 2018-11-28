#include <iostream>
#include <cstdio>
#include <cctype>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cassert>
#include <string.h>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define GL ({LL t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})
#define FOR(i,a,b) for(LL i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define ROF(i,a,b) for(int i=a;i>b;i--)
#define SET(x,a) memset(x,a,sizeof(x));
#define all(a) a.begin(),a.end()
#define rall(a) a.rbegin(),a.rend()
#define tr(i,a) for( typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define pb push_back
#define sz(a) (int)(a.size())
#define INF (int)1e9
#define EPS (double)1e-9

#define is istringstream
#define os ostringstream
#define lb lower_bound
#define ub upper_bound
#define bs binary_search

typedef unsigned long long ULL;
typedef long long LL;
typedef set <int> si;
typedef pair< int,int > ii;
typedef vector< ii > vii;
typedef vector < vii > vvii;
typedef vector< int > vi;
typedef vector< vi > vvi;

#define MAXN 100+5
#define MAXM 255+5
int D, I, M, N;
int inp[MAXN];
LL mem[MAXN][MAXM];

LL go(int i, int prev){
    if(i == N)    return 0;
    LL &ans = mem[i][prev];
    if(ans >= 0)    return ans;
    ans = INF;
    ans = min(ans, D + go(i + 1, prev));
    if(prev > 255){
        REP(j, 256)    ans = min(ans, abs(j - inp[i]) + go(i + 1, j));
    }
    else{
        REP(j, 256){
            if(abs(j - prev) <= M){
                ans = min(ans, abs(j - inp[i]) + go(i + 1, j)); 
            }
        }     
    }
    
        if(prev > 255){
            REP(j, 256){
                ans = min(ans, I + go(i, j));       
            }
        }
        else{
            REP(j, 256){
                if(abs(j - prev) <= M){
                    ans = min(ans, I + go(i, j));
                }
            }     
        }
    return ans;
}

int main(){
    ifstream fin("B.in");
    ofstream fout("B.out");
    int t, kase = 0;
    fin >> t;
    while(t--){
        kase++;
        fin >> D >> I >> M >> N;
        REP(i, N)    fin >> inp[i];
        memset(mem, -1, sizeof(mem));
        LL ans = go(0, 256);
        fout << "Case #" << kase << ": " << ans << endl;           
    }
    // GI;
    fin.close();
    fout.close();
	return 0;
}
