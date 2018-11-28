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
#include <deque>
#include <cassert>

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

typedef pair<int, int> pint;

int N, R, C;

char board[20][20];

ll starting_situation;
ll final_situation;

int d[4][2] = {
    {-1, 0},
    {+1, 0},
    { 0,-1},
    { 0,+1},
};


ll serialize(vector<pint> &a) {
    sort(all(a));

    ll result = 0;

    FORE(it, a) {
        result *= 400;
        result += (it->first * 20 + it->second);
    }

    return result;
}

void deserialize(vector<pint> &a, ll id) {
    a.clear();

    REP(i, N) {
        int kw = id % 400;
        id /= 400;
        a.pb(make_pair(kw / 20, kw % 20));
    }

    sort(all(a));
}

bool is_connected(vector<pint> &a) {
    bool mat[6][6];
    REP(i, N) {
        REP(j, N) {
            mat[i][j] = (i == j);
        }
    }
    REP(i, N) {
        REP(j, N) {
            if (i == j) continue;
            REP(k, 4) {
                pint newp = make_pair(
                    a[i].first + d[k][0], a[i].second + d[k][1]);

                if (newp == a[j]) {
                    mat[i][j] = true;
                    mat[j][i] = true;
                }
            }
        }
    }
    REP(k, N) {
        REP(i, N) {
            REP(j, N) {
                if (mat[i][k] && mat[k][j]) {
                    mat[i][j] = true;
                }
            }
        }
    }
    REP(j, N) {
        if (!mat[0][j]) return false;
    }
    return true;
}


bool is_safe(pint a) {
    if (a.first < 0 || a.first >= R) return false;
    if (a.second < 0 || a.second >= C) return false;

    return true;
}

void enumerate_moves(ll from, vector<ll>& to) {
    vector<pint> fv;
    deserialize(fv, from);

    to.clear();

    char nboard[20][20];

    REP(r, R) {
        REP(c, C) {
            if (board[r][c] == '#')
                nboard[r][c] = '#';
            else
                nboard[r][c] = '.';
        }
    }
    REP(j, N) {
        nboard[fv[j].first][fv[j].second] = 'o';
    }

    REP(i, N) {
        REP(k, 4) {
            vector<pint> nv;
            nv = fv;


            bool infeasible = false;

            pint bk = make_pair(fv[i].first - d[k][0], fv[i].second - d[k][1]);

            if (!is_safe(bk)) continue;
            if (nboard[bk.first][bk.second] != '.') continue;

            pint nk = make_pair(fv[i].first + d[k][0], fv[i].second + d[k][1]);
            if (!is_safe(nk)) continue;

            if (nboard[nk.first][nk.second] != '.') continue;

            if (infeasible) continue;

            nv[i] = nk;

            to.pb( serialize(nv) );
        }
    }
}

int main(int argc, char *argv[]) {
    freopen(argv[1], "r", stdin);
    int Tests;
    cin >> Tests;
    FOR(test, 1, Tests+1) {
        printf("Case #%d: ", test);
        cin >>R >>C;
        string s;

        vector<pint> src;
        vector<pint> tgt;
        REP(i, R) {
            cin >> s;
            REP(j, C) {
                board[i][j] = s[j];
                if (board[i][j] == 'o' || board[i][j] == 'w') {
                    src.pb(make_pair(i, j));
                }
                if (board[i][j] == 'x' || board[i][j] == 'w') {
                    tgt.pb(make_pair(i, j));
                }
            }
        }

        N = src.sz;

        starting_situation = serialize(src);
        final_situation = serialize(tgt);

        map<ll, int> serials;
        deque<ll> q;
        serials[starting_situation] = 0;
        q.push_back(starting_situation);


        bool found = false;

        while (!q.empty())  {
            ll th = q.front();
            q.pop_front();
            int moves = serials[th];

            vector<pint> this_th;

            deserialize(this_th, th);
            bool is_conn = is_connected(this_th);

            vector<ll> nexts;

            enumerate_moves(th, nexts);
            FORE(it, nexts) {
                ll nx = *it;
                vector<pint> tm;
                deserialize(tm, nx);

                if (!is_conn && !is_connected(tm)) continue;

                if (serials.find(nx) == serials.end()) {
                    serials[nx] = moves + 1;
                    q.push_back(nx);
                    if (nx == final_situation) {
                        found = true;
                        break;
                    }
                }
                else {
                    //printf("%d %d\n", serials[nx], moves + 1);
                }
            }
            if (found) break;
        }
        if (serials.find(final_situation) == serials.end()) {
            cout << "-1" <<endl;
        }
        else {
            cout << serials[final_situation] <<endl;
        }
        
    }

    return 0;

}
