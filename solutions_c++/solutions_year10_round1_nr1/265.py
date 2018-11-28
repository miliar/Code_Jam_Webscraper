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

#define MAXN 50+5
int grid[MAXN][MAXN];
int g[MAXN][MAXN];
int N, K;

int main(){
    ifstream fin("A.in");
    ofstream fout("A.out");
    int t, kase = 0;
    fin >> t;
    string temp;
    while(t--){
        kase++;       
        fin >> N >> K;
	    REP(i, N){
            fin >> temp;
            REP(j, N){
                   if(temp[j] == '.')    grid[i][j] = -1;
                   else if(temp[j] == 'R')    grid[i][j] = 0;
                   else grid[i][j] = 1;
            }
        }
        REP(i, N)    REP(j, N)    g[j][N - 1 - i] = grid[i][j];
        REP(it, N){
             ROF(i, N - 2, -1)    REP(j, N){
                 if(g[i][j] >= 0 && g[i + 1][j] < 0)    swap(g[i][j], g[i + 1][j]);       
             }
        }
        int okb = 0, okr = 0;
        REP(i, N)    REP(j, N){
            int r = 0, b = 0;
            REP(k, K){
                if(j + k >= N)    break;
                if(g[i][j + k] == 0)    r++;
                else if(g[i][j + k] == 1)    b++;       
            }
            if(r == K)    okr = 1;
            if(b == K)    okb = 1;
            r = 0, b = 0;
            REP(k, K){
                if(i + k >= N)    break;
                if(g[i + k][j] == 0)    r++;
                else if(g[i + k][j] == 1)    b++;       
            }
            if(r == K)    okr = 1;
            if(b == K)    okb = 1;
            r = 0, b = 0;
            REP(k, K){
                if(i + k >= N || j + k >= N)    break;
                if(g[i + k][j + k] == 0)    r++;
                else if(g[i + k][j + k] == 1)    b++;       
            }
            if(r == K)    okr = 1;
            if(b == K)    okb = 1;
            r = 0, b = 0;
            REP(k, K){
                if(i + k >= N || j - k < 0)    break;
                if(g[i + k][j - k] == 0)    r++;
                else if(g[i + k][j - k] == 1)    b++;       
            }
            if(r == K)    okr = 1;
            if(b == K)    okb = 1;          
        }
        fout << "Case #" << kase << ": ";
        if(okr == 0 && okb == 0)    fout << "Neither\n";
        else if(okr == 0 && okb == 1)    fout << "Blue\n";
        else if(okr == 1 && okb == 0)    fout << "Red\n";
        else fout << "Both\n";         
    }
    fin.close();
    fout.close();
    // GI;
	return 0;
}
