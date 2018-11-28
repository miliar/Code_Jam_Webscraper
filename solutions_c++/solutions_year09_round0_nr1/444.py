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
#include <ctime>
#include <cstring>
#include <cassert>

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define ford(i, n) for(int i = int(n) - 1; i >= 0; --i)
#define fore(i, l, r) for(int i = int(l); i < int(r); ++i)
#define sz(v) int((v).size())
#define X first
#define Y second
#define all(v) (v).begin(), (v).end()
#define mp(q, p) make_pair(q, p)
#define sqr(a) ((a) * (a))
#define pb push_back
#define ensure(a) assert(a)

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = 1E9 + 7;
const int NMAX = 1E3 + 7;
const ld EPS = 1E-9;

bool used[40][500];

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int L, D, N;
    scanf("%d%d%d\n", &L, &D, &N);
    vector<string> word(D);

    forn(i, D) getline(cin, word[i]);

    forn(T, N){
        memset(used, 0, sizeof(used));
        printf("Case #%d: ", T + 1);
        string s;
        getline(cin, s);
        int idx = 0;
        bool inBrack = false;
        forn(i, sz(s)){
            if(s[i] == '(') inBrack = true;
            if(s[i] == ')') idx++, inBrack = false;

            if(isalpha(s[i])){
                used[idx][s[i] - 'a'] = true;
                if(!inBrack) idx++;
            }
        }

        int cnt = 0;
        if(L == idx)
            forn(i, D){
                bool good = true;
                forn(j, L){
                    if(!used[j][word[i][j] - 'a']){
                        good = false;
                        break;
                    }
                }
                cnt += good;
            }
        cout << cnt << endl;
    }
    return 0;
}
