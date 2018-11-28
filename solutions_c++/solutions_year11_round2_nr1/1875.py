#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define FOR(i, x)    for (int i = 0; i < x; i++)
#define FORI(i,a, x) for (int i = a; i < x; i++)
#define ALL(x)       (x).begin(), (x).end()
#define FORE(i, x)   for (__typeof__((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define SZ(x)        ((int) (x).size())
#define INF          0x3F3F3F3F

const int dx[]  = {-1, 0,0,1};
const int dy[]  = { 0,-1,1,0};
const int dx8[] = {-1,-1,-1, 0,0, 1,1,1};
const int dy8[] = {-1, 0, 1,-1,1,-1,0,1};
const double PI = acos(-1.0);

int main()
{
//    freopen("A.in","r",stdin);
//    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-large.in","r",stdin);
//    freopen("A-small-attempt0.out","w",stdout);
    freopen("A-large.out","w",stdout);

    int T, N;
    string str;

    getline(cin,str);
    sscanf(str.c_str(),"%d",&T);
    FOR(TT,T)
    {
        getline(cin,str);
        sscanf(str.c_str(),"%d",&N);

        vector<string> m(N);
        vector<int> wins(N,0), played(N,0), loses(N,0);

        printf("Case #%d:\n",TT+1);

        FOR(i,N)
        {
            getline(cin,m[i]);
            FOR(j,N)
            {
                if(m[i][j] == '1')
                {
                    played[i]++;
                    wins[i]++;
                }
                else if(m[i][j] == '0')
                {
                    played[i]++;
                    loses[i]++;
                }
            }
        }
        double wp = 0.0, owp = 0.0, oowp = 0.0, tmp;
        int w, p;
        FOR(i,N)
        {
            wp = wins[i] * 1.0 / played[i] * 1.0;
//            printf("wp[%d]=%.6lf\n", i+1, wp);

            owp = 0.0;
            int cnt = 0;
            FOR(j,N)
            {
                if(i == j) continue;
                if(m[i][j]=='.') continue;
                w = 0, p = 0;
                cnt++;
                FOR(k,N)
                {
                    if(i == k) continue;
                    if(m[j][k] == '.') continue;
                    p++;
                    if(m[j][k] == '1') w++;
                }
                owp += w * 1.0 / p * 1.0;
            }
            owp /= cnt * 1.0;
//            printf("owp[%d]=%.6lf\n", i+1, owp);

            oowp = 0.0, tmp = 0.0;
            cnt = 0;
            int cnt2 = 0;
            FOR(l,N)
            {
                if(i == l) continue;
                if(m[i][l]=='.') continue;
                tmp = 0.0;
                cnt2 = 0;
                FOR(j,N)
                {
                    if(l == j) continue;
                    if(m[l][j]=='.') continue;
                    w = 0, p = 0;
                    cnt2++;
                    FOR(k,N)
                    {
                        if(l == k) continue;
                        if(m[j][k] == '.') continue;
                        p++;
                        if(m[j][k] == '1') w++;
                    }
                    tmp += w * 1.0 / p * 1.0;
                }
                tmp /= cnt2 * 1.0;
//                printf("%d - owp[%d]=%.6lf\n", i, l, tmp);
                oowp += tmp;
                cnt++;
            }
//            printf("cnt=%d\n", cnt);
            oowp /= cnt * 1.0;
//            printf("oowp[%d]=%.6lf\n", i+1, oowp);

            printf("%.9lf\n", 0.25 * wp + 0.5 * owp + 0.25 * oowp);
        }
    }

    return 0;
}
