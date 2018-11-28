#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;

#define f(i, a, b) for(int i = a; i < b; i++)
#define rep(i, n)  f(i, 0, n)

string s[10000], t[100];
int status[15];
int ok[10000];
int l;

int match(int i, char c) {

    int con = 0;
    rep(j, l) {
        if(status[j] != s[i][j] && status[j] != -1) return 0;
        if(s[i][j] == c) con = 1;
    }

    return con;

}

int contains(int i, char c) {

    rep(j, l) if(s[i][j] == c) return 1;
    return 0;

}

int main(){

    int T; scanf("%d", &T); for(int test = 1; test <= T; test++) {

        printf("Case #%d: ", test);

        int n, m; cin >> n >> m;
        rep(i, n) cin >> s[i];
        rep(i, m) cin >> t[i];

        rep(j, m) {

            int mxi = -1;
            int mxct = -1;

            rep(i, n) {

                l = s[i].length();
                rep(k, l) status[k] = -1;
                rep(k, n) ok[k] = 1;

                int ct = 0;

                rep(jj, 26) {

                    int f1 = 1;
                    int f2 = 1;

                    rep(k, n) if(s[k].length() == l && match(k, t[j][jj]) && ok[k]) {

                        f2 = 0;

                        rep(p, l)
                            if(s[i][p] == t[j][jj]) {
                                status[p] = s[i][p];
                                f1 = 0;
                            }

                        break;

                    }

                    // need to eliminate others
                    if(f1 == 0) {

                        rep(k, n) if(s[k].length() == l) {

                            // check if t[j][jj] appears not in status
                            rep(p, l) if(s[k][p] == t[j][jj] && status[p] != t[j][jj]) {
                                ok[k] = 0;
                                break;
                            }

                        }

                    }

                    if(f1 == 1 && f2 == 0) {

                        rep(k, n) if(s[k].length() == l && contains(k, t[j][jj])) {
                            ok[k] = 0;
                        }
                       
                        ct++;
                    }
                }

                if(ct > mxct) {
                    mxct = ct;
                    mxi = i;
                }
            }
            
            cout << s[mxi];
            if(j != m - 1) cout << ' ';
        }
        cout << endl;
    }
}
