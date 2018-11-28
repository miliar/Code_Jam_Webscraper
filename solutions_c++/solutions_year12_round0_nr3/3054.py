#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <queue>
#include <bitset>
#include <utility>
#include <list>
#include <numeric>

#include <cstdio>
#include <cmath>
#include <cctype>
using namespace std;

#define rep(i,a,b) for(__typeof(b) i=a; i<(b); ++i)
#define trav(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
const int ma = 2000001;
vector<int> q[ma];
int main()
{
    int moc = 1;
    int len = 0;
    rep(i,1,ma+1)
    {
        if (i == moc * 10)
        {
            moc *= 10;
            len++;
        }
        int mi = i, cur = i;
        rep(j,0,len)
        {
            cur = (cur % 10) * moc + cur / 10;
            mi = min(cur, mi);
        }
        q[mi].push_back(i);
    }

    int tt; scanf("%d", &tt);
    rep(sd,0,tt)
    {
        int a, b; scanf("%d %d", &a, &b);
        int res = 0;
        rep(i,0,int(ma))
        {
            rep(j,0,q[i].size()) if (a <= q[i][j] && q[i][j] <= b)
                rep(k,0,j) if (a <= q[i][k] && q[i][k] <= b)
                    res++;
        }
        printf("Case #%d: %d\n", sd+1, res);
    }
}
