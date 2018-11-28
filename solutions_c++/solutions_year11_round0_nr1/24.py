#include <ctime>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <functional>
#include <map>
#include <set>
#include <queue>
#include <fstream>
using namespace std;
#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fornd(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define forabd(i, a, b) for (int i = (int)(b); i >= (int)(a); i--)
#define tr(i, a) for (typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define pb push_back
#define mp make_pair
#define N 120
typedef long long ll;
int in[N], type[N], n;
int ans[N][N][N];
struct pos{
    pos(int a = 0, int b = 0, int c = 0):i(a), j(b), k(c){}
    int i, j, k;
};
int solve(){
    zero(ans);
    queue<pos> Q;
    Q.push( pos(1, 1, 0) );
    while(!Q.empty()){
        pos v = Q.front();Q.pop();
        //cerr << v.i << ' ' << v.j << ' ' << v.k << '=' << ans[v.i][v.j][v.k] << endl;
        if(v.k == n)
            return ans[v.i][v.j][v.k];
        for(int di = -1; di <= 1; di++)
            if( v.i + di >= 1 && v.i + di <= 100)
                for(int dj = -1; dj <= 1; dj++)
                    if( v.j + dj >= 1 && v.j + dj <= 100)
                    {
                        pos u(v.i + di, v.j + dj, v.k + (!di && type[v.k] && v.i == in[v.k]) + (!dj && !type[v.k] && v.j == in[v.k]));
                        if(!ans[u.i][u.j][u.k] && (u.i != 1 || u.j != 1 || u.k != 0)){
                            ans[u.i][u.j][u.k] = ans[v.i][v.j][v.k] + 1;
                            Q.push(u);
                        }
                    }
    }
    return -1;
}
int main() {
    int T;
    cin >> T;
    forn(_t, T){
        cin >> n;
        forn(t, n){
            char c;
            int x;
            cin >> c >> x;
            in[t] = x;
            type[t] = c == 'B';
        }
        cout << "Case #" << _t + 1 << ": " << solve() << endl;
    }
    return 0;
}
