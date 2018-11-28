#define _CRT_SECURE_NO_DEPRECATE

#include <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <ctime>
using namespace std;

#define sz(x) int((x).size())
#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(int (i) = (a); (i) >= (b); --(i))
#define rep(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define fe(i,a) for (int (i) = 0; (i) < int((a).size()); ++(i))
#define C(a) memset((a),0,sizeof(a))
#define inf 1000000000
#define eps 1e-9
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define pi 2*acos(0.0)
#define sqr(a) (a)*(a)
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second

typedef vector<int> vint;
typedef long long ll;
typedef pair<int, int> pii;


char a[10][10];
bool dot;
int T;

bool look_for(char P)
{
    bool flag;

    // looking in rows
    rep(j, 4)
    {
        flag = true;
        rep(i, 4)
            if (a[j][i] != P && a[j][i] != 'T')
            {
                flag = false;
                break;
            }
        if (flag)
            return true;
    }

    // looking in columns
    rep(j, 4)
    {
        flag = true;
        rep(i, 4)
            if (a[i][j] != P && a[i][j] != 'T')
            {
                flag = false;
                break;
            }
        if (flag)
            return true;
    }

    // looking in diag1
    flag = true;
    rep(i, 4)
        if (a[i][i] != P && a[i][i] != 'T')
        {
            flag = false;
            break;
        }
    if (flag)
        return true;

    // looking in diag2
    flag = true;
    rep(i, 4)
        if (a[i][3 - i] != P && a[i][3 - i] != 'T')
        {
            flag = false;
            break;
        }
    if (flag)
        return true;

    return false;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("a_output.txt", "w", stdout);

    scanf("%d\n", &T);
    FOR(test, 1, T)
    {
        rep(j, 5)
            gets(a[j]);

        dot = false;
        rep(i, 4)
            rep(j, 4)
                if (a[i][j] == '.')
                    dot = true;

        printf("Case #%d: ", test);
        if (look_for('X'))
            printf("X won\n");
        else if (look_for('O'))
            printf("O won\n");
        else if (dot)
            printf("Game has not completed\n");
        else
            printf("Draw\n");
    }

    return 0;
}
