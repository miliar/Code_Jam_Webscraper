#pragma comment(linker, "/STACK:10000000")

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <sstream>

#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define ford(i, n) for(int i = int(n) - 1; i >= 0; --i)
#define fore(i, l, r) for(int i = int(l); i < int(r); ++i)
#define iter(i, v) for(typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)

#define sz(v) int((v).size())
#define all(v) (v).begin(), (v).end()
#define pb push_back

#define X first
#define Y second
#define mp make_pair

#define debug(x) {cerr << #x << " = " << x << endl;}

template<typename T> inline T abs(T a){ return ((a < 0) ? -a : a); }
template<typename T> inline T sqr(T a){ return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = (int)1E9 + 7;
const ld EPS = 1E-9;
const ld PI = 3.1415926535897932384626433832795;

const int NMAX = (int)1E3 + 7;

int a[200][200], sza;

void clear_(){
    memset(a, 0, sizeof a);
    sza = 0;
}


void get(int cc, int& ansHor){
    forn(dh, cc){
        bool good = true;
        forn(i, sza){
            int cnt = i < cc ? i + 1 : cc - (i - cc + 1);
            forn(j, cnt){
                int sym = -1;
                if(dh & 1){
                    if(i & 1){
                        int cidx = cnt / 2 + dh / 2;
                        sym = cidx + (cidx - j);

                    }else{
                        int cidx = cnt / 2 + dh / 2;
                        sym = cidx + (cidx - j) + 1;
                    }
                }else{
                    if(i & 1){
                        int cidx = cnt / 2 + dh / 2 - 1;

                        sym = cidx + (cidx - j) + 1;

                    }else{
                        int cidx = cnt / 2 + dh / 2;

                        sym = cidx + (cidx - j);
                    }
                }    

                if(sym < cnt && a[i][sym] != a[i][j])
                    good = false;

                if(!good) break;
            }

            if(!good) break;
        }

        if(good){
            ansHor = dh; 
            break;
        }
    }
}

void rotate_(int cc){
    
    vector<vector<int> > row;
    vector<int> size(sza);

    forn(i, sza){
        int cnt = i < cc ? i + 1 : cc - (i - cc + 1);

        size[i] = cnt - 1;
    }

    forn(i, cc){
        vector<int> cur;
        forn(j, cc){
            cur.pb(a[i + j][size[i + j]--]);            
        }
        row.pb(cur);
    }

    size.resize(sza);
    forn(i, sza) size[i] = 0;

    forn(i, cc){
        forn(j, cc){
            a[i + j][size[i + j]++] = row[i][cc - j - 1];                
        }
    }

}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int testCount;
    scanf("%d", &testCount);
    for1(NumberTest, testCount){
        printf("Case #%d: ", NumberTest);

        clear_();

        int cc;
        scanf("%d", &cc);

        sza = cc * 2 - 1;
        forn(i, sza){
            int cnt = i < cc ? i + 1 : cc - (i - cc + 1);
            forn(j, cnt)
                scanf("%d", &a[i][j]);
        }

        int ansHor = -1, ansVer = -1, ans3 = -1, ans4 = -1;

        get(cc, ansHor);
        rotate_(cc);
        get(cc, ansVer);
        rotate_(cc);
        get(cc, ans3);
        rotate_(cc);
        get(cc, ans4);


        assert(ansVer >= 0 && ansHor >= 0);

        int ans = sqr(cc + min(ansHor + ansVer, min(ansVer + ans3, min(ans3 + ans4, ans4 + ansHor)))) - sqr(cc);
        //int ans = sqr(cc + ansHor + ansVer) - sqr(cc);

        printf("%d\n", ans);
    }

    return 0;
}





















