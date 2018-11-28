#define _CRT_SECURE_NO_DEPRECATE
#pragma warning(disable:4530)
#include <string>
#include <vector>
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <sstream>
#include <set>
#include <cmath>
#include <map>
#include <cassert>
#include <stack>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(it,x) for(typeof((x).begin())it=(x).begin();it!=(x).end();++it)
#define all(x) (x).begin(),(x).end()
#define CLR(x,v) memset(x,v,sizeof(x))
#define pb push_back
#define sz size()
#define exist(c,x) ((c).find(x)!=(c).end())
#define cexist(c,x) (find(all(c),x)!=(c).end())
#define SMIN(a, b) a = min((a),(b))
#define SMAX(a, b) a = max((a),(b))

typedef long long ll;

#define MAX_VERT 1000
class BipartiteMatching {
public:
    int N;
    int M;
    vector<int> ed[MAX_VERT];
    vector<int> ied[MAX_VERT];

    int ma[MAX_VERT], ima[MAX_VERT];


    BipartiteMatching(int N, int M) : N(N), M(M) {
        REP(i, N) {
            ma[i] = -1;
        }
        REP(j, M) {
            ima[j] = -1;
        }
    }
    
    void connect(int v, int w) {
        ed[v].pb(w);
        ied[w].pb(v);
    }

    void greedyMatch() {
        REP(i, N) {
            if (ma[i] != -1) continue;
            FORE(it, ed[i]) {
                int j = *it;
                if (ima[j] == -1) {
                    ma[i] = j;
                    ima[j] = i;
                    break;
                }
            }
        }
    }

    bool augment() {
        bool visited[MAX_VERT];
        int origin[MAX_VERT];

        stack<int> st;

        REP(i, N) {
            visited[i] = false;
            origin[i] = -1;

            if (ma[i] == -1) {
                visited[i] = true;
                st.push(i);
            }
        }

        while (!st.empty()) {
            int v = st.top();
            st.pop();

            FORE(it, ed[v]) {
                int w = *it;
                if (ma[v] == w) continue;
                if (ima[w] == -1) {
                    vector<int> left;
                    vector<int> right;
                    right.pb(w);
                    int pv = v;
                    while (true) {
                        left.pb(pv);
                        if (ma[pv] == -1) break;
                        right.pb(ma[pv]);
                        pv = origin[pv];
                    }
                    REP(i, left.sz) {
                        int lv = left[i];
                        int lw = right[i];
                        ma[lv] = lw;
                        ima[lw] = lv;
                    }
                    //  We found the answer, back-track, augment and print
                    return true;
                }
                if (visited[ima[w]]) continue;
                visited[ima[w]] = true;
                origin[ima[w]] = v;
                st.push(ima[w]);
            }
        }

        return false;
    }

};


int main(int argc, char *argv[]) {
    freopen(argv[1], "r", stdin);
    int Tests;
    cin >> Tests;
    FOR(test, 1, Tests+1) {
        printf("Case #%d: ", test);
        int n, k;
        int W[MAX_VERT][50];
        cin >>n >>k;

        BipartiteMatching b(n, n);
        
        REP(i, n) {
            REP(j, k) {
                cin >> W[i][j];
            }
        }

        REP(i, n) {
            REP(j, n) {
                if (i == j) continue;
                bool dom = true;
                REP(l, k) {
                    if (W[i][l] <= W[j][l]) {
                        dom = false;
                        break;
                    }
                }
                if (dom) {
                    //cout << "***" <<i << "," <<j << endl;
                    b.connect(i, j);
                }
            }
        }
        b.greedyMatch();
        while (b.augment()) {
        }

        //cout <<endl;
        int cnt = 0;
        REP(i, n) {
            //cout << "===" << b.ima[i] <<endl;
            if (b.ima[i] == -1) cnt++;
        }
        cout <<cnt <<endl;

    }

}
