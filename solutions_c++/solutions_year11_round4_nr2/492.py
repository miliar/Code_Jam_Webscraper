#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>

using namespace std;

#define FOR(i,a,b)	for(int i=(a); i<(b); ++i)
#define REP(iter,v) for(typeof((v).begin()) iter = (v).begin(); iter != (v).end(); ++iter)
#define MP make_pair
#define PB push_back
#define SZ size()
#define iss istringstream 

#define SORT(x) sort(x.begin(), x.end())
#define ALL(x) x.begin(), x.end()
#define UNIQUE(x) x.erase(unique(x.begin(),x.end()),x.end()) 
#define dbg(x) cerr << #x << " -> '" << (x) << "'\t"
#define dbge(x) cerr << #x << " -> '" << (x) << "'\n"

typedef long long ll, int64;
typedef vector<int> VI;

int64 INF = 1000*1000*1001;

int R, C, D;
string s[512];
int a[512][512];
int row[512], tot[512][512], ly[512][512], lx[512][512];

int areatot(int i1, int j1, int i2, int j2)    {
    return tot[i2][j2] - (j1 > 0 ? tot[i2][j1-1] : 0) - (i1 > 0 ? tot[i1-1][j2] : 0) + (j1 > 0 && i1 > 0 ? tot[i1-1][j1-1] : 0);
}

int arealy(int i1, int j1, int i2, int j2)    {
    return ly[i2][j2] - (j1 > 0 ? ly[i2][j1-1] : 0) - (i1 > 0 ? ly[i1-1][j2] : 0) + (j1 > 0 && i1 > 0 ? ly[i1-1][j1-1] : 0);
}

int arealx(int i1, int j1, int i2, int j2)    {
    return lx[i2][j2] - (j1 > 0 ? lx[i2][j1-1] : 0) - (i1 > 0 ? lx[i1-1][j2] : 0) + (j1 > 0 && i1 > 0 ? lx[i1-1][j1-1] : 0);
}

int main(void)	{
	int T;
	cin >> T;
	FOR (nc, 1, T+1)	{
        cin >> R >> C >> D;
        FOR (i, 0, R)   {
            cin >> s[i];
            FOR (j, 0, C)   {
                a[i][j] = s[i][j]-'0';
            }
        }
        
        memset(tot, 0, sizeof tot);
        FOR (i, 0, R)   {
            memset(row, 0, sizeof row);
            FOR (j, 0, C)   {
                row[j] = (j > 0 ? row[j-1] : 0) + a[i][j];
                tot[i][j] = (i > 0 ? tot[i-1][j] : 0) + row[j];
            }
        }
       
        /*
        FOR (i, 0, R)   {
            FOR (j, 0, C)   {
                cout << tot[i][j] << "\t";
            }
            cout << endl;
        }
        */

        FOR (i, 0, R)   {
            FOR (j, 0, C)   {
                int val = 0;
                FOR (k, 0, i+1) {
                    int mass = areatot(k, 0, k, j);
                    val += mass*(2*k+1);
                }
                ly[i][j] = val;
                
                val = 0;
                FOR (k, 0, j+1) {
                    int mass = areatot(0, k, i, k);
                    val += mass*(2*k+1);
                }
                lx[i][j] = val;
            }
        }
            
        int best = 0;
        
        FOR (k, 3, min(R, C) + 1)   {
            FOR (i, 0, R)   if(i+k-1 < R) {
                FOR (j, 0, C)   if(j+k-1 < C) {
                    int my = arealy(i, j, i+k-1, j+k-1);
                    int mx = arealx(i, j, i+k-1, j+k-1);
                    int mass = areatot(i, j, i+k-1, j+k-1);
                    
                    int ty = my - 2*mass*i;
                    int tx = mx - 2*mass*j;
                    
                    mass -= a[i][j] + a[i][j+k-1] + a[i+k-1][j] + a[i+k-1][j+k-1];
                    int cmp = mass*k;
                    
                    ty -= (a[i][j]+a[i][j+k-1])*1 + (a[i+k-1][j] + a[i+k-1][j+k-1])*(2*k-1);
                    
                    tx -= (a[i][j]+a[i+k-1][j])*1 + (a[i][j+k-1] + a[i+k-1][j+k-1])*(2*k-1);
                    
                    //if (i == 1 && j == 1 && k == 5) cout << tx << "\t" << ty << "\t" << mass << endl;
                    if (ty == cmp && tx == cmp) {
                        best = max(best, k);
                    }
                }
            }
        }
        
        cout << "Case #" << nc << ": ";
        if (best == 0)
            cout << "IMPOSSIBLE";
        else
            cout << best;
        cout << endl;
    }
	
}
