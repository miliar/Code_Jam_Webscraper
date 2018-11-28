#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

#define FOR(A, I, B) for(int A = (int)I; A < (int)B; A++)
#define SZ(A) (int)(A).size()
#define vs vector<string>
#define vi vector<int>
#define pb push_back
#define pii pair<int, int>
#define ll long long
#define ERRO 1e-12
#define DEQ(X,Y) ( fabs((X) - (Y)) < ERRO)

vector< pii > moves; // bot / button

int main()
{
    int t;
    scanf("%d", &t);
    FOR(testcase, 0, t){
        int n;

        moves.clear();

        scanf("%d", &n);
        FOR(i, 0, n){
            char buff[3];
            int button;
            scanf("%s %d", buff, &button);

            int bot = buff[0] == 'O' ? 0 : 1;

            moves.pb(pii(bot, button));

        }

        int p = 0, resp = 0;
        int po = 1, pb = 1, to = 0, tb = 0;
        while(p < SZ(moves)){
            if(moves[p].first == 0){
                to = to + abs(po - moves[p].second) + 1;
                po = moves[p].second;
                if(tb > 0)
                    to = max(to, tb + 1);
                resp = to;
            } else {
                tb = tb + abs(pb - moves[p].second) + 1;
                pb = moves[p].second;
                if(to > 0)
                    tb = max(tb, to + 1);
                resp = tb;
            }
            p++;
        }
        printf("Case #%d: %d\n", testcase + 1, resp);
    }
    return 0;
}

