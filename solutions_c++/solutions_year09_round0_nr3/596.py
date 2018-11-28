#include <iostream>
#include <stdio.h>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>
#include <utility>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int) n; ++i)
#define fore(i, a, b) for(int i = (int) a; i < (int) b; ++i)

#define ll long long
#define ld long double
#define PLL pair <ld, ld>

#define x first
#define y second

const ld EPS = 1e-9;
const int MAXN = 1000;
const int BASE = 10000;
string p = "welcome to code jam";
char tmp[MAXN];
string s;
int a[MAXN][30];

int main()
{
    freopen("input.txt","rt", stdin);
    freopen("output.txt", "wt", stdout);    
    int tk;
    scanf("%d\n", &tk);
    
    forn(ii, tk){
        getline(cin, s);
        
        memset(a, 0, sizeof a);
        a[0][0] = 1 % BASE;
        
        forn(i, s.size()){
            forn(j, p.size()){
                if (a[i][j] == 0) continue;
                
                fore(k, i, s.size()){
                    if (s[k] == p[j]){
                        a[k + 1][j + 1] += a[i][j];
                        
                        if (a[k + 1][j + 1] > BASE - 1){
                            a[k + 1][j + 1] -= BASE;
                        }                        
                    }
                }
            }
        }
        
        int ans = 0;
        
        forn(i, s.size() + 1){
            ans += a[i][p.size()];
            ans %= BASE;
        }
        
        stringstream ss;
        ss << ans;
        string res;
        ss >> res;
        while (res.size() < 4){
            res = "0" + res;
        }
        printf("Case #%d: %s\n", ii + 1, res.c_str());
    }
         
          
    return 0;
}

