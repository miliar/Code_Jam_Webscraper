#include <cstdio>
#include <algorithm>
#include <vector>
#include <sstream>
#include <iostream>
#include <map>
#include <cctype>
#include <cassert>
using namespace std;
typedef long long LL;

int N;
string mat[100];
map<LL, int> memo;

int DX[] = { 1,-1,0,0 };
int DY[] = { 0,0,1,-1 };

inline bool valid(int y, int x) { return 0 <= y && y < N && 0 <= x && x < N; }

bool f(int y, int x, int n, int s)
{
    assert(valid(y, x) && isdigit(mat[y][x]));

    if (n == 1)
        return s == 0;

    LL key = n*1000 + y*25 + x;
    key += s * 1000000LL;

    if (memo.count(key)) return memo[key];
    int &res = memo[key];
    res = 0;

    for (int d1 = 0; d1 < 4; d1++) {
        if (!valid(y + DY[d1], x + DX[d1])) continue;

        int sign = mat[y + DY[d1]][x + DX[d1]] == '+' ? 1 : -1;
        for (int d2 = 0; d2 < 4; d2++) {
            int yy = y + DY[d1] + DY[d2];
            int xx = x + DX[d1] + DX[d2];
            if (!valid(yy, xx)) continue;

            int ss = s - sign * (mat[yy][xx] - '0');
            if (f(yy, xx, n-1, ss)) {
                return (res = 1);
            }
        }
    }

    return (res = 0);
}

map<LL, string> memo2;

string g(int y, int x, int n, int s)
{
    assert(f(y,x,n,s));
    if (n == 1) return string("") + mat[y][x];

    LL key = n*1000 + y*25 + x;
    key += s * 1000000LL;

    if (memo2.count(key)) return memo2[key];
    string &best = memo2[key];

    for (int d1 = 0; d1 < 4; d1++) {
        if (!valid(y + DY[d1], x + DX[d1])) continue;

        int sign = mat[y + DY[d1]][x + DX[d1]] == '+' ? 1 : -1;
        for (int d2 = 0; d2 < 4; d2++) {
            int yy = y + DY[d1] + DY[d2];
            int xx = x + DX[d1] + DX[d2];
            if (!valid(yy, xx)) continue;

            int ss = s - sign * (mat[yy][xx] - '0');
            if (!f(yy, xx, n-1, ss)) continue;

            string t;
            t += mat[y][x];
            t += mat[y + DY[d1]][x + DX[d1]];

            if (best == "" || t <= best.substr(0, 2)) {
                t += g(yy, xx, n-1, ss);
                if (best == "" || t < best)
                    best = t;
            }
        }
    }

    return best;
}

int main()
{
    int T,Q,X;
    cin >> T;

    for (int cs = 1; cs <= T; cs++) {
        cout << "Case #" << cs << ":\n";

        cin >> N >> Q;
        for (int i = 0; i < N; i++)
            cin >> mat[i];

        memo.clear();
        memo2.clear();

        for (int q = 1; q <= Q; q++) {
            cin >> X;

            string best = "";

            int len = 1;
            while (best == "") {
                assert(len < 1000);

                for (int i = 0; i < N; i++)
                for (int j = 0; j < N; j++)
                    if (isdigit(mat[i][j]) && f(i,j,len,X-mat[i][j]+'0')) {
                        string s = g(i,j,len,X-mat[i][j]+'0');
                        assert(s.size() > 0);
                        if (best == "" || s < best)
                            best = s;
                    }
                
                fprintf(stderr, "C%d Q%d len=%d memo=%u memo2=%u\n",
                        cs, q, len, memo.size(), memo2.size());

                len++;
            }

            cout << best << endl;

        }
    }
}
