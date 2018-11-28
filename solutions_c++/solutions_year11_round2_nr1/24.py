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

int n;
char s[200][200];

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    cout.precision(10); cout << fixed;

    int testCount;
    cin >> testCount;

    forn(curTest, testCount){
        printf("Case #%d:\n", curTest+1);
        cin >> n;
        gets(s[0]);
        forn(i, n){
            gets(s[i]);
        }

        vector<ld> wp(n, 0.0), owp(n, 0.0), oowp(n, 0.0);
        vector<int> cw(n, 0), ca(n, 0);
        forn(i, n){
            forn(j, n)
                ca[i] += s[i][j] != '.', cw[i] += s[i][j] == '1';
            wp[i] = ld(cw[i]) / ld(ca[i]);                    
//            cerr << wp[i] << endl;
        }

        forn(i, n){
            int cnt = 0; ld sum = 0.0;
            forn(j, n){
                if(s[i][j] != '.'){
                    cnt++;
                    ld cwp = ld(cw[j] - (s[j][i] == '1')) / ld(ca[j] - 1);
                    sum += cwp;
                }
            }
            owp[i] += sum / cnt;
//            cerr << owp[i] << endl;
        }

        forn(i, n){
            int cnt = 0; ld sum = 0;
            forn(j, n)
                if(s[i][j] != '.'){
                    cnt++;
                    sum += owp[j];
                }
            oowp[i] = sum / cnt;
        }
        
        forn(i, n){
            cout <<  double(0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]) << endl;
        }
    }
    
    return 0;
}



