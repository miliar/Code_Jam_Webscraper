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

char get[300][300];
int bad[300][300];

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int testCount;
    cin >> testCount;
    forn(curTest, testCount){
        printf("Case #%d: ", curTest+1);

        //Place solution here
        memset(get, 0, sizeof get);
        memset(bad, 0, sizeof bad);

        int C, D, N;
        cin >> C;
        forn(i, C){
            string s;
            cin >> s;
            get[s[0]][s[1]] = s[2];
            get[s[1]][s[0]] = s[2];
        }
        cin >> D;
        forn(i, D){
            string s;
            cin >> s;
            bad[s[0]][s[1]] = bad[s[1]][s[0]] = true;
        }     
        cin >> N;

        string s;
        if(N != 0)
            cin >> s;

        vector<char> st;
        forn(i, N){
            st.pb(s[i]);

            while(sz(st) >= 2 && get[st[sz(st)-2]][st.back()] != 0){
                char c1 = st.back(); st.pop_back();
                char c2 = st.back(); st.pop_back();
                st.pb(get[c1][c2]);
            }

            bool was = false;
            forn(j, sz(st)){
                forn(k, j){
                    if(bad[st[j]][st[k]]){
                        was = true;
                        break;
                    }
                }
                if(was) break;
            }
            if(was)
                st.clear();
        }
        printf("[");
        forn(i, sz(st)){
            if(i)
                printf(", ");
            printf("%c", st[i]);
        }
        printf("]\n");
    }
    
    return 0;
}



