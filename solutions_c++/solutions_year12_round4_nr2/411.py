#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stdio.h>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>
#include <assert.h>
#define REP(i,n) for(int i=0;i<n;i++)
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))
#define FILL(x,c) memset(x,c,sizeof(x))

using namespace std;

const double eps = 1e-8;

#define PB push_back
#define MP make_pair

typedef map<int,int> MII;
typedef map<string,int> MSI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<long double> VD;
typedef pair<int,int> PII;
typedef long long int64;
typedef long long ll;
typedef unsigned int UI;
typedef long double LD;
typedef unsigned long long ULL;

long long x[9999], y[9999];
long long r[9999];

bool intersect(int i, int j)
{
    return ((x[i]-x[j])*1ll*(x[i]-x[j])+(y[i]-y[j])*1ll*(y[i]-y[j])>=(r[i]+r[j])*1ll*(r[i]+r[j]));
}

long long dx[4] = {1, -1, 0, 0},
    dy[4] = {0, 0, -1, 1};

int idx[9999];

bool cmp(const int i, const int j)
{
    return r[i] < r[j];
}

int id[99999];

int main()
{
    freopen("C:\\GCJ\\B-large.in", "r", stdin);
    freopen("C:\\GCJ\\bl.txt", "w", stdout);
    int T, nowCase = 0;
    cin >> T;
    while (T--)
    {
        int n, w, h;
        cin >> n >> w >> h;
       // ++w, ++h;
        REP(i, n) cin >> r[i];
        REP(i, n) idx[i] = i;
        sort(idx, idx+n, cmp);
        sort(r, r+n);
        reverse(r, r+n);
        reverse(idx, idx+n);
        REP(i, n) id[idx[i]] = i;
        x[0] = 0, y[0] = 0;
        REP(i, n)
        {
            if (!i) continue;
            bool ok = false;
            REP(k, i)
            {
                REP(rr, 4)
                {
                    x[i] = x[k]+dx[rr]*(r[i]+r[k]);
                    y[i] = y[k]+dy[rr]*(r[i]+r[k]);
                    if (x[i] >= 0 && y[i] >= 0 && x[i] < w && y[i] < h)
                    {
                        bool ok1 = true;
                        REP(j, i) if (!intersect(i, j))
                        {
                            ok1 = false;
                            break;
                        }
                        ok |= ok1;
                        if (ok1) break;
                    }
                }
                if (ok) break;
            }
            if (!ok) i /= 0;
        }
        REP(i, n) REP(j, n) if (i != j)
        {
            if (x[i] < 0 || y[i] < 0 || x[j] < 0 || y[j] < 0 || x[i] >= w || x[j] >= w || y[i] >= h || y[j] >= h)
                i /= 0;
            if (intersect(i, j) == false)
                i /= 0;
        }
        printf("Case #%d:", ++nowCase);
        REP(i, n) cout << " " << x[id[i]] << " " << y[id[i]];
        printf("\n");
    }
	return 0;
}
