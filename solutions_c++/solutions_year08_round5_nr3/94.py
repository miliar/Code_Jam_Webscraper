#include <string>
#include <vector>
#include <deque>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <set>
#include <queue>
#include <map>
#include <bitset>
#include <cmath> 

#define FOR(i, a, b) for (int i=(int)(a); i<(int)(b); i++)
#define REP(i, n) for (int i=0; i<(int)(n); i++)
#define all(c) (c).begin(), (c).end()
#define tr(c, i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define pb push_back

using namespace std;

typedef vector <string> vs;
typedef vector <int> vi;
typedef long long ll; 

bool con[3201][3201];
int match[3201];
bool vis[3201];
bool cl[100][100];

int n, m;

bool aug(int a) {
    if (vis[a]) return 0;
    vis[a] = 1;
    for (int i=0; i<m; i++) {
        if (con[a][i] && (match[i]<0 || aug(match[i]))) {
            match[i] = a;
            return 1;
        }
    }
    return 0;
}

bool conn(pair<int, int> p1, pair<int, int> p2) {
    int a1=p1.first, b1=p1.second;
    int a2=p2.first, b2=p2.second;
    if (b1 == b2-1) {
        if (a1 == a2-1 || a1 == a2 || a1 == a2+1) return 1;
    }
    if (b1 == b2+1) {
        if (a1 == a2-1 || a1 == a2 || a1 == a2+1) return 1;
    }
    return 0;
}

pair<int, int> v1[3201];
pair<int, int> v2[3201];

int main () {
    int T, cs=0;
    cin >> T;
    int i, j;
    while (T--) {
        int M, N;
        char c;
        int v=0;
        cin >> M >> N;
        for (i=0; i<M; i++) {
            for (j=0; j<N; j++) {
                cin >> c;
                if (c == '.') {
                    cl[i][j] = 0;
                    v++;
                }
                else cl[i][j] = 1;
            }
        }
        n = 0;
        for (i=0; i<N; i+=2) {
            for (j=0; j<M; j++) {
                if (!cl[j][i]) {
                    v1[n++] = make_pair(j, i);
                }
            }
        }
        m = 0;
        for (i=1; i<N; i+=2) {
            for (j=0; j<M; j++) {
                if (!cl[j][i]) v2[m++] = make_pair(j, i);
            }
        }
        for (i=0; i<n; i++) {
            for (j=0; j<m; j++) {
                con[i][j] = conn(v1[i], v2[j]);
            }
        }
        //cout << "m n " << v1[0].first << " " << v1[0].second << endl;
        //cout << "m n " << v2[0].first << " " << v2[0].second << endl;
        for (i=0; i<m; i++) match[i] = -1;
        int r = 0;
        for (i=0; i<n; i++) {
            for (j=0; j<3201; j++) vis[j] = 0;
            if (aug(i)) {
                r++;
            }
        }
        cout << "Case #" << ++cs << ": " << v-r << endl;
        //cout << v << " " << r << endl;
    }
    return 0;
}
