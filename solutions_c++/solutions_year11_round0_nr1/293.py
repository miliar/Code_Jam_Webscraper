#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <memory>
#include <vector>
#include <string>
#include <bitset>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cmath>
#define sz(a) ((int)(a).size())
#define foreach(i, v) for(__typeof((v).begin()) i=(v).begin(); i!=(v).end(); i++)
using namespace std;
typedef long long llong;
typedef pair<string, int> Item;

const int Maxn = 100+10;
const int INF = 0x7f7f7f7f;
const double eps = 1e-10;
const double pi = acos(-1.0);
inline int realcmp(double a, double b){ return (a>b+eps) ? 1 : ((a+eps<b)?-1:0); }

Item it[Maxn];

int main()
{
    int ans, cas, n, pO, pB, tO, tB;
    ios::sync_with_stdio(0);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    cin>>cas;
    for(int c=1; c<=cas; c++)
    {
        cin>>n;
        pO = pB = 1;
        tO = tB = 0;
        for(int i=0; i<n; i++)
            cin>>it[i].first>>it[i].second;
        if( it[0].first[0] == 'O' )
        {
            tO = it[0].second-pO+1;
            pO = it[0].second;
            ans = tO;
        }
        else
        {
            tB = it[0].second-pB+1;
            pB = it[0].second;
            ans = tB;
        }
        for(int i=1; i<n; i++)
        {
            if( it[i].first[0] == 'O' )
            {
                if( it[i-1].first[0] == 'O' )
                    tO += abs(it[i].second-pO)+1;
                else
                    tO += max(abs(it[i].second-pO), tB-tO)+1;
                pO = it[i].second;
                ans = tO;
            }
            else
            {
                if( it[i-1].first[0] == 'B' )
                    tB += abs(it[i].second-pB)+1;
                else
                    tB += max(abs(it[i].second-pB), tO-tB)+1;
                pB = it[i].second;
                ans = tB;
            }
        }
        printf("Case #%d: %d\n", c, ans);
    }

    return 0;
}
