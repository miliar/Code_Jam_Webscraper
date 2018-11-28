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
#include <deque>

using namespace std;

#define f(i, a, b) for(int i = a; i < b; i++)
#define rep(i, n)  f(i, 0, n)

char combine[30][30];
int oppose[30][30];

int main(){

    int T; scanf("%d", &T); for(int test = 1; test <= T; test++) {

        printf("Case #%d: ", test);

        memset(combine, -1, sizeof(combine));
        memset(oppose, 0, sizeof(oppose));

        int nc, nd, n;
        string s;

        cin >> nc;
        rep(i, nc) {
            cin >> s;
            rep(j, 3) s[j] -= 'A';
            combine[s[0]][s[1]] = combine[s[1]][s[0]] = s[2];
        }

        cin >> nd;
        rep(i, nd) {
            cin >> s;
            rep(j, 2) s[j] -= 'A';
            oppose[s[0]][s[1]] = oppose[s[1]][s[0]] = 1;
        }

        cin >> n;
        cin >> s;
        rep(i, n) s[i] -= 'A';

        deque<int> v;
        v.push_back(s[0]);

        f(i, 1, n) {

            v.push_back(s[i]);
            while(v.size() > 1) {

                int k = v.size();
                if(combine[v[k - 1]][v[k - 2]] != -1) {
                    v[k - 2] = combine[v[k - 1]][v[k - 2]];
                    v.pop_back();
                }
                else {

                    int o = 0;
                    rep(i, k) if(oppose[v[i]][v[k - 1]]) {
                        o = 1;
                        break;
                    }

                    if(o) v.clear();
                    break;

                }
            }
        }

        int k = v.size();
        printf("[");
        rep(i, k - 1)
            cout << char(v[i] + 'A') << ", ";
        if(k != 0) cout << char(v[k - 1] + 'A');
        printf("]\n");

    }
}
